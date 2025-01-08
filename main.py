from isds_client import ISDSClient
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    client = ISDSClient(
        username=os.getenv("DATA_BOX_NAME") or "",
        password=os.getenv("DATA_BOX_PASSWORD") or "",
    )
    print(client.get_message_info("11678994"))


if __name__ == "__main__":
    main()
