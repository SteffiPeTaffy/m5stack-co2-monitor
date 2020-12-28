# m5stack-co2-monitor

Disclaimer: This project is inspired by [https://github.com/aquahika/M5Stack-MHZ19-Co2Display](https://github.com/aquahika/M5Stack-MHZ19-Co2Display)

This tiny tutorial describes how you can build a CO2 measuring device that can help to reduce the spread of Covid-19. 

You can read more about the correlation between CO2-concentration and the potential risk of Covid-19 infection in this paper: [Risk assessment of aerosols loaded with virus based on CO2-concentration.](https://depositonce.tu-berlin.de/bitstream/11303/11478.3/9/hartmann_kriegel_2020_en_v3.pdf)

The following hardware and software will be used in this tutorial:

<table>
  <tr>
   <td>Hardware</td>
   <td>Software</td>
  </tr>
  <tr>
  <td><a href="https://eckstein-shop.de/M5Stack-ESP32-Basic-Core-IoT-Development-Kit">M5Stack ESP32 Basic Core IoT Development Kit</a></td>
  <td><a href="https://flow.m5stack.com/">UIFlow Web IDE</a> (MicroPython)</td>
  </tr>
  <tr>
   <td><a href="https://www.amazon.de/-/en/gp/product/B07VD15YRP/ref=ppx_yo_dt_b_asin_image_o01_s00?ie=UTF8&psc=1">ICQUANZX MH-Z19 Infrared CO2 Sensor Module</a></td>
   <td><a href="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/M5Burner_MacOS.zip">M5Stack Burner</a></td>
  </tr>
</table>



## 00 Getting started

### 1. Download and install M5Stack Burner
You can find the official instructions [here](https://m5stack.github.io/UIFlow_doc/en/en/base/Update.html)

On Mac:
*   Download the <a href="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/M5Burner_MacOS.zip">M5Stack Burner</a> & Unzip
*   Move “M5Burner” file to your application folder (:warning: important)
*   Open the application (and allow Mac to open applications from an unknown source)
    *   Go to System Preferences > Security and Privacy > General
    *   Unlock so you can make changes
    *   Allow application to open
*   Create an account for UIFlow (click on the profile symbol in the top right corner) and log in to the M5Burner application (:warning: important)
![alt_text](images/M5Burner_Setup.png)

### 2. Flash UIFlow to your M5Stack
* Connect your M5Stack Core device to your computer using USB
* Download the UIFlow (Core) for the M5Stack Core device
![alt_text](images/M5Burner_Download.png)
* Enter your wifi credentials and hit the burn button
* After successful installation of the UIFlow software, your device should display your API Key
  ![alt_text](images/M5Stack_APIKey.png)
  * Sometimes the API Key does not show up immediately despite a successful burn. Press the red button on the upper left side of the main module and select "Settings" (be quick as it is fast to disappear) > "Switch Mode" > "Internet Mode". Press the Red button again to reboot.
    ![alt_text](images/Device_InternetMode.jpg)

## 01 Hello World
It's time for your first lines of code running on your device!
* Go to <a href="https://flow.m5stack.com/">flow.m5stack.com</a>

* Click on VER and select UIFlow Beta 
  ![alt_text](images/UIFlow_ChangeVersion.png)

  ![alt_text](images/UIFlow_Version.png)

* Select Core and enter your API Key
  ![alt_text](images/UIFlow_SetupDevice.png)

* Select the Python tab and start writing your first hello world (:wave: :earth_africa:) 
  ```print('hello world!')```

* Press Run to upload to temporary memory (this program will cease to exist on a reboot)

  ![alt_text](images/UIFlow_Run.png)

* Press Download to save to disk
  ![alt_text](images/UIFlow_Download.png)

* Select the USB interface for your device and open the ```COM Monitor```
  ![alt_text](images/M5Burner_Connect.png)

* If everything is correct, it should look similar to  this

## 02 Connect the CO2 Sensor
![alt_text](images/Device_ConnectSensor.jpg)

## 03 CO2 Monitor
* In the Python tab, copy the code from [code/main.py](./code/main.py) into the console

* Press Run to ensure that the program works. If so, it will show the following:
  ![alt_text](images/Device_CO2Reading.png)

* Press Download to upload to disk

  ![alt_text](images/UIFlow_Download.png)

* Switch to App Mode and Reboot using the Red Button (upper left corner)

  ![alt_text](images/Device_AppMode.png)

* The device should show the following

  ![alt_text](images/Device_CO2Reading.png)