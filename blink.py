from machine import Pin
from utime import sleep

pin = Pin("LEDW", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        print("toggle")
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
