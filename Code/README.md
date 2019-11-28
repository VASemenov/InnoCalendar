# InnoCalendar telegram bot

[@innocalendarv1_bot](https://t.me/innocalendarv1_bot)

This bot is an extension of the original InnoSchedule bot (https://gitlab.com/Louie_ru/InnoSchedule/)


# How it works

- `python3` was developed on version 3.7
- `PyTelegramBotAPI` for work with telegram api
- `sqlalchemy` ORM
- `sqlite3` database


# Existing modules

At the moment there are 7 modules:

1. `core` is the head module that links everything together. Contains all the necessary functionality for other modules:
    - work with Telegram API
    - logging
    - establish a database connection
2. `admin ` contains commands for admins. For example, displaying statistics or sending notifications to everyone
3. `schedule ` allows you to get the schedule for a specific time or day of the week, as well as to see the schedule of friends
4. `remind` sends out reminders about coming lesson
5. `sample` is a working example of a simple module. It will be useful for those who want to add their own module
6. `electives_schedule` allows you to get the schedule of any elective course.
7. `autoparser` automatically parse schedule from google sheets
    Additionally, sends information on schedule changes for the elective courses.



# Install and run

```
1. Create your bot
Write @BotFather on Telegram command '/newbot'
Provide your bot's name and username
Put your bot's token into admin/permanent 'token' parameter

2. Install requirements and run your bot
pip3 install -r requirements.txt
python3 InnoSchedule.py

```

