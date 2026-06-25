import requests
import json

# Step 1: defining the URL target
url = "https://pokeapi.co/api/v2/pokemon-species/1"

# Step 2: Make a "get" request (asking the API for data)
response = requests.get(url)

# Step 3: turn "response" into something usable (a JSON)
pokemon_data = response.json()

f = open("bulbasaur-species.json", "w")
f.write(json.dumps(pokemon_data, indent=4))

'''
There are several API URLs that all contain different information.
The one above (.../pokemon/1/) gives the name, type(s)
Another, (.../pokemon-species/1/) gives descriptions (flavor_text) and
    the evolution chain. HOWEVER, the evolution chain is actually its
    own API call, at (.../evolution-chain/1/)

What does this mean for us? Well, we'll have to have three different
URL variables for each piece of information we want to store.
'''