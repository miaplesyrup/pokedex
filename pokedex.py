import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    # response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format{name})
    # print(response.json())

    pokemon = response.json()
    # print(pokemon["name"])
    # print(pokemon["id"])

    print(f"Name: {pokemon['name'].capitalize()}")
    print(f"ID: {pokemon['id']}")
    print(f"Base XP: {pokemon['base_experience']}")




if __name__ == "__main__":
    search_pokemon(sys.argv[1])