MODULE_NAME = "core"
DATABASE_FOLDER = "modules/admin/db"
DATABASE_NAME = "db.sqlite3"

LOG_FILE_NAME = 'log'
LOG_MAX_SIZE_BYTES = 1024 * 1024 * 10  # 10 MB
LOG_NAME = 'logger'
LOG_BACKUP_COUNT = 1
LOG_MESSAGE_FORMAT = "%(asctime)s :: %(message)s"
LOG_DATE_FORMAT = "%d.%m.%Y :: %H:%M:%S"

PROXY_PROTOCOL = 'https'
PROXY_SOCKS = 'socks5'
PROXY_LOGIN = '356819408'
PROXY_PASSWORD = 'nya8e4Es'
PROXY_ADDRESS = 'deimos.public.opennetwork.cc'
PROXY_PORT = '1090'

MESSAGE_HI = "Hi there!✋"
MESSAGE_HELP = "Schedule open platform for Innopolis students.\n\n" \
               "Some commands, that might be useful for you:\n" \
               "/configure_schedule - change group settings\n" \
               "/configure_remind - change reminders settings\n" \
               "/add_course - add an elective course to your list of reminders\n" \
               "/friend - show current and next friend's lessons\n" \
               "   or you can just send his alias directly\n" \
               "/help - show current list of commands\n"
MESSAGE_ERROR = "Sorry, I did not understand you"
MESSAGE_UNKNOWN = "Unknown message from"
