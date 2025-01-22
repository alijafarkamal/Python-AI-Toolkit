from pytrends.request import TrendReq

# Predefined regions for trending searches
available_regions = {
    'united_states': 'united_states',
    'india': 'india',
    'japan': 'japan',
    'germany': 'germany',
    'united_kingdom': 'united_kingdom',
    'australia': 'australia',
    'canada': 'canada',
    'france': 'france',
    'italy': 'italy',
    'netherlands': 'netherlands',
    'russia': 'russia',
    'south_korea': 'south_korea',
    'spain': 'spain',
    'sweden': 'sweden',
    'brazil': 'brazil',
    'mexico': 'mexico',
    'pakistan': 'pakistan'
}

pytrends = TrendReq()

region = input("Enter the region: ").lower().replace(" ", "_")

if region in available_regions:
    trending_searches = pytrends.trending_searches(pn=available_regions[region])
    print("\nTrending Searches:")
    print(trending_searches)
else:
    print("Invalid region. Please enter a valid region from the following list:")
    for region_name in available_regions.keys():
        print(region_name.replace("_", " ").title())