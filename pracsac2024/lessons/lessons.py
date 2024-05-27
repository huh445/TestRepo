import xml.etree.ElementTree as ET

class Analyse:
    def __init__(self):
        xml = ET.parse("timetable.xml")
        xml_root = xml.getroot()
        self.lessons = xml_root.findall("lesson")
        self.element = ET.Element("lesson")
        self.tree = ET.ElementTree("lesson")
    def get_lessons(self, id):
        row = []
        col = []
        for lesson in self.lessons:
            id_element = lesson.find("teacherid").text
            if id == id_element:
                date = lesson.find("date").text
                student = lesson.find("student").text
                time = lesson.find("time").text
                instrument = lesson.find("instrument").text
                col.append(date)
                row.append([time, student, instrument])
        return row, col
    
    def search(self, dates):
        row = []
        col = []
        for lesson in self.lessons:
            date_element = lesson.find("date").text
            if dates == date_element:
                date = lesson.find("date").text
                student = lesson.find("student").text
                time = lesson.find("time").text
                instrument = lesson.find("instrument").text
                col.append(date)
                row.append([time, student, instrument])
        print(col, row)
        return row, col
    
    def add_lesson(self, name, date, time, instrument, combination):
        ET.SubElement(self.element, "student").text = name
        ET.SubElement(self.element, "date").text = date
        ET.SubElement(self.element, "time").text = time
        ET.SubElement(self.element, "instrument").text = instrument
        # ET.SubElement(lesson, "room").text = room
        ET.SubElement(self.element, "has_paid").text = combination
        with open("timetable.xml", "ab") as f:
            f.write(ET.tostring(self.element, encoding="utf-8", xml_declaration=True))