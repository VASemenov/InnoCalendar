from datetime import datetime

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean, DateTime

from modules.core.source import Base


# class ElectivesUser(Base):
#     __tablename__ = "electives_users"
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(String)
#     subject = Column(String, ForeignKey('electives_lessons.subject'))
#
#     def __init__(self, user_id, subject):
#         self.user_id = user_id
#         self.subject = subject
#
#     def __repr__(self):
#         return f"ElectivesUser({self.user_id}, {self.subject})"

class ElectivesUser(Base):
    __tablename__ = 'electives_users'

    # TODO: it should be primary key
    id = Column(Integer)
    user_id = Column(Integer, primary_key=True)
    # TODO: remove primary key
    subject = Column(String)

    def __init__(self, user_id, subject):
        self.subject = subject
        self.user_id = user_id

    def __repr__(self):
        return f"ElectivesUser({self.id},{self.subject}, {self.user_id})"


class ElectivesLesson(Base):
    __tablename__ = 'electives_lessons'

    subject = Column(String, primary_key=True)
    info = relationship("ElectivesInfo", backref=backref("electives_lessons_info"))
    # user = relationship("ElectivesUser", backref=backref("electives_users"))

    def __init__(self, subject):
        self.subject = subject

    def __repr__(self):
        return f"ElectivesLesson({self.subject})"


class ElectivesInfo(Base):
    __tablename__ = "electives_lesson_info"

    id = Column(Integer, primary_key=True)
    subject = Column(String, ForeignKey('electives_lessons.subject'))
    teacher = Column(String)
    day = Column(DateTime)
    start = Column(String)
    end = Column(String)
    room = Column(Integer)

    def __init__(self, subject, teacher, day, start, end, room):
        self.subject = subject
        self.teacher = teacher
        self.day = day
        self.start = start
        self.end = end
        self.room = room

    def __repr__(self):
        return f"ElectivesInfo({self.subject}, {self.day})"

    def __str__(self):
        """
        Converts current lesson to string for easy output

        :return: String
        """
        return f"{self.subject}\n"\
               f"👨‍🏫 {self.teacher}\n"\
               f"🕐 {self.start} 	— {self.end}\n" \
               f"🚪 {self.room if self.room != -1 else '?'}\n"