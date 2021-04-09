import paho.mqtt.client as mqtt
import logbook
import os
import sys


def on_connect(client, userdata, flags, rc):
    if rc:
        log.critical("failed to connect to {}, error code is {}. Aborting.".format(mqtt_server,rc))
        sys.exit()
    else:
        log.info("connected to {}".format(mqtt_server))
        client.subscribe("#")
        log.info("subscribed to # (all topics)")


def on_message(client, userdata, msg):
    log.info("{} {}".format(msg.topic,msg.payload.decode()))


# log to console
logbook.StreamHandler(sys.stdout).push_application()
log = logbook.Logger('log-mqtt')
log.level = logbook.DEBUG if os.environ.get('DEV') else logbook.INFO

mqtt_server = "mqtt.example.com"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_server, 1883, 60)
log.info("starting MQTT loop")
client.loop_forever()