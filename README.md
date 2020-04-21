# badapple
ESP8266 micropython badapple 64*32
# badapple
首先你需要一块ESP8266已经刷好了micropython固件，一块oled 12864 IIC接口（只有四个引脚）  

ESP8266 micropython badapple 64*32
OLED和ESP8266 按照如下接线  
OLED SDA  ESP8266 D1  
OLED SCL ESP8266 D2  
OLED GND ESP8266 GND  
OLED vcc ESP8266 3v3  

上传boot.py和bad.data到你的ESP8266，即可自动运行
