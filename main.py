import requests
from pprint import pprint

# ========================== Telegram Details Fetch ==========================

url = '1531834992:AAGUD6mRAiUf0a9O9JQTSoJHb6uvjKWGamA'
api = f'https://api.telegram.org/bot{url}/'


# create function that get chat id
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


# create function that get message text
def get_message_text(update):
    message_text = update['message']['text']
    return message_text


# create function that get last update
def last_update(req):
    response = requests.get(req + 'getUpdates')
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {'chat_id': chat_id, "text": message_text}
    response = requests.post(api + "sendMessage&parse_mode=markdown" ,data=params)
    # parse_mod=markdown
    print(response.status_code)
    return response

def send_image(chat_id, caption , user_image):
    photo = user_image
    params = {'chat_id': chat_id, "caption": caption , 'photo' : photo}
    response = requests.post(api + "sendPhoto" , data=params)
    print(response.status_code)
    return response


# create main function for nevigate or reply message back
def main():
    update_id = last_update(api)['update_id']
    while True:
        update = last_update(api)
        if update_id == update['update_id']:

            if get_message_text(update).lower() == "/start":
                first_name = last_update(api)['message']['from']['first_name']
                last_name = last_update(api)['message']['from']['last_name']
                send_message(get_chat_id(
                    update), f"Hello {first_name}  {last_name} !! Welcome To NorthFoxGroup Github User Details Fetch Bot")

            if get_message_text(update).lower() != "/start":
                try:
                    username = get_message_text(update).lower()
                    # ========================== Github Details Fetch ==========================

                    # Github API
                    url = f"https://api.github.com/users/{username}"

                    # get User data
                    user_data = requests.get(url).json()

                    send_caption = f"• Username : {user_data['login']}\n\n• Name : {user_data['name']}\n\n• Type : {user_data['type']}\n\n• Company : {user_data['company']}\n\n• Bio : {user_data['bio']}\n\n• Blog : {user_data['blog']}\n\n• Loaction : {user_data['location']}\n\n• Email : {user_data['email']}\n\n• Hireable : {user_data['hireable']}\n\n• Twitter Username : {user_data['twitter_username']}\n\n• Public Repository : {user_data['public_repos']}\n\n• Followers : {user_data['followers']}\n\n• Following : {user_data['following']}\n\n• Node Id: {user_data['node_id']}\n\n• Created At : {user_data['created_at'][:10]}\n\n• Updated At : {user_data['updated_at'][:10]}"

                    user_image = user_data['avatar_url']

                    send_image(get_chat_id(update), send_caption , user_image)
                except:
                    pass
            update_id += 1


main()