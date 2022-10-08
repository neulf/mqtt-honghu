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


--mqtt-host
s1a8a4e2.cn-hangzhou.emqx.cloud
--mqtt-port
15438
--mqtt-username
honghu
--mqtt-password
Lf@202209
--honghu-host
118.195.251.186
--honghu-port
18080
--honghu-token
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20ueWFuaHVhbmdkYXRhIiwiaWF0IjoxNjY0OTQzMTAxLCJleHAiOjE2NjUwMjk1MDEsInRlbmFudCI6Inlhbmh1YW5nIiwidG9rZW4iOiIzOGI4MTA1MS1iMWZjLTRhYTEtYmZiMi1hMDdmYmZhYjJhZTAiLCJkYXRhdHlwZSI6Impzb24iLCJldmVudFNldCI6InBjcyIsImV2ZW50U2V0cyI6Im1haW4scGNzIn0.lxrvEp0hYD-llTA7PWx5TD6X_51m_oWKsDtFm1vKDqCVEhwkqE5oQgtkr1Hcai-6aGYqU90gQRXCv8JmcMUn39osw1YD9Zy6iV94W3gMwuoC_SmS5wQ76uBAqgShG3krLfWOTqxsI3kDF7ASKZeBWRa0YXurRAHdaqNSOdcgBkV07H6rFKqCMymHzgzZNx0BrWfHWQkGMquiGGaG8A1mGQW3Tk1bQfX7TbSD6exyyf-HOuhpzTMf8fV7SurLf7A-YJsO9rnNgu0enszV0j5bH3ahIgHr3elOV2ujufGlccj_CsMPEUCLnZzdnjOGRWxC6b48Goqx_jHqirHpL_2fjw
--honghu-hei
mqtt
--event-set
pcs
--node-name
node1

Key	Default	Description
pidfile	empty	If set to a path, write PID file to that location
mqtt-host	localhost	Hostname or IP address for MQTT broker
mqtt-port	15438	Port for MQTT broker
mqtt-useranme	empty	Username for MQTT authentication
mqtt-password	empty	Password for MQTT authentication
honghu-host	localhost	Hostname or IP address of Honghu
honghu-port	18080	Port for InfluxDB
honghu-token	empty	Token for authenticating against Honghu Hei
honghu-hei	empty	Hei name for Honghu
event-set	empty	Event set name
node-name	empty	Node name