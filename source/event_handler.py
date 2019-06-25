from source.objects.Message import Message
from source.misc import tag_member, emoji

def on_message_receive(event:'Message'):
    # here is where we will be writing code. Don't worry about all the overhead in the other modules
    print(event)
    event.respond(
        "HELLO " + tag_member(event.user) + ". I SEE YOU!!!!!" + emoji("bitcoin"),
        username="CreepyDude100",
        bot_emoji=":excellent-mrburns:"
    )
