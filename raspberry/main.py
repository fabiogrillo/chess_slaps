from machine_i2c_lcd import I2cLcd
from time import sleep_ms
from machine import I2C, Pin
from rotary_irq_rp2 import RotaryIRQ

DEFAULT_I2C_ADDR = 0x27

def start_game(game_value):
  if game_value == 3:
    print("starting blitz")
    lcd.clear()
    lcd.putstr("U select blitz")
    sleep_ms(3000)
  else:
    lcd.clear()
    lcd.putstr("selected wrogn number")
    sleep_ms(3000)
  return

def display_menu(game_value):
  lcd.clear()
  if game_value == 0:
    mode = 'Rapid\n'
  elif game_value == 1:
    mode = 'Rapid'
  elif game_value == 2:
      mode = 'Blitz'
  elif game_value == 3:
      mode = 'Bullet'
  
  lcd.putstr(mode)
  lcd.putstr("\nPress to start")


  
def main():
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    SW=Pin(20,Pin.IN,Pin.PULL_UP)  
    r = RotaryIRQ(pin_num_clk=18,   
           pin_num_dt=19,   
           min_val=0,
           max_val=3,   
           reverse=True,   
           range_mode=RotaryIRQ.RANGE_BOUNDED)  
    val_old = r.value()  
    while True:  
      try:  
        val_new = r.value()  
        if SW.value()==0 and n==0:  
          print("Button Pressed")  
          print("Selected Number is : ",val_new)
          start_game(val_new)  
          n=1  
          while SW.value()==0:  
            continue  
        n=0  
        if val_old != val_new:  
          val_old = val_new
          print('result =', val_new)
          display_menu(val_new)  
        sleep_ms(50)  
      except KeyboardInterrupt:  
        break  

main()
