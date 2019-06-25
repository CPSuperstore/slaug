from slackclient import SlackClient

TOKEN = open("API.token").read()

sc = SlackClient(TOKEN)


bot_emoji = None
icon_url = None
username = None