"""
application config
"""
from os.path import join
from pathlib import Path


LOGGER_NAME = 'skylift'
LOGFILE_FORMAT = "%(log_color)s%(levelname)-8s%(reset)s %(cyan)s%(filename)s:%(lineno)s:%(bold_cyan)s%(funcName)s() %(reset)s%(message)s"

DIR_DATA = '../data'
FP_MAC_VENDOR = join(DIR_DATA, 'mac_vendor', 'manufacturer.csv')
DIR_JOBS = join(DIR_DATA, 'jobs')
DIR_JSON = join(DIR_DATA, 'json')
DIR_ARDUINO = join(DIR_DATA, 'ino')
DIR_NETWORKS = join(DIR_DATA, 'networks')
FP_JOBS_ARDUINO = join(DIR_JOBS, 'arduino.csv')
FP_JOBS_IOS = join(DIR_JOBS, 'ios.csv')
FP_JOBS_WIGLE = join(DIR_JOBS, 'wigle.csv')
FP_LOCATION_SUMMARY = join(DIR_ARDUINO, 'networks.h')

# OSX
FP_AIRPORT = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport'

# ESP8266
ESP_MAX_TX = 20.5  # maximum hardware TX power in dB
ESP_MIN_OP_TX = 15  # minium operational TX power in dB
