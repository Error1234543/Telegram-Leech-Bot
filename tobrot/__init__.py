#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

import os
import time
import logging

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from tobrot.sample_config import Config
else:
    from tobrot.config import Config
from logging.handlers import RotatingFileHandler

# TODO: is there a better way?
class Config:
    TG_BOT_TOKEN = "7764590689:AAFc4kG8_8hBRjye9MdsMndgwTfEPisSohE"
    APP_ID = 20619533
    API_HASH = "5893568858a096b7373c1970ba05e296"
    OWNER_ID = 7447651332
    AUTH_CHANNEL = [-1002432150473]

    DOWNLOAD_LOCATION = "./downloads"
    MAX_FILE_SIZE = 2097152000  # 2GB
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 500000000
    CHUNK_SIZE = 128 * 1024
    DEF_THUMB_NAIL_VID_S = 5
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    ARIA_TWO_STARTED_PORT = 6800
    EDIT_SLEEP_TIME_OUT = 10
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = 600
    MAX_TG_SPLIT_FILE_SIZE = 2097152000
    FINISHED_PROGRESS_STR = "▓"
    UN_FINISHED_PROGRESS_STR = "░"
    TG_OFFENSIVE_API = ""
    CUSTOM_FILE_NAME = ""
    LEECH_COMMAND = "leech"
    YTDL_COMMAND = "ytdl"
    RCLONE_CONFIG = "rclone.conf"
    DESTINATION_FOLDER = "./downloads"
    GLEECH_COMMAND = "gleech"
    INDEX_LINK = ""
    TELEGRAM_LEECH_COMMAND_G = "gleech"
    CANCEL_COMMAND_G = "cancel"
    GET_SIZE_G = "getsize"
    STATUS_COMMAND = "status"
    SAVE_THUMBNAIL = "savethumb"
    CLEAR_THUMBNAIL = "clearthumb"
    UPLOAD_AS_DOC = False
    PYTDL_COMMAND_G = "pytdl"
    LOG_COMMAND = "log"
    CLONE_COMMAND_G = "clone"

if os.path.exists("TorrentLeech-Gdrive.txt"):
	with open("Torrentleech-Gdrive.txt", "r+") as f_d:
		f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "Torrentleech-Gdrive.txt",
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
