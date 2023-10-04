# import requests
# import sys

# def search_pokemon(name):
#     response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")

#     pokemon = response.json()

#     if response.status_code == 200:
#         pokemon = response.json()
#         if 'stats' in pokemon and 'moves' in pokemon:
#             hp = pokemon['stats'][0]['base_stat']
#             print(f"HP: {hp}")
#             attacks = [move['move']['name'] for move in pokemon['moves']]
#             print(f"Attacks: {', '.join(attacks)}")
#         else:
#             print("HP and Attacks data not found for this Pokémon.")
        
#         # Check if 'held_items' is present in the response JSON
#         if 'held_items' in pokemon:
#             # Print Held Items
#             held_items = [item['item']['name'] for item in pokemon['held_items']]
#             print(f"Held Items: {', '.join(held_items)}")
#         else:
#             print("Held Items data not found for this Pokémon.")
#     else:
#         print("Pokemon not found!")



# if __name__ == "__main__":
#     search_pokemon(sys.argv[1])




import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")

    pokemon = response.json()
    print(pokemon)

    name = pokemon.get('name', '').capitalize()
    print(f"Name: {name}")
    print(f"Name: {pokemon['name'].capitalize()}")
    print(f"ID: {pokemon['id']}")

    hp = pokemon.get('stats', [{}])[0].get('base_stat', '')
    print(f"HP: {hp}")
    print(f"HP: {pokemon['stats'][0]['base_stat']}")
    

    attacks = [] 
    for move in pokemon.get('moves', []):
        move_name = move.get('move', {}).get('name', '')
        attacks.append(move_name)
    print(f"Attacks: {', '.join(attacks)}")

    held_items = []
    for item in pokemon.get('held_items', []):
        item_name = item.get('item', {}).get('name', '')
        held_items.append(item_name)
    print(f"Held items: {', '.join(held_items)}")



def main():
    while True:
        pokemon_name = input("Enter a Pokemon name (or 'exit' to quit): ").lower()

        if pokemon_name == 'exit':
            break

        search_pokemon(pokemon_name)

if __name__ == "__main__":
    main()
