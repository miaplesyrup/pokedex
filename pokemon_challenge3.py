import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")

    pokemon = response.json()

    if response.status_code == 200:
        pokemon = response.json()
        
        # Print Name
        print(f"Name: {pokemon['name'].capitalize()}")
        
        # Check if 'stats' and 'moves' are present in the response JSON
        if 'stats' in pokemon and 'moves' in pokemon:
            # Print HP
            hp = pokemon['stats'][0]['base_stat']
            print(f"HP: {hp}")
            
            # Print Attacks
            attacks = [move['move']['name'] for move in pokemon['moves']]
            print(f"Attacks: {', '.join(attacks)}")
        else:
            print("HP and Attacks data not found for this Pokémon.")
        
        # Check if 'held_items' is present in the response JSON
        if 'held_items' in pokemon:
            # Print Held Items
            held_items = [item['item']['name'] for item in pokemon['held_items']]
            print(f"Held Items: {', '.join(held_items)}")
        else:
            print("Held Items data not found for this Pokémon.")
    else:
        print("Pokemon not found!")



if __name__ == "__main__":
    search_pokemon(sys.argv[1])