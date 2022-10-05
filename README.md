# mqtt-honghu
A bridge from mqtt to honghu.

The MQTT topic structure and measurement values are mapped as follows:
The measurement name becomes the Honghu event set name.

The console show some logs as follows:

    INFO:bridge.MQTTSource:Connected with result code  5
    INFO:bridge.MQTTSource:Subscribing to topic /node1/# for node_name node1
    INFO:bridge.MQTTSource:Connected with result code  0
    INFO:bridge.MQTTSource:Subscribing to topic /node1/# for node_name node1
    INFO:bridge.MQTTSource:Received MQTT message for topic /node1/pcs with payload b'{\n"temp": "36.1"\n}'