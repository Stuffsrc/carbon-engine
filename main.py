import time
import sys
import json
import threading
player = {
    "health": 10,
    "maxhealth": 10,
    "bleeding": 0,
}
def clearterm():
    os.system('clear')
def tick():
