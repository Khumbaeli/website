The DayTrip Climber site was a Django-based web application I developed that helped Chapel Hill climbers plan their outdoor sessions. While no longer active, it combined weather forecasting, drive times, and a crowdsourced photo gallery to help users find optimal climbing conditions.
The site's climb finder tool would take your current location and preferred temperature range for climbing (most users set this between 45-75°F), then query several locations within a 3-hour drive radius. It would cross-reference hourly weather forecasts with drive times from the Google Maps API to suggest potential climbing spots where the weather would be good when you actually arrived.

I built a gallery section where users could upload their own climbing photos, tag the location and grade of the routes, and add beta (climbing advice). Each photo included EXIF data scraping to automatically record when the photo was taken, helping other climbers understand seasonal conditions.
Looking back, this was an interesting project that solved a real problem for the climbing community - namely finding that sweet spot where driving distance, arrival time, and weather conditions all lined up perfectly. Unfortunately, I took it offline a while back when the API costs started adding up, but it was a great learning experience in combining multiple data sources into something useful.
