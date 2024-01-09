#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bridge.py - A bridge which forwards IoT sensor data from MQTT to Honghu.
#
# Copyright (C) 2022 Jason <neulf@hotmail.com>
#

import argparse
import re
import logging
import sys
import paho.mqtt.client as mqtt
import requests
import requests.exceptions


class MessageStore(object):

    def store_msg(self, node_name, event_name, value):
        raise NotImplementedError()


class HonghuStore(MessageStore):
    logger = logging.getLogger("bridge.HonghuStore")
    url = ""
    token = ""

    def __init__(self, host, port, token, hei_name, event_set):

        hei_name = hei_name
        event_set = event_set

        self.token = token
        self.url = f"http://{host}:{port}/api/data/v1.0/data/ingestions/events?endpoint={hei_name}&event_set={event_set}&_datatype=json"

    def store_msg(self, node_name, event_name, data):
        honghu_msg = data

        headers = {
            "Content-Type": "text/plain",
            "Authorization": 'Bearer ' + self.token
        }
        self.logger.debug("Writing Honghu Event: %s", honghu_msg)
        post_url = "{}&_source={}".format(self.url, node_name)

        try:
            res = requests.post(url=post_url, data=honghu_msg, headers=headers)
            # print(res.raw)

        except requests.exceptions.ConnectionError as e:
            self.logger.exception(e)


class MessageSource(object):

    def __init__(self):
        self._stores = None

    def register_store(self, store):
        if not hasattr(self, '_stores'):
            self._stores = []
        self._stores.append(store)

    @property
    def stores(self):
        # return copy
        return list(self._stores)


class MQTTSource(MessageSource):
    logger = logging.getLogger("bridge.MQTTSource")

    def __init__(self, host, port, username, password, node_names, stringify_values_for_measurements):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.node_names = node_names
        self.stringify = stringify_values_for_measurements
        self._setup_handlers()

    def _setup_handlers(self):
        self.client = mqtt.Client()

        def on_connect(client, userdata, flags, rc):
            self.logger.info("Connected with result code  %s", rc)
            # subscribe to /node_name/wildcard
            for node_name in self.node_names:
                topic = "{node_name}".format(node_name=node_name)
                self.logger.info(
                    "Subscribing to topic %s for node_name %s", topic, node_name)
                client.subscribe(topic)

        def on_message(client, userdata, msg):
            print("data received.")
            self.logger.info(
                "Received MQTT message for topic %s with payload %s", msg.topic, msg.payload)

            # token_pattern = '(?:\w|-|\.)+'
            # regex = re.compile(
            #     '/(?P<node_name>' + token_pattern + ')/(?P<event_name>' + token_pattern + ')/?')
            # match = regex.match(msg.topic)
            # if match is None:
            #     self.logger.warn(
            #         "Could not extract node name or measurement name from topic %s", msg.topic)
            #     return
            # node_name = match.group('node_name')
            # if node_name not in self.node_names:
            #     self.logger.warn(
            #         "Extract node_name %s from topic, but requested to receive messages for node_name %s", node_name,
            #         self.node_name)
            # event_name = match.group('event_name')
            node_name = msg.topic
            event_name = msg.topic

            stored_message = msg.payload

            for store in self.stores:
                store.store_msg(node_name, event_name, stored_message)

        self.client.on_connect = on_connect
        self.client.on_message = on_message

    def start(self):
        self.client.connect(self.host, self.port)
        self.client.username_pw_set(self.username, self.password)
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self.client.loop_forever()


def main():
    parser = argparse.ArgumentParser(
        description='MQTT to Honghu bridge for IOT data.')
    parser.add_argument('--mqtt-host', required=True, help='MQTT host')
    parser.add_argument('--mqtt-port', default="15438", help='MQTT port')
    parser.add_argument('--mqtt-username', required=True, help='MQTT username')
    parser.add_argument('--mqtt-password', default="18080", help='MQTT password')
    parser.add_argument('--honghu-host', required=True, help='Honghu host')
    parser.add_argument('--honghu-port', default="8086", help='Honghu port')
    parser.add_argument('--honghu-hei', required=True,
                        help='honghu HEI Name')
    parser.add_argument('--honghu-token', required=False, help='Token')
    parser.add_argument('--event-set', required=True,
                        help='Event set')
    parser.add_argument('--node-name', required=True,
                        help='Sensor node name', action="append")
    parser.add_argument('--stringify-values-for-measurements', required=False,
                        help='Force str() on measurements of the given name', action="append")
    parser.add_argument('--verbose', help='Enable verbose output to stdout',
                        default=True, action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    store = HonghuStore(host=args.honghu_host, port=int(args.honghu_port),
                        token=args.honghu_token, hei_name=args.honghu_hei,
                        event_set=args.event_set)

    source = MQTTSource(host=args.mqtt_host,
                        port=int(args.mqtt_port),
                        username=args.mqtt_username,
                        password=args.mqtt_password,
                        node_names=args.node_name,
                        stringify_values_for_measurements=args.stringify_values_for_measurements)
    source.register_store(store)
    source.start()


if __name__ == '__main__':
    main()
