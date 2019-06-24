# pip3 install slackclient==2.0.0
# pip3 install websocket-client
import time
from slackclient import SlackClient


TOKEN = open("TOKEN.txt").read()
sc = SlackClient(TOKEN)

def run():
    # do some stuff that I don't know, but the docs say to do
    if sc.rtm_connect():
        sc.rtm_send_message("welcome-test", "test")

        # while the PC is connected to the server, get the events since the last check
        while sc.server.connected is True:
            for event in sc.rtm_read():

                # check if the event which occurred is a message being sent
                if "type" in event and event["type"] == "message":

                    # this bit is important.
                    # it checks if the sender is this bot. Without it, the bot sends the message,
                    # and is triggered by the message it has sent, causing an infinite loop.
                    if "subtype" in event and event["subtype"] == "bot_message":
                        continue

                    print(event)

    # check every 1/2 s to not overload slack too much.
    time.sleep(0.5)