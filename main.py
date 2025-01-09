from pprint import pprint
from isds_client import ISDSClient
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    client = ISDSClient(
        username=os.getenv("DATA_BOX_NAME") or "",
        password=os.getenv("DATA_BOX_PASSWORD") or "",
    )

    # print(client.message_info.verify_message("11678994"))
    # print(client.data_box_access.get_password_info())
    print(client.message_info.get_received_messages())


if __name__ == "__main__":
    main()
