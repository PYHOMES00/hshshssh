import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7477581065:AAG24CLKLPsIOqvlnEssh0jGeFLdeIL6DBk")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28243586"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://madarazbotz:riVNFzoBGQlnkmEA@cluster0.4nx2vpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


from os import environ

API = environ.get("API", "") # shortlink api
URL = environ.get("URL", "") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.
