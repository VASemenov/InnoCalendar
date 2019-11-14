import datetime
from sqlalchemy import func

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


@db_read
def get_day_elective_lessons(session, user_id, day):
    """
    Function return elective lessons for user on exact weekday sorted by start time
    :param session: sqlalchemy session from decorator
    :param user_id:  int
    :param day:  int [0-6]
    :return: [Lesson]
    """
    monday = datetime.date.today() - datetime.timedelta(days=day-1)
    this_week_dates = [monday]
    for i in range(1, 7):
        this_week_dates.append(monday + datetime.timedelta(i))
    all_user_electives = list(i[0] for i in session.query(ElectivesUser).filter_by(user_id=user_id).values('subject'))
    today_lessons = set(session.query(ElectivesInfo).filter(ElectivesInfo.subject.in_(all_user_electives), func.DATE(ElectivesInfo.day).in_(this_week_dates)).values('subject', 'day'))

    return sorted([i[0] for i in today_lessons])
