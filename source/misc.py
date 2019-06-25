def tag_member(user):
    return "<@{}>".format(user)


def emoji(name):
    if not name.startswith(":"):
        name = ":" + name
    if not name.endswith(":"):
        name += ":"
    return name