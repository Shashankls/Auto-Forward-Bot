from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH",'29410904')
      API_ID = int(getenv("API_ID",'7236f5160bd8c242f58d4d0a8df7d758'))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6375912755:AAF130zocBI0P3WcjjVMdgiXE6dNMBVyTZk")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002100651413:-1001968767283").replace("\n", " ").split(' '))