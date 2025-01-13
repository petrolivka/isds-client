from datetime import datetime, timedelta
import logging
from isds_client import ISDSClient
import os
from dotenv import load_dotenv

from schemas.base import DmFile

logging.basicConfig(
    level=logging.DEBUG,
    filename="isds.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
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

    result = client.create_message(
        recipient_id="8ppkmuz",
        subject=f"Nejaka testovaci sprava png + pdf {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        files=[
            DmFile(file_path="test/files/test.png"),
            DmFile(file_path="test/files/test2.png"),
        ],
    )
    print(result)

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

    # result = client.get_delivery_info("11678994")
    # print(result)

    # result = client.mark_message_as_downloaded("11678994")
    # print(result)

    # result = client.get_message_envelope("11678994")
    # print(result)

    # result = client.get_sent_message_envelope("11693587")
    # print(result)

    # result = client.data_box_fulltext_search(
    #    search_text="mordor",
    # )
    # print(result)

    # result = client.get_credit_info("i9wkmqk")
    # print(result)

    # result = client.get_owner_info()
    # print(result)

    # result = client.get_user_info()
    # print(result)

    # result = client.change_password("123456", "12345678")
    # print(result)

    # result = client.get_password_info()
    # print(result)


if __name__ == "__main__":
    main()
