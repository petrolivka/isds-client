from datetime import datetime, timedelta
import logging
from isds_client import ISDSClient
import os
from dotenv import load_dotenv

from schemas.base import DmFile

logging.basicConfig(
    level=logging.INFO,
)

load_dotenv()


def main():
    client = ISDSClient(
        username=os.getenv("DATA_BOX_NAME") or "",
        password=os.getenv("DATA_BOX_PASSWORD") or "",
        debug=False,
    )

    # result = client.find_data_box(
    #     owner_info={"dbID": "8ppkmuz"},
    # )
    # print(result)

    # result = client.create_message(
    #     recipient_id="8ppkmuz",
    #     subject="Nejaka testovaci sprava png + pdf",
    #     files=[
    #         DmFile(file_path="test/test.png"),
    #         DmFile(file_path="test/test2.png"),
    #     ],
    # )
    # print(result)

    # result = client.download_message("11678994")
    # print(result)

    # result = client.get_owner_info()
    # print(result)

    # result = client.verify_message("11678994")
    # print(result)

    # result = client.get_message_info(
    #     from_time=datetime.now() - timedelta(days=1),
    #     to_time=datetime.now(),
    # )
    # print(result)


if __name__ == "__main__":
    main()
