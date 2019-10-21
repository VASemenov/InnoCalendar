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


def attach_electivies_schedule_module():
    @bot.message_handler(commands=['electives'])
    def schedule_command_handler(message):
        """
        Register module's commands
        """
        log(permanent.MODULE_NAME, message)
        if message.text == '/electives':
            lessons = controller.get_all_lesson()
            reply = "List of electives course:\n"
            # for lesson in lessons:
            #     reply += "- /electives_"+str(lesson.id)+" "+str(lesson.subject)+" "+ str(lesson.teacher)+"\n"

            reply += permanent.HEADER_SEPARATOR.join(str(lesson) for lesson in lessons)
            msg = bot.send_message(message.chat.id, reply, reply_markup=main_markup)
            bot.register_next_step_handler(msg, process_electives)

    @bot.message_handler(regexp="^/electives_?[A-Za-z0-9_]{5,100}$")
    def process_electives(message):
        if '/electives_' in message.text:
            lessons = controller.get_all_lesson()

            options = telebot.types.ReplyKeyboardMarkup(True, False)
            options.add(*list(permanent.TEXT_BUTTON_YES_NO))

            reply = str(lessons[0].get_detail())
            msg = bot.send_message(message.chat.id, reply+permanent.MESSAGE_CONFIRMATION, reply_markup=options)
        else:
            bot.send_message(message.chat.id, permanent.MESSAGE_UNKNOWN, reply_markup=main_markup)
