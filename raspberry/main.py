from machine_i2c_lcd import I2cLcd
from time import sleep_ms
from machine import I2C, Pin
from rotary_irq_rp2 import RotaryIRQ

DEFAULT_I2C_ADDR = 0x27

'''
def main():
    
    #This function runs the main scripts
    

    # standard commands for set up the lcd screen
    #i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
    #lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    #lcd.putstr("Welcome on\nChess&Slaps!")
    #sleep_ms(3000)
    #lcd.clear()
    #lcd.backlight_off()
    #sleep_ms(500)
    #lcd.backlight_on()
    #lcd.putstr("Game mode:\n")    
#
    #lcd.clear()


main()
'''

def test():
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    SW=Pin(20,Pin.IN,Pin.PULL_UP)  
    r = RotaryIRQ(pin_num_clk=18,   
           pin_num_dt=19,   
           min_val=0,   
           reverse=False,   
           range_mode=RotaryIRQ.RANGE_UNBOUNDED)  
    val_old = r.value()  
    while True:  
      try:  
        val_new = r.value()  
        if SW.value()==0 and n==0:  
          print("Button Pressed")  
          lcd.putstr("Soooca\n Marceloo")
          print("Selected Number is : ",val_new)  
          n=1  
          while SW.value()==0:  
            continue  
        n=0  
        if val_old != val_new:  
          val_old = val_new  
          print('result =', val_new)  
        sleep_ms(50)  
      except KeyboardInterrupt:  
        break  

test()