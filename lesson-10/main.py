import asyncio
import os
import random
import time
import urllib.request


from aiohttp import ClientSession


POKEMON_DIR = os.path.join("assets", "pokemons")
SERVER_URL = "http://localhost:5001/"


def random_pokemon(directory: str) -> str:

    return random.choice(os.listdir(directory))


async def download_image(img_url: str, directory) -> None:

    # some images urls are not strings
    if isinstance(img_url, str):
        urllib.request.urlretrieve(img_url, directory)


async def get_pokemon_json(session: ClientSession, url: str) -> dict:

    async with session.get(url) as response:

        pokemon = await response.json()

        return pokemon


async def main(num: int) -> None:

    async with ClientSession() as session:

        pokemons = []

        for i in range(num):
            pokemons.append(asyncio.ensure_future(get_pokemon_json(session, SERVER_URL + random_pokemon(POKEMON_DIR))))

        pokemons = await asyncio.gather(*pokemons)

        tasks = []

        for pokemon in pokemons:
            pokemon_image_dir = os.path.join("pokemon_images", pokemon["name"])
            os.mkdir(pokemon_image_dir)
            for key in pokemon["sprites"].keys():
                tasks.append(asyncio.ensure_future(
                    download_image(pokemon["sprites"][key], os.path.join(pokemon_image_dir, f"{key}.jpg"))))

        await asyncio.gather(*tasks)


if __name__ == "__main__":

    begin_time = time.perf_counter()

    asyncio.run(main(5))

    end_time = time.perf_counter()

    print("Time taken: ", end_time - begin_time)
