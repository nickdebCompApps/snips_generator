from modules import info
from modules import example
import paho.mqtt.client as mqtt
import requests
import json

mqtt_client = mqtt.Client()
try:
    HOST = info.__MQTT_CONFIG__['HOST']
    PORT = int(info.__MQTT_CONFIG__['PORT'])
except:
    HOST = None
    PORT = None

try:
    TOPICS = info.__TOPICS__
except:
    TOPICS = []

    
if HOST is None:
    HOST = example.__MQTT_CONFIG__['HOST']
    
if PORT is None:
    PORT = int(example.__MQTT_CONFIG__['PORT'])
    
if not TOPICS:
    TOPICS = example.__TOPICS__
    
if len(TOPICS) == 0:
    TOPICS = example.__TOPICS__

###########################################
def on_connect(client, userdata, flags, rc):
    if TOPICS is None:
        for topic in example.__TOPICS__:
            topic = 'hermes/intent/{0}'.format(topic)
            mqtt_client.subscribe(topic)
    else:
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
    	
    if msg.topic == 'hermes/intent/searchWeatherForecast': 
        response = 'Here is the the intent! ... searchWeatherForecast'	
    if msg.topic == 'hermes/intent/searchWeatherForecastItem': 
        response = 'Here is the the intent! ... searchWeatherForecastItem'	
    if msg.topic == 'hermes/intent/searchWeatherForecastCondition': 
        response = 'Here is the the intent! ... searchWeatherForecastCondition'	
    if msg.topic == 'hermes/intent/searchWeatherForecastTemperature': 
        response = 'Here is the the intent! ... searchWeatherForecastTemperature'

    print(response)
    session_id = parse_session_id(msg)
    say(session_id, response)

###########################################
if __name__ == '__main__':
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(HOST, PORT)
    mqtt_client.loop_forever()

