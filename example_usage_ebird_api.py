
from datetime import date
from ebird.api import Client
from ebird.api import get_observations
from ebird.api import get_top_100, get_totals
from ebird.api import get_nearby_observations
from ebird.api import get_visits, get_checklist
from ebird.api import get_regions, get_adjacent_regions, get_region
from ebird.api import get_hotspots, get_nearby_hotspots, get_hotspot
from ebird.api import get_taxonomy, get_taxonomy_forms, get_taxonomy_versions
from ebird.api import get_notable_observations, get_nearby_notable, get_species_observations, get_nearby_species, get_nearest_species

"""
Documentation for the eBird API: https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest#intro
Available translations for species names: http://help.ebird.org/customer/portal/articles/1596582
Information on the taxonomy used by eBird: http://help.ebird.org/customer/portal/articles/1006825-the-ebird-taxonomy
"""


api_key = "2hig7s0jt391"


#OBSERVATIONS

# Get observations from Woodman Pond, Madison county, New York for the past week.
records = get_observations(api_key, 'L227544', back=7)
print(records)

# Get observations from Madison county, New York
records = get_observations(api_key, 'US-NY-053')
print(records)

# Get observations from New York
records = get_observations(api_key, 'US-NY')
print(records)

# Get observations from the USA - don't overdo the data downloads
records = get_observations(api_key, 'US')
print(records)
"""
Any where you pass in single location or region you can also pass in a list or a comma-separated string.
 You can specify up to 10 locations or regions:
"""
# Get the observations for the most visited locations in Madison county, New York:
# Woodman Pond, Ditch Bank Rd., Cornell Biological Field Station and
# Anne V Pickard Memorial Wildlife Overlook.
locations = ['L227544', 'L273783', 'L677871', 'L2313391']
get_observations(api_key, locations, provisional=True, detail='full')


# Get the observations for Suffolk, Nassau and Queens counties in New York state.
counties = 'US-NY-103,US-NY-059,US-NY-81'
records = get_observations(api_key, locations, hotspot=False, category='species')
print(records)


#Different locale
"""
The functions that return observations, checklists or taxonomy support allow the common name for species to be returned
 in different languages:
"""
records = get_observations(api_key, 'CA-QC', locale='fr')
print(records)

# Get the most recent sightings of all species seen in the last week within
# 10km of Point Reyes National Seashore.
records = get_nearby_observations(api_key, 38.05, -122.94, dist=10, back=7)
print(records)

"""
The calls to get_observations() and get_nearby_observation() return all the available records.
 You can limit the set of records returned to only include notable ones (locally or nationally rare species) or
  limit the records to a small number of species:
"""

# Get the interesting birds seen in New York state.
records = get_notable_observations(api_key, 'US-NY')
print(records)

# Get the observations of Horned Lark (Eremophila alpestris) in New York state.
records = get_species_observations(api_key, 'horlar', 'US-NY')
print(records)

# Get the interesting birds within 50kn of Point Reyes
records = get_nearby_notable(api_key, 38.05, -122.94, dist=50)
print(records)

# Find out if Barn Swallows have been seen in the area in the past 10 days
records = get_nearby_species(api_key, 'barswa', 38.05, -122.94, back=10)
print(records)

# Where is the closest place to Cornell Lab of Ornithology to see
# Tennessee Warbler.
locations = get_nearest_species('tenwar', 42.48, -76.45)
print(locations)


#CHECKLISTS

"""
There are two functions for finding out what has been seen at a given location.
 First you can get the list of checklists for a given country, region or location using get_visits().
  Each result returned has the unique identifier for the checklist.
   You can then call get_checklist() to get the list of observations.
"""

# Get visits made recently to locations in New York state:
records = get_visits(api_key, 'US-NY')
print(records)

# Get visits made recently to locations in New York state on Jan 1st 2010
records = get_visits(api_key, 'US-NY', '2010-01-01')
print(records)

# Get the details of a checklist
checklist = get_checklist(api_key, 'S22536787')
print(checklist)


#HOTSPOTS

"""
There are two functions for discovering hotspots. get_hotspots() list all the locations in a given area.
 You can find all the hotspots visited recently by given a value for the back argument. get_nearby_hotspots() is used
  to find hotspots within a given radius. get_hotspot() can be used to get information on the location of a given hotspot.
"""

# List all the hotspots in New York state.
hotspots = get_hotspots(api_key, 'US-NY')
print(hotspots)

# List all the hotspots in New York state visited in the past week.
recent = get_hotspots(api_key, 'US-NY', back=7)
print(recent)

# List all the hotspots in New York state visited in the past week.
recent = get_hotspots(api_key, 'US-NY', back=7)
print(recent)

# List all the hotspots in within 50kn of Point Reyes
nearby = get_nearby_hotspots(api_key, 38.05, -122.94, dist=50)
print(nearby)

# Get the details of Anne V Pickard Memorial Wildlife Overlook in New York state.
details = get_hotspot(api_key, 'L2313391')
print(details)

#REGIONS

"""
eBird divides the world into countries, subnational1 regions (states) or subnational2 regions (counties).
 You can use get_regions() to get the list of sub-regions for a given region.
  For the approximate area covered by a region use get_region().
"""

# Get the list of countries in the world.
countries = get_regions(api_key, 'country', 'world')
print(countries
      )
# Get the list of states in the US.
states = get_regions(api_key, 'subnational1', 'US')
print(states)

# Get the list of counties in New York state.
counties = get_regions(api_key, 'subnational2', 'US-NY')
print(counties)

# Get the list of states which border New York state.
nearby = get_adjacent_regions(api_key, 'US-NY')
print(nearby)

# Get the approximate area covered by New York state.
bounds = get_region(api_key, 'US-NY')
print(bounds)


#TAXONOMY

"""
You can get details of all the species, subspecies, forms etc. in the taxonomy used by eBird.
 It's the easiest way of getting the codes for each species or
  subspecies, e.g. horlar (Horned Lark), cangoo (Canada Goose), etc., that are used in the other API calls.
"""

# Get all the species in the eBird taxonomy.
taxonomy = get_taxonomy(api_key)

# Get all the species in the eBird taxonomy with common names in Spanish
names = get_taxonomy(api_key, locale='es')

# Get all the taxonomy for Horned Lark
species = get_taxonomy(api_key, species='horlar')

# Get the codes for all the subspecies and froms recognised for Barn Swallow.
forms = get_taxonomy_forms(api_key, 'barswa')

# Get information on all the taxonomy revisions, i.e. versions.
# Usually only the latest is important.
versions = get_taxonomy_versions(api_key)


#STATISTICS
"""
You can also get some statistics from the eBird data.
 The most interesting is probably get_top_100() which return the list of observers who have seen the most species or
  submitted the largest number of checklists. The list is just for a specific day
   so it is really only useful for "Big Days" when lots of people are out trying to get the greatest number of species.
   You can also get some statistics from the eBird data. The most interesting is probably get_top_100() which
    return the list of observers who have seen the most species or submitted the largest number of checklists.
     The list is just for a specific day so it is really only useful for "Big Days"
      when lots of people are out trying to get the greatest number of species.
"""
# Get the winner of the Global Big Day in New York, on 5th May 2018
winners = get_top_100(api_key, 'US-NY', '2018-05-05')
print(winners)

# Get the number of contributors, checklist submitted and species seen today
totals = get_totals(api_key, 'US-NY', date.today())
print(totals)

#CLIENT

"""
There is a simple Client class which wraps the various functions from the API.
 You can set the API key and locale when creating a Client instance so you don't have to keep passing them as arguments.
 The client supports all the API functions.
"""

locale = 'es'

client = Client(api_key, locale)
results = client.get_observations('MX-OAX') #MEXICO - OAXACA