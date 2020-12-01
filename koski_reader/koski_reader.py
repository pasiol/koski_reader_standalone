import os
import sys
import json
import csv
import click
import logging
import requests
from requests.auth import HTTPBasicAuth


def create_json_file(data, output_path, oid, logger):
    try:
        with open(
            f"{output_path}{os.path.sep}{oid}.json", "w", encoding="utf-8"
        ) as output_file:
            json.dump(data, output_file, sort_keys=True, indent=4)
    except Exception as error:
        logger.error(f"Creating json file {oid}.json failed: {error}")
        sys.exit(1)


def pseudonymise(response, logger):
    data = None
    try:
        data = dict(response.json())
    except Exception as error:
        logger.info(f"Casting response to JSON failed: {error}")
        sys.exit(1)

    if "henkilö" in data.keys():
        try:
            data["oid"] = data["henkilö"]["oid"]
            data.pop("henkilö", None)
            return data
        except Exception as error:
            logger.info(f"Anonymizing failed: {error}")
            sys.exit(1)
    return data


@click.command()
@click.argument("username", type=click.STRING)
@click.argument("password", type=click.STRING)
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path(exists=True))
def main(username, password, input_file, output_path):

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    collection = None
    endpoint = f"https://virkailija.opintopolku.fi/koski/api/opiskeluoikeus"


    logger.info(f"The Koski reader started. Trying to fetch data from url: {endpoint}")

    urls = None
    try:
        with open(input_file, "r", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=["parameter"], delimiter=";")
            urls = [f"{endpoint}/{str(row['parameter'])}" for row in reader]
        logger.info(f"Getting {len(urls)} parameters to do.")
    except Exception as error:
        logger.error(f"Reading input file failed: {input_file} {error}")
        sys.exit(1)
    for url in urls:
        oid = url.split("/")[-1]
        logger.info(f"Processing id: {oid}")
        try:
            response = requests.get(
                url, auth=HTTPBasicAuth(str(username), str(password))
            )
            if response.status_code == 200:
                data = pseudonymise(response, logger)
                data["_id"] = oid
                create_json_file(data, output_path, oid, logger)
            else:
                logger.error(f"Get request failed: {response.status_code} {url}")
        except Exception as error:
            logger.error(f"Get request failed: {url} {error}")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter