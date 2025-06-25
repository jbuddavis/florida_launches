#!/usr/bin/env python3
import requests, uuid, pytz
from datetime import datetime
from icalendar import Calendar, Event  # pip install icalendar pytz

API_URL = ("https://ll.thespacedevs.com/2.3.0/launches/upcoming/"
           "?mode=list&format=json&limit=10&location__ids=12,27")

tz = pytz.timezone("America/New_York")          # East-coast times
cal = Calendar()
cal.add("prodid", "-//Cape Launch Feed//github.com/you//")
cal.add("version", "2.0")

for launch in requests.get(API_URL, timeout=30).json()["results"]:
    ev = Event()
    ev.add("summary", launch["name"])
    ev.add("dtstart", datetime.fromisoformat(launch["window_start"].replace("Z", "+00:00")))
    ev.add("dtend", datetime.fromisoformat(launch["window_end"].replace("Z", "+00:00")))
    ev.add("description", (launch.get("status") or {}).get("description", "No mission info"))
    ev.add("location", "KSC")
    ev["uid"] = f'{launch["id"]}@thespacedevs'   # stable UID per launch
    ev.add("status", launch["status"]["name"])
    cal.add_component(ev)

with open("cape_launches.ics", "wb") as f:
    f.write(cal.to_ical())
