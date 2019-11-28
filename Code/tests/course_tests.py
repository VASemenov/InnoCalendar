import datetime
from unittest.mock import MagicMock, patch, Mock
from nose.tools import assert_equal
from parameterized import parameterized

import unittest

from telebot.types import Message, User, Chat

from modules.core.source import attach_core_module
from modules.electives_schedule import permanent
from modules.electives_schedule.source import attach_electives_schedule_module

(add_course_handler, process_electives) = attach_electives_schedule_module()



messages = []


def send_message(chat_id, message, reply_markup=None):
    messages.append(message)



class TestCourseAttachment(unittest.TestCase):
    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])
    def test_add_course(self, message, value):
        message.text = "/add_course"
        with patch('modules.core.source.bot.register_next_step_handler'):
            with patch('modules.core.source.bot.send_message', side_effect=send_message):
                with patch('modules.electives_schedule.controller.get_electives_course'):
                    add_course_handler(message)
        assert_equal(messages.pop(), str("What course you want to add?"))



    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])
    def test_wrong_add_course(self, message, value):
        message.text = "/some_staff"
        with patch('modules.core.source.bot.register_next_step_handler'):
            with patch('modules.core.source.bot.send_message', side_effect=send_message):
                with patch('modules.electives_schedule.controller.get_electives_course'):
                    add_course_handler(message)
        assert_equal(len(messages), 0)


    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])

    def test_course_set(self, message, value):
        message.text = "B19"
        with patch('modules.electives_schedule.controller.check_electives_course', return_value=True):
            with patch('modules.core.source.bot.send_message' , side_effect=send_message):
                with patch('modules.electives_schedule.controller.set_electives_user'):
                    process_electives(message)
        assert_equal(messages.pop(),  permanent.MESSAGE_SUCCESS)



    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])
    def test_wrong_course_set(self, message, value):
        message.text = "BBBSBS"
        with patch('modules.electives_schedule.controller.check_electives_course', return_value=False):
            with patch('modules.core.source.bot.send_message' , side_effect=send_message):
                with patch('modules.electives_schedule.controller.set_electives_user'):
                    process_electives(message)
        assert_equal(messages.pop(),  permanent.MESSAGE_UNKNOWN_LESSON)

