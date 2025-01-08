import plasma
from plasma import plasma_stick
import time
from machine import I2C
from qwstpad import QwSTPad # type: ignore
from qwstpad import DEFAULT_ADDRESS as ADDRESS # type: ignore


from snake1d import Snake

# Set how many LEDs you have
NUM_LEDS = 300

# How many times the LEDs will attempt to be updated per second. Note that this specifies the *delay* so this is just max fps
FPS = 60

#Controller setup
i2c = I2C(id=0, scl=5, sda=4) 
try:
    pad = QwSTPad(i2c, ADDRESS)
except OSError:
    print("QwSTPad: Not Connected ... Exiting")
    raise SystemExit

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_GRB)
led_strip.start(FPS)



pixels = [(0,0,0) for i in range(NUM_LEDS)]
for i in range(NUM_LEDS):
        led_strip.set_rgb(i,pixels[i][0],pixels[i][1],pixels[i][2])
position = 0
playerRGB = (125,0,125)

game = Snake()
game.gameInit()


while True:
    buttons = pad.read_buttons()
    if(buttons['-']): #QUIT (for development purposes)
        raise SystemExit
    
    new_pixels = game.draw(buttons,pixels)

    
    for i in range(len(new_pixels)): #only change updated pixels
        if new_pixels[i] != pixels[i]:
            led_strip.set_rgb(i,new_pixels[i][0],new_pixels[i][1],new_pixels[i][2])

    pixels = new_pixels
    time.sleep(1.0 / FPS)




