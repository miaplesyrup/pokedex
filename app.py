# pylint: disable=trailing-whitespace
"""
you need a docstring
"""
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

"""kelangan ulit ng docstring"""
def search_pokemon(name):
    """doctring ulit"""
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)
    if response.status_code == 404:
        return None  
    pokemon_data = response.json()
    
    return {
        "name": pokemon_data.get('name', '').capitalize(),
        "id": pokemon_data.get('id', ''),
        "hp": pokemon_data.get('stats', [{}])[0].get('base_stat', ''),
        "attacks": [move.get('move', {}).get('name', '') for move in pokemon_data.get('moves', [])],
        "held_items": [item.get('item', {}).get('name', '') 
        for item in pokemon_data.get('held_items', [])],
        "image_url": pokemon_data.get('sprites', {}).get('front_default', ''),
    }

@app.route("/", methods=["GET", "POST"])
def index():
    """docstring ulit"""
    pokemon_data = None
    
    if request.method == "POST":
        pokemon_name = request.form["pokemon_name"].lower()
        pokemon_data = search_pokemon(pokemon_name)
    
    return render_template("index.html", pokemon_data=pokemon_data)

if __name__ == "__main__":
    app.run(debug=True)
    