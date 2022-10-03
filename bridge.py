#!/usr/bin/env python
# -*- coding: utf-8 -*-

# forwarder.py - forwards IoT sensor data from MQTT to Honghu
#
# Copyright (C) 2022 Jason <neulf@hotmail.com>
#

import argparse
import paho.mqtt.client as mqtt
import requests
import json
import re
import logging
import sys
import requests.exceptions


