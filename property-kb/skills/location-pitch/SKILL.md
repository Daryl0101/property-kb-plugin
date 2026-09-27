---
name: location-pitch
description: Answer where a Malaysian new property project is and what is around it (schools, stations, malls, hospitals, highways, commute to work, what a buyer may worry about) with Property KB, and pitch it truthfully. Use when an agent asks about a project's location, nearby places, distances, travel or commute times, or whether it is "in KL".
---

# Talking about a project's location

Property KB holds the map of KL, Selangor and Putrajaya (© OpenStreetMap contributors): states,
districts, council areas, towns, schools, stations, malls, hospitals, parks, highways and rail
lines. It also holds what documents say about each project's location ("5 mins to LRT"). The
two are kept apart, so you can say which is which.

## Steps

1. **Where it is**: `get` the project with `include=["location"]`. Each area comes with its
   basis:
   - "official": the project's point is inside that area's boundary;
   - "loose": a document says so, or it is the nearest area.

   A brochure's "KL" for a project in Petaling Jaya is loose. Say "near KL (the brochure says
   KL; officially it is in Petaling Jaya, Selangor)".
2. **What is around it**: `nearby` with the project and the categories the buyer cares about
   (the table below). You get the nearest places of each kind with straight-line metres, the
   nearest exit of each highway and station of each rail line, and places not yet open under
   their own heading. You also get what the documents and the map measured for places the
   project's documents name.
3. **How far to one place**: `distance` between the project and the place, or `"lat,lon"` for
   an office. It gives the straight line, any brochure or map figures for that pair, and a rail
   route by the timetables' minutes (walk, ride, changes).

## Which places for which buyer

| Buyer | Categories | Radius |
|---|---|---|
| Young family | `school`, kindergarten, park, clinic, supermarket | 3 km |
| Expat or international-school family | school_international, hospital, mall | 5 km |
| Car-free or first job | rail_station, rail_line, supermarket | 1 km |
| Driver or commuter | highway (the nearest exits) | 3 km |
| Retiree | hospital, clinic, park, place_of_worship | 3 km |
| Student or investor for student rental | university (and college) | 3 km |

## Commute checks (to an office or a school)

- Straight-line distance is a floor: a road trip is never shorter. Use it to cut a long list,
  then route the shortlist (at most 10) with your own maps if you have a maps tool, and give
  both figures, each labelled ("12 km in a straight line; about 25 min by car at 8 am per
  Google Maps").
- Without a maps tool, give the straight line and the rail route from `distance`. Never turn
  a straight line into minutes by car.
- Rail minutes come from the timetables; some stops are estimates, and the answer says which.
  The total includes walking at 80 m a minute and 5 minutes per change, but not waiting.

## Rules

- **Travel times from brochures are the developer's claim**, and may not be advertised to
  buyers (HDR reg 8(1A)(d); the warning says so). Give the distance, and give the time only
  labelled as "the developer states …". Map road times assume no traffic.
- **Sensitive places**: cemeteries, funeral homes, landfills, sewage plants, substations,
  prisons, high-voltage lines. Look them up (`include_sensitive`) only when the client or agent
  asks, or when they would clearly want to know before buying. Say what and how far, plainly,
  without judging ("a Hindu cemetery 1.9 km west").
- **Not in the knowledge base**: crime, flooding, traffic at peak hour, school rankings, noise,
  zoning plans, internet coverage, assessment tax, prices of resale units. Say so; never
  estimate them.
- Everyday places (restaurants, cafés, convenience shops, banks, petrol stations) are not
  stored: use your own maps for them, or say so.
- A place `nearby` lists with `opening_status` is not open yet: say "under construction,
  expected …", never "near an MRT station".
