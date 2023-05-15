import logging
import os
import sys
import tempfile
from zipfile import ZipFile

import requests
from flask.cli import AppGroup

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


data_cli = AppGroup("data")


@data_cli.command("load")
def load_data():
    spec_zip_url = (
        "https://github.com/digital-land/specification/archive/refs/heads/main.zip"
    )

    with tempfile.TemporaryDirectory() as tmp_dir:
        logger.info(f"Created temp directory {tmp_dir}")

        resp = requests.get(spec_zip_url)
        zip_file_path = os.path.join(tmp_dir, "main.zip")

        with open(zip_file_path, "wb") as f:
            f.write(resp.content)

        with ZipFile(zip_file_path) as config_zip:
            config_zip.extractall(path=tmp_dir)
            # TODO - process the files
