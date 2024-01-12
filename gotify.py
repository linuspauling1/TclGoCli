import requests

def send_gotify_message(message, title):
    gotify_url = "http://192.168.88.2:90/message?token=AXMOOpzeOEpRMJd"
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
        title = input('Title of the message: ')
        message_text = input('Content of the message: ')
        send_gotify_message(message_text,title)
