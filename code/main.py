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

setScreenColor(black)
speaker.setVolume(1)
muted = False

bar_bgr = M5Rect(10, 35, 300, 90, grey, grey)
bar_line = M5Rect(10, 35, 10, 90, 0x1c1c1c, 0x1c1c1c)
label_low = M5TextBox(10, 135, "low", lcd.FONT_Default, white, rotate=0)
label_high = M5TextBox(278, 135, "high", lcd.FONT_Default, white, rotate=0)
label_ppm = M5TextBox(60, 155, "----ppm", lcd.FONT_DejaVu40, white, rotate=0)
label_quality = M5TextBox(80, 200, "(-)", lcd.FONT_Default, white, rotate=0)
btn_mute = M5Img(60, 220, "res/mute.png", muted)

label_battery = M5TextBox(280, 6, "---%", lcd.FONT_Default, white, rotate=0)
img_battery = M5Img(260, 2, "res/battery.png", True)


def btnA_pressed():
  print('button pressed')
  global muted
  if muted is True:
    print('you were muted and will now be unmuted')
    btn_mute.hide()
    speaker.setVolume(1)
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


uart1 = machine.UART(1, tx=17, rx=16)
uart1.init(9600, bits=8, parity=None, stop=1, timeout=3000)
while True:
  label_battery.setText(str(power.getBatteryLevel()) + '%')
  
  try:
    co2_ppm = get_co2()
    bar_bgr.setPosition(x=10, y=40)
    bar_bgr.setSize(width=300)
    
    line_width = int(co2_ppm*300/1400)
    bar_line.setSize(width=line_width)
  
    if co2_ppm <= 800:
      bar_line.setBgColor(green)
      label_quality.setText('(high air quality)')
    elif co2_ppm <= 1000:
      bar_line.setBgColor(yellow)
      label_quality.setText('(medium air quality)')
    elif co2_ppm < 1400:
      bar_line.setBgColor(orange)
      label_quality.setText('(moderate air quality)')
      if muted is False:
        speaker.tone(freq=1800, duration=100)
    else:
      bar_line.setBgColor(red)
      label_quality.setText('(poor air quality)')
      bar_line.setSize(width=300)
      if muted is False:
        speaker.tone(freq=1800, duration=5000)
  
    co2LabelText = str(co2_ppm) + "ppm"
    label_ppm.setText(co2LabelText)
  except:
    print("Could not get reading")
    pass
  finally:
    wait_ms(5000)
