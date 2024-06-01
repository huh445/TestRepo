import xml.etree.ElementTree as ET
from lessons.rooms import Rooms

class Lessons:
    def __init__(self):
        self.xml = ET.parse("timetable.xml")
        self.xml_root = self.xml.getroot()
        self.lessons = self.xml_root.findall("lesson")
        self.root = self.xml_root
        self.rooms = Rooms()

    def search(self, date, id):
        cols = []
        rows = []
        for lessons in self.lessons:
            date_element = lessons.find("date").text
            id_element = lessons.find("teacherid").text
            if str(date_element) == str(date) and str(id) == str(id_element):
                student = lessons.find("student").text
                time = lessons.find("time").text
                instrument = lessons.find("instrument").text
                room = lessons.find("roomid").text
                lessons_missed = lessons.find("lessons_missed").text
                has_paid = lessons.find("has_paid").text
                
                room = self.rooms.rooms(room)
                cols.append(date_element)
                rows.append([time, lessons_missed, student, instrument, room, has_paid])
        return rows, cols
    
    def add_lessons(self, lesson_data):
        lesson = ET.SubElement(self.root, "lesson")
        for key, value in lesson_data.items():
            sub_element = ET.SubElement(lesson, key)
            sub_element.text = str(value)
        self.xml.write("timetable.xml", encoding="utf-8", xml_declaration=True)