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

# Search for a data box
results = client.search_data_box("Company Name")

# Send a message
client.create_message(
    recipient_id="recipient_data_box_id",
    subject="Test message",
    content="Hello from ISDS client!"
)

# Get message info
message_info = client.get_message_info("message_id")
```

## Features

- Basic authentication
- Message operations (create, get info)
- Data box search
- Support for both test and production environments
- Automatic handling of SOAP/WSDL operations

## Requirements

- Python 3.7+
- zeep>=4.2.1
- requests>=2.31.0
- python-dateutil>=2.8.2

## Note

This client requires valid ISDS credentials. For production use, you'll need to obtain credentials from the Czech Data Box Information System. 