import os
import telebot
import telegram
from telebot import types
import emoji
import time
import pickle
from flask import Flask, request
from instagram_private_api import Client
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

# Telegram variables
TOKEN = os.getenv("TOKEN")

# Instagram variables
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = telebot.TeleBot(TOKEN, threaded=True)

client = Client(USERNAME, PASSWORD)

ADMIN_ID = os.getenv("ADMIN_ID")
GROUP_ID = os.getenv("GROUP_ID")



force_reply = types.ReplyKeyboardRemove(selective=False)