> ⚠️ **Warning**: This library is currently in early development and should be considered unstable. The API may change without notice, and not all features are fully implemented or tested. Use at your own risk in production environments.


# ISDS Python Client

A Python client for interacting with the Czech Data Box Information System (ISDS).

## Installation

1. Clone this repository
2. Install dependencies:
```bash
uv sync
```

## Usage

```python
from isds_client import ISDSClient
from schemas.base import DmFile

# Initialize client (test environment)
client = ISDSClient(
    username="your_username",
    password="your_password",
    production=False,  # Use True for production environment
    debug=True,
)

# Send a message
client.create_message(
    recipient_id="xxxxxxx",
    subject="Test message",
    files=[
        DmFile(file_path="test/test.png"),
        DmFile(file_path="test/test2.png"),
    ],
)

# Get list of received messages
messages = client.get_received_messages()

# Search for a data box
results = client.find_data_box(
    owner_info={"dbID": "yyyyyyy"},
)

# Get credit info
credit_info = client.get_credit_info("xxxxxxx")

```

## Features

### Message Operations
- Create and send messages (`create_message`)
- Download messages (`download_message`, `download_signed_message`)
- Verify message authenticity (`authenticate_message`)

### Message Information
- Get message state changes (`get_message_info`)
- Verify message authenticity (`verify_message`)
- Get delivery information (`get_delivery_info`)
- List messages (`get_sent_messages`, `get_received_messages`)
- Mark messages as read (`mark_message_as_downloaded`)
- Get message envelopes (`get_message_envelope`, `get_sent_message_envelope`)
- Get signed delivery info (`get_delivery_info`)
- Register for notifications (`register_for_notifications`)
- Get notification list (`get_notification_list`)
- Get list of erased messages (`get_list_of_erased_messages`)

### Data Box Search
- Find data boxes (`find_data_box`)
- Check data box status (`check_data_box`)
- Get data box list (`get_data_box_list`)
- Get credit info (`get_credit_info`)

### Data Box Access
- Get owner information (`get_owner_info`)
- Get user information (`get_user_info`)
- Password management (`change_password`, `get_password_info`)

## Requirements

- Python 3.12+
- pydantic>=2.10.5
- python-dateutil>=2.9.0.post0
- python-dotenv>=1.0.1
- zeep==4.3.1

## Note

This client requires valid ISDS credentials. For production use, you'll need to obtain credentials from the Czech Data Box Information System (ISDS).

## Environment Support

The client supports both test (czebox.cz) and production (mojedatovaschranka.cz) environments. Use the `production` parameter when initializing the client to switch between them:

```python
# Test environment
client = ISDSClient(username="test_user", password="test_pass", production=False)

# Production environment
client = ISDSClient(username="prod_user", password="prod_pass", production=True)
```

## Service Endpoints

The client automatically handles the following ISDS service endpoints:
- Message Operations (dm_operations.wsdl)
- Message Info (dm_info.wsdl)
- Data Box Search (db_search.wsdl)
- Data Box Access (db_access.wsdl)

## Error Handling

All operations are wrapped with proper error handling and will raise `ISDSError` with descriptive messages in case of failures. 