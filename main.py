from isds_client import ISDSClient
import os
from dotenv import load_dotenv

from schemas.search import OwnerInfo


load_dotenv()


def main():
    client = ISDSClient(
        username=os.getenv("DATA_BOX_NAME") or "",
        password=os.getenv("DATA_BOX_PASSWORD") or "",
    )

    # print(client.verify_message("11678994"))

    result = client.find_data_box2(owner_info=OwnerInfo(db_id="8ppkmuz"))
    print(result.results.list[0].db_owner_info.db_id)


if __name__ == "__main__":
    main()
