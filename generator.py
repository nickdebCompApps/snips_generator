from modules import info
import os.path
from time import sleep as Sleep

class Handler():

    def __init__(self, file):
        self.file = file
        self.body = None

    def read(self):
        with open(self.file, 'r') as script:
            for line in script:
                print(line)

    def write(self, body):
        self.body = body
        if self.body is not None:
            with open(self.file, 'a') as script:
                script.write(self.body)

    def clearAndWrite(self, body):
        self.body = body
        if self.body is not None:
            with open(self.file, 'w') as script:
                script.write(self.body)


def isFile(path):
    try:
        os.path.exists(path)
        return True
    except:
        return False


if_topics = """"""
for topic in info.__TOPICS__:
    if_topics = if_topics + """\t\n    if msg.topic == 'hermes/intent/{0}': \n        response = 'Here is the the intent! ... {1}'""".format(topic, topic)

body = """from modules import info
import paho.mqtt.client as mqtt
import requests
import json

mqtt_client = mqtt.Client()
HOST = info.__MQTT_CONFIG__['HOST']
PORT = int(info.__MQTT_CONFIG__['PORT'])
TOPICS = info.__TOPICS__

###########################################
def on_connect(client, userdata, flags, rc):
    for topic in TOPICS:
        topic = 'hermes/intent/{0}'.format(topic)
        mqtt_client.subscribe(topic)

def parse_slots(msg):
    data = json.loads(msg.payload.decode())
    return {slot['slotName']: slot['value']['value'] for slot in data['slots']}


def parse_session_id(msg):
    data = json.loads(msg.payload.decode())
    return data['sessionId']


def say(session_id, text):
    mqtt_client.publish('hermes/dialogueManager/endSession', json.dumps({'text': text, "sessionId" : session_id}))
###########################################


def on_message(client, userdata, msg):
    topicName = msg.topic.split('/')
    
    if topicName[2] not in TOPICS:
        return False
    slots = parse_slots(msg)
    %s

    print(response)
    session_id = parse_session_id(msg)
    say(session_id, response)

###########################################
if __name__ == '__main__':
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(HOST, PORT)
    mqtt_client.loop_forever()

""" % (
if_topics
)




if isFile(info.__PATH__ + 'script.py'):
    file = 'script.py'
else:
    files = open('script.py', 'w+')
    files.close()
    file = 'script.py'

handler = Handler(file)
handler.clearAndWrite(body)
handler.read()
