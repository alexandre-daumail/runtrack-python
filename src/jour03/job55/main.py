import json

encodings = ['utf-8', 'latin-1', 'cp1252']

for encoding in encodings:
    try:
        with open('pokemon.json', 'r', encoding=encoding) as f:
            data = json.load(f)
            pokemons = []
            for pokemon in data:
                pokemons.append(pokemon['name']['french'])
        print(f"Successfully loaded data using encoding {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to load data using encoding {encoding}")

with open('../job01/data.txt', 'r') as f:
    data = f.read()
    for pokemon in pokemons:
        if pokemon in data:
            print(f"{pokemon} found!")
