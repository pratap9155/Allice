import re
from os import getenv
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "26788076"))
API_HASH = getenv("API_HASH", "5f6d551ff94c49365428978a182facb4")

EVAL = list(map(int, getenv("EVAL", "7499773246 1073815732").split()))
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7214950972:AAFpMkZYMIKFQrmtg2hU_c5h8FNJWTdv3b0")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Ownergit")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "ISTKHARkoBot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "ISTKHARko")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "MissYumikoo")
# ---------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://venompratap:venom9155@cluster0.dcz5eaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1001969159081))
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7499773246))
# ---------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://https://github.com/pratap9155/Allice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # -----------------------------------------
API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
API_KEY = getenv("API_KEY", 'NxGBNexGenBots0688b3') # youtube song api ke
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/venompratap")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/venompratapchat")
# ------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQGYwOwAs5bb1_BIPwq72jPbhYq4_jpwCcpimG96O91bWd07Km7wedurcOWSLLjAdr-uC8S-NLyxJIyhpTAjRlzt7jPjMKt3axHgvhN_egWRLesPSyOygZvgSvFT-iicnIDSKhzjtIUtvivaNO4ysRtfQF8oYV8nVe0Pf1qMrn0GLO_j1kUXrFZv1uQRCtJSLksBOmzE0iL2bFke3NTRAoD49oiJrXicthIAWGaXbOjgfM2SnfiBHWMIM7mDFK5TSz_P8u0je3GDxlVoVPjC3dLYXOBVmyPjyOA5n7PL7l5F0x4HpeSBCO_TT_HzOCuVcRlirBS104Z1aN6dT8OnmDzt01GYsAAAAAHEXmh9AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
# ------------------------------------------------------------------------
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/fu6jk3.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/26nzoq.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://files.catbox.moe/z0gh23.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
