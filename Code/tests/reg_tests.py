import datetime
from unittest.mock import MagicMock, patch, Mock
from nose.tools import assert_equal
from parameterized import parameterized

import unittest

from telebot.types import Message, User, Chat

from modules.core.source import attach_core_module
from modules.schedule import permanent
from modules.schedule.source import attach_schedule_module

(schedule_command_handler, process_course_step, process_group_step) = attach_schedule_module()

messages = []


def send_message(chat_id, message, reply_markup=None):
    messages.append(message)


class TestUserRegistration(unittest.TestCase):
    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])
    def test_registration(self, message, value):
        message.text = "/configure_schedule"
        get_user = Mock(return_value=["Hi"])

        with patch('modules.schedule.controller.get_user', new=get_user):
            with patch('modules.schedule.controller.set_user_configured'):
                with patch('modules.core.source.bot.send_message',side_effect=send_message):
                    with patch('modules.core.source.bot.register_next_step_handler'):
                        schedule_command_handler(message)
        assert_equal(messages.pop(), permanent.REQUEST_COURSE)
        messages.clear()

    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])
    def test_course_set(self, message, value):
        message.text = "B19"
        with patch('modules.schedule.controller.append_user_group'):
            with patch('modules.core.source.bot.send_message', side_effect = send_message):
                with patch('modules.core.source.bot.register_next_step_handler'):
                    process_course_step(message)
        assert_equal(messages.pop(), permanent.REQUEST_GROUP)

    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])
    def test_group_set(self, message, value):
        message.text = "B16-SE-01"
        with patch('modules.schedule.controller.append_user_group'):
            with patch('modules.core.source.bot.send_message', side_effect = send_message):
                with patch('modules.core.source.bot.register_next_step_handler'):
                    with patch('modules.schedule.controller.set_user_configured'):
                        process_group_step(message)
        assert_equal(messages.pop(),  permanent.MESSAGE_SETTINGS_SAVED)


    @parameterized.expand([
        (Message(from_user=User(first_name="Oleg", id=3847590291, is_bot=False,
                                username="Soler"),
                 message_id=2211, date=datetime.datetime.now(),
                 chat=Chat(id=381278125782, type="private", username="Soler"),
                 content_type="text", options=[], json_string=""), 12)
    ])
    def test_wrong_course_set(self, message, value):
        message.text = "Cake is a lie"
        with patch('modules.schedule.controller.append_user_group'):
            with patch('modules.core.source.bot.send_message', side_effect = send_message):
                with patch('modules.core.source.bot.register_next_step_handler'):
                    process_course_step(message)
        assert_equal(messages.pop(),  permanent.MESSAGE_ERROR)
