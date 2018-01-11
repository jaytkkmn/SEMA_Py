#!/usr/bin/python3

from subprocess import check_output
import paho.mqtt.publish as publish


# subprocess.run(["./semaeapi_tool", "-a", "SemaEApiBoardGetStringA", "1"]) #doesn't capture output

def MQTT_pub(payload):
    host = "localhost"
    topic = "adlink/SEMA"
    publish.single(topic, payload, qos=1, hostname=host)


def getinfo():
    result = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetStringA", "1"]).decode("utf-8")

    return result



payload = getinfo()
MQTT_pub(payload)

