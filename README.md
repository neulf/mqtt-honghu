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

Configuration keys and default values:
| Key | Default | Description |
| ---- | ---- | ---- |
| mqtt-host | localhost | Hostname or IP address for MQTT broker |
| mqtt-port | 15438 | Port for MQTT broker|
| mqtt-useranme | empty | Username for MQTT authentication|
| mqtt-password | empty | Password for MQTT authentication|
| honghu-host | localhost | Hostname or IP address of Honghu|
| honghu-port | 18080 | Port for InfluxDB|
| honghu-token | empty | Token for authenticating against Honghu Hei|
| honghu-hei | empty | Hei name for Honghu|
| event-set | empty | Event set name|
| node-name | empty | Node name|