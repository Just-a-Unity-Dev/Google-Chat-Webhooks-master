from json import dumps

from httplib2 import Http


def main():
    webhook = 'REPLACE-WITH-GOOGLE-CHAT-WEBHOOK-KEY'
    print("Using webhook ",webhook)
    msg = input("Message here: ")

    """Hangouts Chat incoming webhook quickstart."""
    url = webhook
    bot_message = {
        'text' :'Annoucement: ' +  msg}

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