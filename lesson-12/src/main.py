import os
import sys
import logging
import requests


from bs4 import BeautifulSoup
from package import Package
from DataProcess import PackageConverter, JSONConverter, CSVConverter, XMLConverter


ABS_PATH = os.path.abspath("").replace("src", "")
OUTPUT_PATH = ABS_PATH + os.sep + "output"
WEBSITE_SEARCH = "https://pypi.org/search/?q="
# logging
LOG_FILE_NAME = os.path.join(ABS_PATH, "logs", "log.txt")
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(levelname)s | %(message)s"
level = os.environ.get("LOGLEVEL", DEFAULT_LOG_LEVEL)
# config
logging.basicConfig(filename=LOG_FILE_NAME, level=level, filemode='a', format=DEFAULT_LOG_FORMAT)
logger = logging.getLogger()
# Handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(level)
console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
logger.addHandler(console_handler)


def get_response(url):
    response = None

    try:
        logger.info(f"Requesting data from {url}")
        response = requests.get(url=url)
        logger.info("Data received")
    except requests.exceptions.ConnectionError:
        logger.error("Connection Error. Data was not received")
    finally:
        return response


def main() -> None:
    search = WEBSITE_SEARCH + input("Search for a package: ")

    response = get_response(search)
    if response is None:
        logger.warning("Exiting...")
        sys.exit(0)

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        os.mkdir(OUTPUT_PATH)
    except FileExistsError:
        pass

    for package_snippet in soup.select(".package-snippet")[0:9]:
        select = package_snippet.select

        package_name = select(".package-snippet__name")[0].text
        package_version = select(".package-snippet__version")[0].text
        package_date = select(".package-snippet__created")[0].text.replace("\n", "").removeprefix("  ")
        package_description = select(".package-snippet__description")[0].text

        file_path = os.path.join(OUTPUT_PATH, package_name)
        output_file_path = os.path.join(file_path, package_name)

        try:
            os.mkdir(file_path)
        except FileExistsError:
            logger.warning("FILE ALREADY EXISTS")
            continue

        logger.info("Parsing data for package <" + package_name + ">")

        package_info = Package(name=package_name,
                               version=package_version,
                               date=package_date,
                               description=package_description)

        PackageConverter.convert(JSONConverter, output_file_path, logger, package_info)
        PackageConverter.convert(CSVConverter, output_file_path, logger, package_info)
        PackageConverter.convert(XMLConverter, output_file_path, logger, package_info)


if __name__ == "__main__":
    main()
