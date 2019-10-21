from datetime import datetime

import telebot

from modules.electives_schedule import controller, permanent
from modules.core.source import bot, log, main_markup

"""
Module allows to set user's groups and get information about current and next lesson,
lessons at some day of week or get link to official google doc
Also may provide information about friend's current and next lessons by his alias

Authors: @Nmikriukov @thedownhill
"""


def attach_electives_schedule_module():

    @bot.message_handler(commands=['add_course'])
    def add_cousre_handler(message):
        """
        Register module's commands
        """
        log(permanent.MODULE_NAME, message)
        if message.text == '/add_course':
            lessons = controller.get_electives_course()
            lesson_list = []

            for lesson in lessons:
                lesson_list.append(lesson.subject)

            options = telebot.types.ReplyKeyboardMarkup(True, False)
            options.add(*list(lesson_list))

            reply = str("Select elective course")
            msg = bot.send_message(message.chat.id, reply, reply_markup=options)
            bot.register_next_step_handler(msg, process_electives)


    def process_electives(message):
        check = controller.check_electives_course(message.text)
        if check == True:
            controller.set_electives_user(message.from_user.id ,message.text)
            msg = bot.send_message(message.chat.id, permanent.MESSAGE_SUCCESS, reply_markup=main_markup)
        else:
            bot.send_message(message.chat.id, permanent.MESSAGE_UNKNOWN_LESSON, reply_markup=main_markup)