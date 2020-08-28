from json import dumps

from httplib2 import Http

import random

messageType = random.randint(1, 26)

if messageType == 1:
    msg = "a"
if messageType == 2:
    msg = "b"
if messageType == 3:
    msg = "c"
if messageType == 4:
    msg = "d"
if messageType == 5:
    msg = "e"
if messageType == 6:
    msg = "f"
if messageType == 7:
    msg = "g"
if messageType == 8:
    msg = "h"
if messageType == 9:
    msg = "i"
if messageType == 10:
    msg = "j"
if messageType == 11:
    msg = "k"
if messageType == 12:
    msg = "l"
if messageType == 13:
    msg = "m"
if messageType == 14:
    msg = "n"
if messageType == 15:
    msg = "o"
if messageType == 16:
    msg = "p"
if messageType == 17:
    msg = "q"
if messageType == 18:
    msg = "r"
if messageType == 19:
    msg = "s"
if messageType == 20:
    msg = "t"
if messageType == 21:
    msg = "u"
if messageType == 22:
    msg = "v"
if messageType == 23:
    msg = "w"
if messageType == 24:
    msg = "x"
if messageType == 25:
    msg = "y"
if messageType == 26:
    msg = "z"



def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = 'REPLACE-WITH-GOOGLE-CHAT-WEBHOOK-KEY'
    bot_message = {
        'text' : msg}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()