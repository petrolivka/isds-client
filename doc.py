from pathlib import Path
from zeep import Client

import json

wsdl_dir = "wsdl"


def parse_element(elements):
    all_elements = {}
    for name, element in elements:
        all_elements[name] = {}
        all_elements[name]["optional"] = element.is_optional
        if hasattr(element.type, "elements"):
            all_elements[name]["type"] = parse_element(element.type.elements)
        else:
            all_elements[name]["type"] = str(element.type)

    return all_elements


def parse_file(file_path):
    client = Client(file_path)
    interface = {}
    for service in client.wsdl.services.values():
        interface[service.name] = {}
        for port in service.ports.values():
            interface[service.name][port.name] = {}
            operations = {}
            for operation in port.binding._operations.values():
                operations[operation.name] = {}
                operations[operation.name]["input"] = {}

                # Check if input body has complex type with elements
                if hasattr(operation.input.body.type, "elements"):
                    elements = operation.input.body.type.elements
                    operations[operation.name]["input"] = parse_element(elements)
                else:
                    # Handle simple types
                    operations[operation.name]["input"] = str(operation.input.body.type)

            interface[service.name][port.name]["operations"] = operations

    return interface


def parse_all_files(wsdl_dir):
    out_dir = Path("doc")
    out_dir.mkdir(parents=True, exist_ok=True)
    for file in Path(wsdl_dir).glob("*.wsdl"):
        json_str = json.dumps(parse_file(str(file)), indent=4)
        with open(out_dir / f"{file.stem}.json", "w") as f:
            f.write(json_str)


parse_all_files(wsdl_dir)
