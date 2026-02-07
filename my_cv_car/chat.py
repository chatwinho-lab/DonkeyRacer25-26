import argparse
import time
import busio
from board import SCL,SDA
from adafruit_pca9685 import PCA9685
import numpy as np

#== Constants ==
FREQ = 60
NEUTRAL = 1500
MAX = 1900
MIN = 1200

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = FREQ

# 1. Initialize the parser
parser = argparse.ArgumentParser(description="Motor testing script!")

# 2. Add arguments (Fixed syntax errors)
parser.add_argument('-e', '--esc', type=int, default=1, help='ESC channel (default: 1)')
parser.add_argument('-s', '--servo', type=int, default=0, help='Servo channel (default: 0)')
parser.add_argument('-i', '--initialize', type=int, default=0, help='Is the motor running for the first time since being switched on? (default: 0)')
parser.add_argument('--extra_option', type=str, default='', help='Message to explain the option (default: empty string)')

# 3. Parse arguments (Fixed 'Ungs' typo)
args = parser.parse_args()

# 4. Assign variables
ESC_CHANNEL = args.esc
SERVO_CHANNEL = args.servo

# If the motor is running for the first time, arm the ESC (send neutral signal for 2s)
arm_ESC = args.initialize
extra_argument = args.extra_option

# --- For verification/debugging ---
print(f"ESC Channel: {ESC_CHANNEL}")
print(f"Servo Channel: {SERVO_CHANNEL}")
print(f"Initialize: {arm_ESC}")
print(f"Extra Option: '{extra_argument}'")

pca.channels[ESC_CHANNEL].duty_cycle =  NEUTRAL
time.sleep(2)

pca.channels[ESC_CHANNEL].duty_cycle = MIN
time.sleep(5)

pca.channels[SERVO_CHANNEL].duty_cycle =  MIN
time.sleep(5)

pca.deinit()


