import requests

with open("../database/pokemon.txt", "r") as pokemon_database:
    for pokemon_name in pokemon_database:
        pokemon_name = pokemon_name.strip("\n")
        downloadurl = f'https://img.pokemondb.net/artwork/{pokemon_name}.jpg'
        req = requests.get(downloadurl)
        filename = f'../img/{pokemon_name}.jpg'
        with open(filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
