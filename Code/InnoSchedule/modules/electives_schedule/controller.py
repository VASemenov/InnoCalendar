from datetime import datetime

from modules.electives_schedule.classes import ElectivesUser, ElectivesLesson, ElectivesInfo
from modules.core.source import db_read, db_write
from modules.schedule.classes import Lesson


@db_read
def get_electives_course(session):
    lessons = session.query(ElectivesLesson).all()
    return lessons


@db_read
def get_today_electives_courses(session, user_id):
    lessons = []
    courses = session.query(ElectivesUser.subject).filter_by(user_id=user_id).all()
    day = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    today_electives = session.query(ElectivesInfo.subject, ElectivesInfo.day, ElectivesInfo.room,
                                    ElectivesInfo.teacher,
                                    ElectivesInfo.start, ElectivesInfo.end).all()
    today_electives = [elec for elec in today_electives if elec.day == day]
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
