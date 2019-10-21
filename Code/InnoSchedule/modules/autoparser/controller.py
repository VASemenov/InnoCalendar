from modules.schedule.classes import Lesson
from modules.core import source as core
from modules.electives_schedule.classes import ElectivesLesson, ElectivesInfo


@core.db_write
def delete_all_lessons(session):
    """
    Delete all lessons from table to parse new ones

    :param session: sqlalchemy session from decorator
    """
    session.query(Lesson).delete()


@core.db_write
def insert_lesson(session, group, subject, teacher, day, start, end, room):
    """
    Insert new lesson with given parameters

    :param session: sqlalchemy session from decorator
    :param group: string
    :param subject: string
    :param teacher: string
    :param day: integer
    :param start: string
    :param end: string
    :param room: string
    """
    session.add(Lesson(group, subject, teacher, day, start, end, room))

@core.db_write
def delete_all_electives_lessons(session):
    session.query(ElectivesLesson).delete()
    print("delete_all_electives_lessons")


@core.db_write
def insert_electives_lesson(session, subject):
    session.add(ElectivesLesson(subject))
    print("insert_electives_lesson")

@core.db_write
def delete_all_electives_lesson_info(session):
    session.query(ElectivesInfo).delete()
    print("delete_all_electives_lesson_info")

@core.db_write
def insert_electives_lesson_info(session, subject, teacher, day, start, end, room):
    session.add(ElectivesInfo(subject, teacher, day, start, end, room))
    print("insert_electives_lesson_info")