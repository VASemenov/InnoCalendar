from datetime import datetime

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean

from modules.core.source import Base


class Electives(Base):
    __tablename__ = "electives_schedule_users"

    id = Column(Integer, primary_key=True)
    schedule_user = Column(Integer, ForeignKey('schedule_users.id'))
    schedule_lessons = Column(Integer, ForeignKey('schedule_lessons.id'))
    

    def __init__(self, id_, schedule_user_):
        self.id = id_
        self.schedule_user_ = schedule_user_


    def __repr__(self):
        return f"ElectiveScheduleUser({self.id})"

    def __str__(self):
        """
        Converts current lesson to string for easy output

        :return: String
        """
        return  f"/electives_{self.id} - "\
                f"{self.subject} - "\
                f"👨‍🏫 {self.teacher}\n"\


class ElectivesLesson(Base):
    __tablename__ = "electives_lesson"

    id = Column(Integer, primary_key=True)
    schedule_lesson = Column(Integer, ForeignKey('schedule_lessons.id'))
    dates = relationship("ElectivesDate", backref=backref("electives_date"))
    subject = Column(String)
    teacher = Column(String)
    day = Column(Integer)
    start = Column(String)
    end = Column(String)
    room = Column(Integer)

    def __init__(self, electives_schedule_user, subject, teacher, day, start, end, room):
        self.electives_schedule_user = electives_schedule_user
        self.subject = subject
        self.teacher = teacher
        self.day = day
        self.start = start
        self.end = end
        self.room = room

    def __repr__(self):
        return f"ElectiveLesson({self.subject}, {self.start})"

    @property
    def start_struct(self):
        """
        Converts start time from string to time object
        :return: datetime
        """
        return datetime.now().replace(hour=int(self.start[:2]), minute=int(self.start[3:]))

    @property
    def end_struct(self):
        """
        Converts end time from string to time object
        :return: datetime
        """
        return datetime.now().replace(hour=int(self.end[:2]), minute=int(self.end[3:]))

    @property
    def minutes_until_start(self):
        """
        Total number of minutes until lesson begins

        :return: int
        """

        seconds_left = (self.start_struct - datetime.now()).total_seconds()
        return round(seconds_left / 60)

    @property
    def minutes_until_end(self):
        """
        Total number of minutes until lesson ends

        :return: int
        """
        seconds_left = (self.end_struct - datetime.now()).total_seconds()
        return round(seconds_left / 60)

    def __lt__(self, other):
        """
        Compares this lesson with given. Used in lesson sort

        :param other: Lesson
        :return: boolean
        """
        return self.start_struct < other.start_struct

    def __str__(self):
        """
        Converts current lesson to string for easy output

        :return: String
        """
        return  f"/electives_{self.id} - "\
                f"{self.subject} - "\
                f"👨‍🏫 {self.teacher}\n"\

    def get_detail(self):
        return f"{self.subject}\n" \
               f"👨‍🏫 {self.teacher}\n" \
               f"🕐 {self.start} 	— {self.end}\n" \
               f"🚪 {self.room if self.room != -1 else '?'}\n"


    def get_str_current(self):
        """
        Returns string, which indicates how many time left until current lesson will be finished.
        Used when NOW button is pressed and current lesson is going

        :return: String
        """
        hours_until_end = self.minutes_until_end // 60
        return f"{self}⏸️ {str(hours_until_end)+'h ' if hours_until_end > 0 else ''}" \
               f"{self.minutes_until_end % 60}m\n"

    def get_str_future(self):
        """
        Returns string, which indicates how many time left until current lesson will be started.
        Used when NOW button is pressed and current lesson will start next

        :return: String
        """
        hours_until_start = self.minutes_until_start // 60
        return f"{self}▶ ️{str(hours_until_start)+'h ' if hours_until_start > 0 else ''}" \
               f"{self.minutes_until_start % 60}m\n"


class ElectivesDate(Base):
    __tablename__ = "electives_date"

    id = Column(Integer, primary_key=True)
    electives_lesson = Column(Integer, ForeignKey('electives_lesson.id'))
    date = Column(String)
    start = Column(String)
    end = Column(String)
    room = Column(Integer)

    def __init__(self, id, electives_lesson, date, start, end, room):
        self.id = id
        self.electives_lesson = electives_lesson
        self.date = date
        self.start = start
        self.end = end
        self.room = room


    def __repr__(self):
        return f"ElectiveDate({self.id})"