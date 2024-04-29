import requests

# For Pokemon 0-9
# pokemon_number = 1
# while(pokemon_number<=9):
#     downloadurl = f"https://www.serebii.net/pokemon/art/00{pokemon_number}.png"
#     req = requests.get(downloadurl)
#     filename = f"img/00{pokemon_number}.png"
#     with open(filename, "wb") as f:
#         for chunk in req.iter_content(chunk_size=8192):
#             if chunk:
#                 f.write(chunk)
#     pokemon_number += 1

# For Pokemon 10-99
# pokemon_number = 10
# while(pokemon_number<=99):
#     downloadurl = f"https://www.serebii.net/pokemon/art/0{pokemon_number}.png"
#     req = requests.get(downloadurl)
#     filename = f"img/0{pokemon_number}.png"
#     with open(filename, "wb") as f:
#         for chunk in req.iter_content(chunk_size=8192):
#             if chunk:
#                 f.write(chunk)
#     pokemon_number += 1

# For Pokemon 100-1025
pokemon_number = 100
while(pokemon_number<=1025):
    downloadurl = f"https://www.serebii.net/pokemon/art/{pokemon_number}.png"
    req = requests.get(downloadurl)
    filename = f"img/{pokemon_number}.png"
    with open(filename, "wb") as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    pokemon_number += 1
