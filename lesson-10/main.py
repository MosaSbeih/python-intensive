import asyncio
import os
import random
import time
import urllib.request


from aiohttp import ClientSession


SERVER_URL = "http://localhost:5050/"
POKEMON_NAME_LIST = ('abra', 'aerodactyl', 'alakazam', 'arbok', 'arcanine', 'articuno', 'beedrill', 'bellsprout', 'blastoise', 'bulbasaur', 'butterfree', 'caterpie', 'chansey', 'charizard', 'charmander', 'charmeleon', 'clefable', 'clefairy', 'cloyster', 'cubone', 'dewgong', 'diglett', 'ditto', 'dodrio', 'doduo', 'dragonair', 'dragonite', 'dratini', 'drowzee', 'dugtrio', 'eevee', 'ekans', 'electabuzz', 'electrode', 'exeggcute', 'exeggutor', 'farfetchd', 'fearow', 'flareon', 'gastly', 'gengar', 'geodude', 'gloom', 'golbat', 'goldeen', 'golduck', 'golem', 'graveler', 'grimer', 'growlithe', 'gyarados', 'haunter', 'hitmonchan', 'hitmonlee', 'horsea', 'hypno', 'ivysaur', 'jigglypuff', 'jolteon', 'jynx', 'kabuto', 'kabutops', 'kadabra', 'kakuna', 'kangaskhan', 'kingler', 'koffing', 'krabby', 'lapras', 'lickitung', 'machamp', 'machoke', 'machop', 'magikarp', 'magmar', 'magnemite', 'magneton', 'mankey', 'marowak', 'meowth', 'metapod', 'mewtwo', 'moltres', 'mr-mime', 'muk', 'nidoking', 'nidoqueen', 'nidoran-f', 'nidoran-m', 'nidorina', 'nidorino', 'ninetales', 'oddish', 'omanyte', 'omastar', 'onix', 'paras', 'parasect', 'persian', 'pidgeot', 'pidgeotto', 'pidgey', 'pikachu', 'pinsir', 'poliwag', 'poliwhirl', 'poliwrath', 'ponyta', 'porygon', 'primeape', 'psyduck', 'raichu', 'rapidash', 'raticate', 'rattata', 'rhydon', 'rhyhorn', 'sandshrew', 'sandslash', 'scyther', 'seadra', 'seaking', 'seel', 'shellder', 'slowbro', 'slowpoke', 'snorlax', 'spearow', 'squirtle', 'starmie', 'staryu', 'tangela', 'tauros', 'tentacool', 'tentacruel', 'vaporeon', 'venomoth', 'venonat', 'venusaur', 'victreebel', 'vileplume', 'voltorb', 'vulpix', 'wartortle', 'weedle', 'weepinbell', 'weezing', 'wigglytuff', 'zapdos', 'zubat')


def random_pokemon() -> str:

    return random.choice(POKEMON_NAME_LIST)


def download_image(img_url: str, directory) -> None:

    urllib.request.urlretrieve(img_url, directory)


async def get_pokemon_json(session: ClientSession, url: str) -> dict:

    async with session.get(url) as response:

        pokemon = await response.json()

        return pokemon


async def main(num: int) -> None:

    def loop(json_data: dict, file_name: str, directory: str) -> None:

        for key in json_data.keys():
            if isinstance(json_data[key], str):
                download_image(json_data[key], os.path.join(directory, file_name + f"{key}.jpg"))
            elif isinstance(json_data[key], dict):
                new_file_name = file_name + f"-{key}"
                loop(json_data[key], new_file_name, directory)

    os.mkdir("pokemon_images")

    async with ClientSession() as session:

        pokemons = []

        for i in range(num):
            pokemons.append(asyncio.ensure_future(get_pokemon_json(session, SERVER_URL + random_pokemon() + ".json")))

        pokemons = await asyncio.gather(*pokemons)

        for pokemon in pokemons:
            pokemon_image_dir = os.path.join("pokemon_images", pokemon["name"])
            try:
                os.mkdir(pokemon_image_dir)
            except FileExistsError:
                pass

            loop(pokemon["sprites"], "", pokemon_image_dir)


if __name__ == "__main__":

    begin_time = time.perf_counter()

    asyncio.run(main(5))

    end_time = time.perf_counter()

    print("Time taken: ", end_time - begin_time)
