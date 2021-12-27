#!/usr/bin/env python3

from hardware_modules.PCF8574 import PCF8574_GPIO
from hardware_modules.Adafruit_LCD1602 import Adafruit_CharLCD

from time import sleep, strftime
from datetime import datetime

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.

class LCD():
    def __init__(self):
        # Create PCF8574 GPIO adapter.
        try:
            self.mcp = PCF8574_GPIO(PCF8574_address)
        except:
            try:
                self.mcp = PCF8574_GPIO(PCF8574A_address)
            except:
                print ('I2C Address Error !')
                exit(1)
        self.mcp.output(3,1)     # turn on LCD backlight

        self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=self.mcp)
        self.lcd.begin(16,2)     # set number of LCD lines and columns
        self.isLoop = True

    def get_time_now(self):     # get system time
        return datetime.now().strftime('    %H:%M:%S')

    def setLoop(self, isLoop):
        self.isLoop = isLoop

    def busy(self):
        while(self.isLoop):
            self.lcd.clear()
            self.lcd.setCursor(0,0)  # set cursor position
            self.lcd.message("BUSY\n")
            self.lcd.message( self.get_time_now() )   # display the time
            sleep(1)

    def available(self):
        while(self.isLoop):
            self.lcd.clear()
            self.lcd.setCursor(0,0)  # set cursor position
            self.lcd.message("AVAILABLE\n")
            self.lcd.message( self.get_time_now() )   # display the time
            sleep(1)

    def offline(self):
        while(self.isLoop):
            self.lcd.clear()
            self.lcd.setCursor(0,0)  # set cursor position
            self.lcd.message("OFFLINE\n")
            self.lcd.message( self.get_time_now() )   # display the time
            sleep(1)

    def destroy(self):
        self.lcd.clear()
        self.mcp.output(0,0)     # turn off LCD backlight

