from machine import I2C,Pin
import gc
import uos
import time
import json
i2c=I2C(sda=Pin(5), scl=Pin(4), freq=40000000)
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c) 
def image(img_list):
    s=time.ticks_ms()   
    oled.fill(0)     
    for i in img_list:
        oled.hline(i[0],i[1],i[2],1)
    oled.show()
    e=time.ticks_ms()-s
    if e<100:
        time.sleep_ms(90-e)
with open('bad.data','r') as f:
    for i in f:
        try:
            z=json.loads(i)
            image(z)
        except Exception as e:
            pass
        gc.collect()
