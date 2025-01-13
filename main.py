from isds_client import ISDSClient
import os
from dotenv import load_dotenv

from schemas.base import DmFile


load_dotenv()


def main():
    client = ISDSClient(
        username=os.getenv("DATA_BOX_NAME") or "",
        password=os.getenv("DATA_BOX_PASSWORD") or "",
    )

    # result = client.get_owner_info()
    # print(result)

    # result = client.verify_message("11678994")
    # print(result)

    # result = client.get_message_info("11678994")
    # print(result)

    # result = client.download_message("11678994")
    # print(result)

    result = client.create_message(
        recipient_id="8ppkmuz",
        subject="Nejaka testovaci sprava png + pdf",
        files=[
            DmFile(file_path="test/test.png"),
            DmFile(file_path="test/test3.pdf"),
        ],
    )
    print(result)


if __name__ == "__main__":
    main()
