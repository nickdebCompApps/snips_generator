# Snips_generator

Generator.py is a simple generator for a snips script in order to handle intents. All you have to do is supply the information, and the generator takes care of the script to handle snips intents

In order to create an intent handling script from the generator, follow these steps:

### ON A RASPBERRY PI:


```
sudo pip install paho-mqtt && sudo pip3 install paho-mqtt
cd /home/pi
git clone https://github.com/nickdebCompApps/snips_generator.git
cd snips_generator
```

Edit the modules/info.py

The default info looks like this:

```
#INSERT INTENTS HERE - spelling/punctuation does count -
#If you need an example look at examples.py
__TOPICS__ = []

__PATH__ = ''

#MQTT HOST AND PORT - DEFAULT HOST IS localhost AND PORT IS 1883
__MQTT_CONFIG__ = {'HOST' : '', 'PORT' : ''}

#(leave the rest blank if you have no clue what they are talking about)
#ANY API KEYS YOU NEED TO BE IMPORTED WITHOUT DISPLAYING DIRECTLY IN THE SCRIPT
__KEYS__ = []
```

You will want to create an info.py file similar to the example, making sure to replace the path with the default path to the snips_generator folder, all your intents and the host and port of mqtt

The example.py looks like this:

```
#
#
#

#INSERT INTENTS HERE - spelling/punctuation does count -
#If you need an example look at examples.py
__TOPICS__ = ['searchWeatherForecast', 'searchWeatherForecastItem']

__PATH__ = '/home/pi/snips_generator/'

#MQTT HOST AND PORT - DEFAULT HOST IS localhost AND PORT IS 1883
__MQTT_CONFIG__ = {'HOST' : 'localhost', 'PORT' : '1883'}

#(leave the rest blank if you have no clue what they are talking about)
#ANY API KEYS YOU NEED TO BE IMPORTED WITHOUT DISPLAYING DIRECTLY IN THE SCRIPT
__KEYS__ = []
```

> Note: this generator is for new people who would like to get their feet wet with snips and do not really know where to start

The generator will create a new script named script.py in your current working directory

### Once info.py is updated:

Once info.py is updated with current information, run the generator.py script from the command line:


```
sudo python3 generator.py
```

After running that command, you should see a new script in the directory called script.py - run that and speak to snips

```
sudo python3 script.py
```

If something the generator finds is incorrect in your info.py script, it will default to the example.py - so if something does not look right in the new script.py, then there could be a problem with the info.py
