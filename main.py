from Pokemon import Pokemon
import requests

def get_pokemon(poke_num):
    # This is a function for fetching all of the pokemon data

    # --- Basic Data (number, name, and types) ---
    base_url = f"https:/pokeapi.co/api/v2/pokemon/{poke_num}"
    base_data = requests.get(base_url).json()

    name = base_data["name"]
    # types = [base_data["types"][0]["type"]["name"], base_data["types"][1]["type"]["name"]]
    types = [t["type"]["name"] for t in base_data["types"]]


    # --- Description ---
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{poke_num}"
    species_data = requests.get(species_url).json()

    desc = "Description not found."

    for entry in species_data["flavor_text_entries"]:
        if entry["language"]["name"] == "en" and entry["version"]["name"] == "firered":
            desc = entry["flavor_text"].replace("\n", " ").replace("\f", " ")
            break

    # --- Evolution Chain ---
    evol_url = f"https://pokeapi.co/api/v2/evolution-chain/{poke_num}"
    evol_data = requests.get(evol_url).json()

    evol = []

    current_evol = evol_data["chain"]

    # GOAL at end of function:
    return Pokemon(poke_num, name, types, desc, evol)

if __name__ == "__main__":
    # This is where the main program is initialized
    bulbasaur = get_pokemon(1)
    print(bulbasaur)