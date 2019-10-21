from datetime import datetime

from modules.schedule.classes import User, Group
from modules.electives_schedule.classes import ElectivesLesson
from modules.core.source import db_read, db_write


@db_read
def get_all_lesson(session):
    """
    Function return lessons for user on exact weekday sorted by start time

    :param session: sqlalchemy session from decorator
    :param user_id:  int
    :param day:  int [0-6]
    :return: [Lesson]
    """
    lessons = session.query(ElectivesLesson).all()
    return lessons