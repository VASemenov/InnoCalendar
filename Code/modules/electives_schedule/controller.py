import datetime
from datetime import datetime as dt

from modules.electives_schedule.classes import ElectivesUser, ElectivesLesson, ElectivesInfo
from modules.core.source import db_read, db_write
from modules.schedule.classes import Lesson


@db_read
def get_electives_course(session):
    lessons = session.query(ElectivesLesson).all()
    return lessons



@db_read
def get_day_elective_lessons(session, user_id, day):
    today = dt.today()
    today = today.replace(hour=0, second=0, microsecond=0, minute=0)
    if day > today.weekday():
        today = today + datetime.timedelta(days=day - today.weekday())
    elif day < today.weekday():
        today = today + datetime.timedelta(days=day - today.weekday() + 7)

    lessons = []
    courses = session.query(ElectivesUser.subject).filter_by(user_id=user_id).all()
    today_electives = session.query(ElectivesInfo.subject, ElectivesInfo.day, ElectivesInfo.room,
                                    ElectivesInfo.teacher,
                                    ElectivesInfo.start, ElectivesInfo.end).all()
    today_electives = [elec for elec in today_electives if elec.day == today]
    for i in today_electives:
        for j in courses:
            if i.subject == j.subject:
                lessons.append(i)
    lessons = [Lesson("Elective",lesson.subject, lesson.teacher, lesson.day, lesson.start, lesson.end, lesson.room) for
               lesson in lessons]
    return lessons



@db_read
def check_electives_course(session, subject):
    lesson = session.query(ElectivesLesson).filter_by(subject=subject).first()
    if not lesson:
        return False
    else:
        return True


@db_write
def set_electives_user(session, user_id, subject):
    session.add(ElectivesUser(user_id, subject))


@db_read
def get_user(session, user_id):
    return session.query(ElectivesUser).filter_by(id=user_id).first()
