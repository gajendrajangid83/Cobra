# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "29907731"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "8f59d632cb374705cfdee46ac17cc3cd")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7591431005:AAHSTGbhrKqbddHPpkauBl7eJwh68nn544k")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@mjteamexbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6697397532"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002475668850"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://mehuldb:ymLdv8Sf2UW49x2m@withcluster.akoofaz.mongodb.net/")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002617386015"))

