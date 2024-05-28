import xml.etree.ElementTree as ET

class Analyse:
    def __init__(self):
        self.xml = ET.parse("timetable.xml")
        xml_root = self.xml.getroot()
        self.lessons = xml_root.findall("lesson")
    def get_lessons(self, id):
        row = []
        col = []
        for lesson in self.lessons:
            id_element = lesson.find("teacherid").text
            if int(id) == int(id_element):
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
        return row, col
    
    def add_lesson(self, name, date, time, instrument, combination, id):
        # Access the root element from the parsed XML
        xml_root = self.xml.getroot()

        # Find the <music_lessons> element (assuming it exists)

        # Create the new lesson element
        new_lesson = ET.Element("lesson")

        # Add child elements to the new lesson element
        ET.SubElement(new_lesson, "date").text = date
        ET.SubElement(new_lesson, "student").text = name
        ET.SubElement(new_lesson, "teacherid").text = id
        ET.SubElement(new_lesson, "time").text = time
        ET.SubElement(new_lesson, "instrument").text = instrument
        ET.SubElement(new_lesson, "has_paid").text = combination

        xml_root.append(new_lesson)

        # Write the entire updated XML tree back to the file
        self.xml.write("timetable.xml", encoding="utf-8", xml_declaration=True)