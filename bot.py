import requests
import json
import configparser

class telegram_chatbot():
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        print(self.base)
    
    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset+1)
        r = requests.get(url)
        return json.loads(r.content)
    
    def send_message(self, message, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, message)
        if message is not None:
            requests.post(url)
    
    def read_token_from_config_file(self, config):
        parser = configparser.ConfigParser()
        parser.read(config)
        print(config)
        return parser.get('creds', 'token')
        