import requests

baseUrl = "https://pokeapi.co/api/v2/"


def getPokemonInfo(name):
    url = f"{baseUrl}/pokemon/{pokemonName}"
    response = requests.get(url)
    return response.json() if response.ok else None


pokemonName = input("Enter Pokemon's name: ").lower()

pokemonInfo = getPokemonInfo(pokemonName)


if pokemonInfo:
    pokemonNname = pokemonInfo.get("name", "Unknown")
    pokemonType = pokemonInfo["types"][0]["type"]["name"]
    pokemonWeight = pokemonInfo.get("weight", "Unknown")

    print(f"Name: {pokemonNname}")
    print(f"Type: {pokemonType}")
    print(f"Weight: {pokemonWeight}")
else:
    print("Failed to fetch pokemon data")
