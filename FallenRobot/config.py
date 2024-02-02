class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 24658337
    API_HASH = "bf99242dbb7f3501f28d39f0a0383cbf"

    CASH_API_KEY = "Y5VGE1Z7YT8O54N6"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://whnbgppl:cKI-0mfAwwchdivC8dEFeYKNJzkNXYpU@kandula.db.elephantsql.com/whnbgppl"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002064023391)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://itachi:itachi@itachi.hyhnjlq.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/1f77e50cc6935f970774b.jpg"

    SUPPORT_CHAT = "yae_support"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6660419733:AAHWcG4bQbkqfZMcu9lYL12AwvFLGGbYCcw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "O0EIKHEZN4FF"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5490773419  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
