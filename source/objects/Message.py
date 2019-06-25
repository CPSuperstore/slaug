from datetime import datetime

from source.gv import sc
import source.gv as gv
import source.misc as misc


class Message:
    """
    This class encapsulates the event of a message being sent (with some additional "features")
    
    Attributes:
        client_msg_id           
        suppress_notification   
        type                    The type of event which this class encapsulates. Should always be "message", otherwise, we have a problem 
        text                    The text which was sent
        user                    The ID of the user who sent the message
        team                    The ID of the team which the message was sent to
        user_team               The ID of the team which the user belongs to (Generally the same as the "team" attribute)
        source_team             
        channel                 The ID of the channel which the message was received from
        event_ts                The DateTime timestamp of when the event occurred (Originally UNIX time, but converted to DateTime)
        ts                      The DateTime timestamp of when the event occurred (Originally UNIX time, but converted to DateTime)
    """
    def __init__(self, json:dict):
        """
        The Object Which Can Encapsulate The Message Event
        :param json: The JSON (dictionary) which was received by the server as a message
        """
        self.client_msg_id = json["client_msg_id"]                              # type: str
        self.suppress_notification = json["suppress_notification"]              # type: str
        self.type = json["type"]                                                # type: str
        self.text = json["text"]                                                # type: str
        self.user = json["user"]                                                # type: str
        self.team = json["team"]                                                # type: str
        self.user_team = json["user_team"]                                      # type: str
        self.source_team = json["source_team"]                                  # type: str
        self.channel = json["channel"]                                          # type: str
        self.event_ts = datetime.utcfromtimestamp(float(json["event_ts"]))      # type: datetime
        self.ts = datetime.utcfromtimestamp(float(json["ts"]))                  # type: datetime

    def __str__(self):
        """
        The toString event
        :return: the user, message, and time of this event
        """
        return "User: '{}', Sent Message: '{}', At {} UTC".format(self.user, self.text, self.event_ts.strftime('%Y-%m-%d %H:%M:%S'))

    def to_dict(self):
        """
        Generates a dictionary representation of this object
        :return: the dict object
        """
        return {
            "client_msg_id": self.client_msg_id,
            "suppress_notification": self.suppress_notification,
            "type": self.type,
            "text": self.text,
            "user": self.user,
            "team": self.team,
            "user_team": self.user_team,
            "source_team": self.source_team,
            "channel": self.channel,
            "event_ts": self.event_ts,
            "ts": self.ts
        }

    def respond(self, message, bot_emoji:str=None, icon_url:str=None, username:str=None):
        """
        Sends a message to the channel, where the message which is insulated by this class, was sent on
        :param message: The message to send
        :param bot_emoji: The emoji to use as the bot's icon in the response (If not specified, the value stored in he gv module (source.gv) will be used in place)
        :param icon_url: The URL to the image to use as the bot's icon in the response (If not specified, the value stored in he gv module (source.gv) will be used in place)
        :param username: The name to display the response from (If not specified, the value stored in he gv module (source.gv) will be used in place)
        """
        if bot_emoji is not None:
            bot_emoji = misc.emoji(bot_emoji)
        else:
            bot_emoji = gv.bot_emoji

        if icon_url is None: icon_url = gv.icon_url
        if username is None: username = gv.username

        sc.api_call(
            "chat.postMessage",
            channel=self.channel,
            text=message,
            icon_emoji=bot_emoji,
            icon_url=icon_url,
            username=username
        )
