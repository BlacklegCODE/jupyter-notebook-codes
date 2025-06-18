import time
from Adafruit_ADS1x15 import ADS1115
adc = ADS1115()
GAIN = 1

while True:
    value = adc.read_adc(0, gain=GAIN)
    temp_c = (value * 0.125) / 10
    print(f"Analog o/p = {value}")
    print(f"Temp. in C = {temp_c:.2f}")
    time.sleep(2)
