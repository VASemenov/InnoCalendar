MODULE_NAME = "remind"
TIMEZONE_OFFSET_MINUTES = 60
REMIND_WHEN_LEFT_MINUTES = 10 + TIMEZONE_OFFSET_MINUTES


MESSAGE_YES = "Yes 🙋"
MESSAGE_NO = "No 🙅"
MESSAGE_SETTINGS_SAVED = "Your remind settings have been saved successfully!"
MESSAGE_ERROR = "Sorry, I did not understand you"
REQUEST_REMINDERS = f"Would you like to get reminders {REMIND_WHEN_LEFT_MINUTES-TIMEZONE_OFFSET_MINUTES} minutes "\
                    "before every lecture, tutorial and lab? 🚨"


HEADER_REMIND = "⏰\n"
