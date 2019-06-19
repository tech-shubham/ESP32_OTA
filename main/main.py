from ota_update.main.ota_updater import OTAUpdater
from machine import Pin



 def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/tech-shubham/ESP32_OTA')
     o.download_and_install_update_if_available('Shubham', 'shubham1234')


 def start():
  
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...
  led = Pin(2, Pin.OUT)
  while True:
   led.value(not led.value())
   time.sleep(0.5)


 def boot():
     download_and_install_update_if_available()
     start()


 boot()


