import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO)

def get_incoming(number_value):
    tree = ET.parse("groups.xml")
    root = tree.getroot()

    for group in root.findall("group"):
        num = group.find("number")
        if num is not None and num.text == str(number_value):
            incoming = group.find("timingExbytes").find("incoming")
            return incoming.text

    return None

result = get_incoming(0)

logging.info(f"Incoming: {result}")