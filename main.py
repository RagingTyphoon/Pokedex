from Pokemon import Pokemon
import requests

def get_pokemon(poke_num):
    # This is a function for fetching all of the pokemon data

    # --- Basic Data (number, name, and types) ---
    base_url = f"https://pokeapi.co/api/v2/pokemon/{poke_num}"
    base_data = requests.get(base_url).json()

    '''
    to capitalize a string, simply use the .capitalize(). Example:
    ex_1 = "bloop"
    print(ex_1) -> bloop
    ex_2 = "bloop".capitalize()
    print(ex_2) -> Bloop
    '''
    name = base_data["name"].capitalize()
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
    evol_url = species_data["evolution_chain"]["url"]
    evol_data = requests.get(evol_url).json()

    evol = []

    current_evol = evol_data["chain"]

    while current_evol:
        '''
        We need to get the pokedex number of each evolution in the 
        current_evol list we make above this while loop.

        THIS is what the current_evol["species"] looks like in the JSON file:

        "species": {
            "name": "ivysaur",
            "url": "https://pokeapi.co/api/v2/pokemon-species/2/"
        }

        To do that, we need to parse the "url" part in the "species" category
        of the JSON data, just as we do with the name using

                current_evol["species"]["nam"]

        So, for instance, if we are looking at the evolution one up from
        bulbasaur, we could get

                current_evol_url = current_evol["species"]["url"]

        Then current_evol_url will store the string

                "https://pokeapi.co/api/v2/pokemon-species/2/"

        Finally, we can parse this string to get the number between the last two //
        using the .split("/") function

                url_components = current_evol_url.split("/")

        That SHOULD give us a list of the pieces of the URL where the final element
        is the number of the pokemon.

        THEN, we can check if that number is less than 147, and if it is, decide
        not to add it to the evol list.
        '''

        current_evol_url = None
        url_components = None
        current_evol_number = None
        if current_evol_number < 147:
            evol.append(current_evol["species"]["name"])

        if len(current_evol["evolves_to"]) > 0:
            # move on to next evolution
            current_evol = current_evol["evolves_to"][0]
        # if we want the loop to break, we can set current_evol to None
        else:
            current_evol = None
    
    # GOAL at end of function:
    return Pokemon(poke_num, name, types, desc, evol)

if __name__ == "__main__":
    # This is where the main program is initialized

    '''
    When the program starts, what do you want the user to see?

    Enter Pokemon ID, or "exit" to end: 
    '''

    # Make a list of valid pokemon id's from '1' to '146'
    VALID_IDS = [str(i) for i in range(1,147)]
    while True:
        # check if the user types exit, and if so, break
        user_entry = input("Enter Pokemon ID, or \"exit\" to end: ")
        if user_entry == "exit":
            break
        elif user_entry in VALID_IDS:
            print(get_pokemon(user_entry))
        else:
            print("Not a valid entry. Try again.")