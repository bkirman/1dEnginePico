from machine import Pin
from utime import sleep
from machine import I2C
from qwstpad import QwSTPad # type: ignore
from qwstpad import DEFAULT_ADDRESS as ADDRESS # type: ignore

pin = Pin("LED", Pin.OUT)
i2c = I2C(id=0, scl=5, sda=4) 
try:
    pad = QwSTPad(i2c, ADDRESS)
except OSError:
    print("QwSTPad: Not Connected ... Exiting")
    raise SystemExit

print("QwSTPad: Connected ... Starting")


print("LED starts flashing...")
while True:
    try:
        buttons = pad.read_buttons()
        if(buttons['B']):
            pin.on()
        else:
            pin.off()
        #print("toggle")
        #sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
