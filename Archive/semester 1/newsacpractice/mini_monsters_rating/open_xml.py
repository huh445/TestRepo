import xml.etree.ElementTree as ET

class OpenXML:
    def __init__(self):
        self.xml = ET.parse("newsacpractice/mini_monsters_rating/monsters.xml")
        xml_root = self.xml.getroot()
        self.root = xml_root
        self.monsters = xml_root.findall("monster")
    def get_monsters(self):
        row = []
        col = []
        for monster in self.monsters:
            rank = monster.find("rank").text
            name = monster.find("name").text
            type = monster.find("type").text
            weight = monster.find("weight").text
            colour = monster.find("colour").text
            col.append(rank)
            row.append([name, type, weight, colour])
        return row, col
    def add_monsters(self, data):
        monster = ET.SubElement(self.root, "monster")
        for key, value in data.items():
            sub_element = ET.SubElement(monster, key)
            sub_element.text = str(value)
            try:
                self.xml.write(self.xml_file_path, encoding="utf-8", xml_declaration=True)
            except ET.ParseError:
                # Handle XML writing error
                print("Error: Failed to write to XML file.")
    def highest_rank(self):
        highest_id = 0
        for monster in self.monsters:
            rank = int(monster.find("rank").text)
            if rank > highest_id:
                highest_id = rank
        highest_id += 1
        return highest_id