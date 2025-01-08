> ⚠️ **Warning**: This library is currently in early development and should be considered unstable. The API may change without notice, and not all features are fully implemented or tested. Use at your own risk in production environments.


# ISDS Python Client

A Python client for interacting with the Czech Data Box Information System (ISDS).

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from isds_client import ISDSClient

# Initialize client (test environment)
client = ISDSClient(
    username="your_username",
    password="your_password",
    production=False  # Use True for production environment
)

# Send a message
client.create_message(
    recipient_id="recipient_data_box_id",
    subject="Test message",
    content="Hello from ISDS client!"
)

# Get list of received messages
messages = client.get_received_messages()

# Search for a data box
results = client.find_data_box("Company Name")
```

## Features

### Message Operations
- Create and send messages (`create_message`)
- Download messages (`download_message`, `download_signed_message`)
- Verify message authenticity (`authenticate_message`)

### Message Information
- Get message state changes (`get_message_info`)
- Get delivery information (`get_delivery_info`)
- List messages (`get_sent_messages`, `get_received_messages`)
- Mark messages as read (`mark_message_as_downloaded`)
- Get message envelopes (`get_message_envelope`)
- Get signed delivery info (`get_signed_delivery_info`)

### Data Box Search
- Find data boxes (`find_data_box`)
- Check data box status (`check_data_box`)
- Get data box lists (`get_data_box_list`)
- Get activity status (`get_data_box_activity_status`)
- Get PDZ info (`get_pdz_info`)
- Get credit info (`get_credit_info`)

### Data Box Access
- Get owner information (`get_owner_info`)
- Get user information (`get_user_info`)
- Password management (`change_password`, `get_password_info`)

### Data Box Manipulations
- Create data boxes (`create_data_box`)
- Delete data boxes (`delete_data_box`)
- Update data box descriptions (`update_data_box_description`)
- Manage users (`add_data_box_user`, `delete_data_box_user`, `update_data_box_user`)
- Generate access data (`new_access_data`)
- Enable/disable data boxes (`enable_own_data_box`, `disable_own_data_box`)
- Manage open addressing (`set_open_addressing`, `clear_open_addressing`)
- Get user lists (`get_data_box_users`)

## Requirements

- Python 3.7+
- zeep>=4.2.1 (SOAP client)
- requests>=2.31.0
- python-dateutil>=2.8.2

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
- Data Box Manipulations (db_manipulations.wsdl)

## Error Handling

All operations are wrapped with proper error handling and will raise `ISDSError` with descriptive messages in case of failures. 