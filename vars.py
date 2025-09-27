import os
from os import environ

# API Configuration
API_ID = int(os.environ.get("API_ID", "26184715"))
API_HASH = os.environ.get("API_HASH", "7fc42fe25c89660b4e0b00dd7aa0beb1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7969383923:AAH0f1LtxGuesqXK3Xwtp3SUgY2Q8HPyLKU")

CREDIT = os.environ.get("CREDIT", "♻️GABBAR♻️")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "GABBAR")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dubeyji0995:Gqaqduzpm98kT6ZF@cluster0.ekxizvl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Add your own atlas db
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "1182777261"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "7793257011").split()]  # Default to owner ID

# Channel Configuration
PREMIUM_CHANNEL = ""
# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://files.catbox.moe/fh731v.jpg").split())) # Image Link For Default Thumbnail 

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin @ItsUGBot to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}




