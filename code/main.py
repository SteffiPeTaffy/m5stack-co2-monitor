from m5stack import *
from m5ui import *
from uiflow import *

black = 0x000000
white = 0xFFFFFF
grey = 0x1c1c1c
green = 0x2ea23e
yellow = 0xFFCE07
orange = 0xff8407
red = 0xff0707

speaker.setVolume(20)
lcd.setRotation(3)
lcd.setTextColor(white, black)
muted = False

label_ppm = M5TextBox(25, 30, "----ppm", lcd.FONT_DejaVu40, white, rotate=0)
label_quality = M5TextBox(40, 80, "(-)", lcd.FONT_Default, white, rotate=0)
btn_mute = M5Img(110, 115, "res/mute.png", muted)

def displayReading(reading, color, label):
  setScreenColor(color)

  lcd.setTextColor(color, color)
  label_ppm.setText("        ")
  label_quality.setText("                        ")

  lcd.setTextColor(white, color)
  co2LabelText = str(reading) + "ppm"
  label_ppm.setText(co2LabelText)
  label_quality.setText(label)

  if muted is True:
    btn_mute.show()

def btnA_pressed():
  print('button pressed')
  global muted
  if muted is True:
    print('you were muted and will now be unmuted')
    btn_mute.hide()
    speaker.setVolume(20)
    muted = False
  else:
    print('you were NOT muted and will now be muted')
    btn_mute.show()
    speaker.setVolume(0)
    muted = True
btnA.wasPressed(btnA_pressed)

def calculate_checksum(res):
  checksum = sum(res[1:8])
  checksum &= 0xff
  checksum = 0xff - checksum
  checksum += 1
  return checksum

def get_co2():
  co2_cmd = b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79'
  uart1.write(co2_cmd)
  wait_ms(10)
  res = uart1.read(9)
  _, sensor, high, low, _, _, _, _, checksum = res

  if calculate_checksum(res) == checksum:
    co2_ppm = high*256+low
    print(co2_ppm)
    return co2_ppm
  else:
    raise Exception('Could. not get valid CO2 reading')


uart1 = machine.UART(1, tx=26, rx=36)
uart1.init(9600, bits=8, parity=None, stop=1, timeout=3000)
while True:
  try:
    co2_ppm = get_co2()

    if co2_ppm <= 800:
      displayReading(co2_ppm, green, '(high air quality)')
    elif co2_ppm <= 1000:
      displayReading(co2_ppm, yellow, '(medium air quality)')
    elif co2_ppm < 1400:
      displayReading(co2_ppm, orange, '(moderate air quality)')
      if muted is False:
        speaker.tone(freq=1800, duration=100)
    else:
      displayReading(co2_ppm, red, '(poor air quality)')
      if muted is False:
        speaker.tone(freq=1800, duration=5000)

  except:
    print("Could not get reading")
    pass
  finally:
    wait_ms(5000)
    
