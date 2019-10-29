from datetime import datetime

from modules.electives_schedule.classes import ElectivesUser, ElectivesLesson, ElectivesInfo
from modules.core.source import db_read, db_write


@db_read
def get_electives_course(session):
    lessons = session.query(ElectivesLesson).all()
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
