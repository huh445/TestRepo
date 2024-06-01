import xml.etree.ElementTree as ET

class XMLExport:
    def __init__(self):
        contacts = [{"name": "John Doe", "email": "johndoe@example.com"}, {"name": "Jane Smith", "email": "janesmith@example.com"}]
        self.root = ET.Element("contacts")
        for contact in contacts:
            contact_element = ET.SubElement(self.root, "contact")
            name_element = ET.SubElement(contact_element, "name")
            email_element = ET.SubElement(contact_element, "email")
            name_element.text = contact["name"]
            email_element.text = contact["email"]
        tree = ET.ElementTree(self.root)
        tree.write("xmlpractice/data.xml", encoding=("utf-8"), xml_declaration=True)

if __name__ == "__main__":
    john = XMLExport()