"""
This test is applicable while InnoSchedule bot instance is running

In order to run the test, you have to:

1.1 Create your bot in telegram:
    Write @BotFather the command "/newbot", follow instructions
1.2 In admin/permanent.py put your token

2.1 Run the bot: Python Innoschedule.py

3.1 Contact you bot, find out your chat id mentioning another bot, @chatid_echo_bot
3.2 Assign your chat id to the chat_id variable in this module

"""
from parameterized import parameterized, parameterized_class

import telebot
import unittest

from modules.core.source import bot, main_markup
from modules.electives_schedule import controller as elective_controller
from modules.electives_schedule import permanent as elective_permanent


# YOU NEED TO KNOW YOUR CHAT_ID
chat_id = 0


@parameterized_class([
   {'test_message': '/add_course',
    'elective': 'Advanced Python Programming',
    }
])
class TestReceiveNotification(unittest.TestCase):

    def test_add_course(self):
        """
        Register module's commands
        """
        message = self.test_message
        if message == '/add_course':
            lessons = elective_controller.get_electives_course()
            options = telebot.types.ReplyKeyboardMarkup(True, False)

            for lesson in lessons:
                line_list = telebot.types.KeyboardButton(lesson.subject)
                options.row(line_list)

            reply = str("What course you want to add?")
            ret_msg = bot.send_message(chat_id, reply, reply_markup=options)
            self.assertEqual(ret_msg.text, reply)

    def test_process_electives(self):
        message = self.elective
        check = elective_controller.check_electives_course(message)
        self.assertTrue(check)
        elective_controller.set_electives_user('test_user_id', message)
        ret_msg = bot.send_message(chat_id, elective_permanent.MESSAGE_SUCCESS, reply_markup=main_markup)
        self.assertEqual(ret_msg.text, 'The course has been successfully added!')
