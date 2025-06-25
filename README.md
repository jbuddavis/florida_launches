**Upcoming Florida Rocket Launches**

- This repository creates an automatically updating calendar of upcoming Florida Rocket Launches
- Rocket launch data is from the Launch Library 2 API (https://ll.thespacedevs.com/docs/#/launches/launches_upcoming_list)
- API is queried every 6 hours to find the next 25 FL-Based launches
- Based on the API a python script creates an updated .ics calendar file 
- The .ics file can be accessed using: https://jbuddavis.github.io/florida_launches/cape_launches.ics
- This should give you a good idea when the upcoming launches are

For Google Calendars:
- Navigate to: https://calendar.google.com/calendar/u/0/r
- At the Bottom Left it says "Other Calendars"
- Next to Other Calendars, click the "+" Sign
- Select "From URL"
- Past this link: https://jbuddavis.github.io/florida_launches/cape_launches.ics
- Google will sync the .ics file periodically
