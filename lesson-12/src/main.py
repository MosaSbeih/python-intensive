import os
import sys
import logging
import requests


from bs4 import BeautifulSoup
from DataProcess import CreateData, Package, PackageName, PackageVersion, PackageDate, PackageDescription


ABS_PATH = os.path.abspath("").replace("src", "")
OUTPUT_PATH = ABS_PATH + os.sep + "output"
WEBSITE_SEARCH = "https://pypi.org/search/?q="
# logging
LOG_FILE_NAME = os.path.join(ABS_PATH, "logs", "log.txt")
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(message)s"
level = os.environ.get("LOGLEVEL", DEFAULT_LOG_LEVEL)
# config
logging.basicConfig(filename=LOG_FILE_NAME, level=level, filemode='a', format=DEFAULT_LOG_FORMAT)
logger = logging.getLogger()
# Handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(level)
console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
logger.addHandler(console_handler)

try:
    os.mkdir(ABS_PATH + os.sep + "output")
except FileExistsError:
    pass


def main() -> None:
    search = WEBSITE_SEARCH + input("Search for a package: ")

    logger.info(f"Requesting data from {search}")
    response = requests.get(url=search)
    logger.info(f"Data received")

    soup = BeautifulSoup(response.text, "html.parser")

    for package_snippet in soup.select(".package-snippet")[0:9]:
        logger.info("INFO | Parsing data for package <" + package_snippet.select(".package-snippet__name")[0].text + ">")

        file_path = os.path.join(OUTPUT_PATH, package_snippet.select(".package-snippet__name")[0].text)

        try:
            os.mkdir(file_path)
        except FileExistsError:
            logger.warning("WARNING | FILE ALREADY EXISTS")
            continue

        data_list = (
            package_snippet.select(".package-snippet__name")[0].text,
            package_snippet.select(".package-snippet__version")[0].text,
            package_snippet.select(".package-snippet__created")[0].text.replace("\n", "").removeprefix("  "),
            package_snippet.select(".package-snippet__description")[0].text
        )

        data_file_path = file_path + os.sep + data_list[0]

        package_info = Package(PackageName=PackageName(data_list[0]), PackageVersion=PackageVersion(data_list[1]),
                               PackageDate=PackageDate(data_list[2]), PackageDescription=PackageDescription(data_list[3]))

        CreateData.create("json", data_file_path, logger, package_info)
        CreateData.create("csv", data_file_path, logger, package_info)
        CreateData.create("xml", data_file_path, logger, package_info)

        logger.info("")


if __name__ == "__main__":
    main()
