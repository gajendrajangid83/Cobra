# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "21157244"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "4981c2699bd91c7db836ec8f77e5b0f0")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8347630166:AAFCrvaixyRfrrz_dLreB5mJdVDgbQzDlDc")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@testseriesgajju_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1783306092"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1783306092").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002887045646"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://saraswatisharmapbc:L8aRiWhBbhi8mFwN@cluster0.gxhxgye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002887045646"))

