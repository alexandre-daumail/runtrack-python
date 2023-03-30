import json

ENCODINGS = ['utf-8', 'latin-1', 'cp1252']
POKEMON_FILE = 'pokemon.json'
DATA_FILE = '../job01/data.txt'


def load_pokemon_names():
    for encoding in ENCODINGS:
        try:
            with open(POKEMON_FILE, 'r', encoding=encoding) as f:
                data = json.load(f)
                return [pokemon['name']['english'] for pokemon in data]
        except UnicodeDecodeError:
            pass
    raise Exception("Failed to load Pokemon data using all encodings")


def find_pokemon_names():
    pokemons = load_pokemon_names()
    with open(DATA_FILE, 'r') as f:
        data = f.read()
        words = data.split()
        print('Looking for pokemon')
        for pokemon in pokemons:
            if pokemon in words:
                print(f"{pokemon} found!")


find_pokemon_names()
