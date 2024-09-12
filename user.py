import os
import json

users = {
#     "samajhdmelpu17": "pritunl://52.140.71.35/ku/3ak8KGZh",
#     "samajhdmelpu27": "pritunl://52.140.71.35/ku/uZUhCSmf",
#     "samajhdmelpu23": "pritunl://52.140.71.35/ku/4D9myNCp",
#     "samajhdmelpu0": "pritunl://52.140.71.35/ku/jr72TJtw",
#     "samajhdmelpu1": "pritunl://52.140.71.35/ku/zEWbCrWQ",
#     "samajhdmelpu4": "pritunl://52.140.71.35/ku/aTPX4a8W",
#     "samajhdmelpu5": "pritunl://52.140.71.35/ku/SVNCkFQp",
#     "samajhdmelpu6": "pritunl://52.140.71.35/ku/vTxbVWzq",
    #  "samajhdmelpu7": "pritunl://52.140.71.35/ku/cFTxUeCT",
#     "samajhdmelpu8": "pritunl://52.140.71.35/ku/C9VZMmZ4",
         "samajhdmelpu9": "pritunl://52.140.71.35/ku/BCgKQeF9",
    #    "samajhdmelpu10": "pritunl://52.140.71.35/ku/khxCsqDZ",
 #      "samajhdmelpu11": "pritunl://52.140.71.35/ku/zKKPadEz",
  #     "samajhdmelpu12": "pritunl://52.140.71.35/ku/dyRQVdPx",
    #    "samajhdmelpu13": "pritunl://52.140.71.35/ku/sjb6NBTW",
    #    "samajhdmelpu14": "pritunl://52.140.71.35/ku/qgMGy6ve",
    #    "samajhdmelpu15": "pritunl://52.140.71.35/ku/6CJsNT8g",
    #    "samajhdmelpu17": "",
         "samajhdmelpu19": "pritunl://52.140.71.35/ku/GCHdn5qz",
    #    "samajhdmelpu20": "pritunl://52.140.71.35/ku/mBtDWthr",
    #    "samajhdmelpu21": "pritunl://52.140.71.35/ku/XeMVsydw",
    #    "samajhdmelpu22n": "pritunl://52.140.71.35/ku/uXAmT9wD",
    #    "samajhdmelpu23": "",
    #    "samajhdmelpu24": "pritunl://52.140.71.35/ku/ypcGeMJ3",
    #    "samajhdmelpu25": "pritunl://52.140.71.35/ku/7Z9eZD9t",
    #    "samajhdmelpu26": "pritunl://52.140.71.35/ku/EtfXuJTN",
    #    "samajhdmelpu27": "",
    #    "samajhdmelpu28": "pritunl://52.140.71.35/ku/eJsVRjTB",
    #    "samajhdmelpu29": "pritunl://52.140.71.35/ku/JvcajCRE",
    #    "samajhdmelup3": "pritunl://52.140.71.35/ku/ru3kujVT"
}

def add_user(username):
    if username in users:
        profile_url = users[username]
        os.system(f"pritunl-client add {profile_url}")
    else:
        print(f"User '{username}' not found in the users dictionary.")

def remove_user(userid):
    os.system(f"pritunl-client remove {userid}")

def fetch_id():
    output = os.popen('pritunl-client list -jf').read()
    data = json.loads(output)
    if len(data) > 0:
        # for item in data:
        #     if 'client_address' in item and item['client_address'].startswith("192.168.230"):
        #         userid = item['id']
        #         remove_user(userid)
        #         return

        item=data[0]
        if 'id' in item:
            userid = item['id']
            state = item['run_state']
            if state == "Inactive":
                os.system(f'pritunl-client start {userid} --mode=ovpn')
                os.system(f'pritunl-client enable {userid}')
                # break  # Exit the loop after one iteration

    else:
        userid = ""
        add_user(os.getlogin())
        fetch_id()

def remove_id():
    output = os.popen('pritunl-client list -jf').read()
    data = json.loads(output)
    if len(data) > 0:
        for item in data:
            if 'client_address' in item and item['client_address'].startswith("192.168.230"):
                userid = item['id']
                remove_user(userid)
                return
try:
    add_user(os.getlogin())
    remove_id()
    fetch_id()
except Exception as e:
    print(f"An error occurred: {str(e)}")
