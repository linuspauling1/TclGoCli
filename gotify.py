import requests

def send_gotify_message(title, message, url, token):
    gotify_url = url+"/message?token="+token
    data = {
        "title": title,
        "message": message,
        "priority": 10,
    }
    response = requests.post(gotify_url, json=data)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

if __name__ == "__main__":
    while True:
        url = input('Server URL: ')
        token = input('Token: ')
        title = input('Title of the message: ')
        message_text = input('Content of the message: ')
        send_gotify_message(message_text,title,url,token)
