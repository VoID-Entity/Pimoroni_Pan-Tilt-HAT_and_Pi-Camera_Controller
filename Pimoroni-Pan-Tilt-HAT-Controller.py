import time
import pantilthat
import curses
from time import sleep
from datetime import datetime
from picamera import PiCamera

print("\n----->| # - Welcome To Pan-Tilt Control - # | <-----")
print ("\nControl your Pan-Tilt HAT with the arrow keys")
print("\nUse c to toggle picture resolution\nUse v to toggle video resolution\nUse e to toggle exposure modes\nUse w to toggle white balance modes\nUse f to toggle camera FX\n")
print("Press p to capture picture\nPress r to start video recording\nPress s to stop video recording\nPress q to quit\n")
input("Press Enter to continue...")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

camera = PiCamera()
camera.resolution = (2592, 1944) #<---Default resolution

# Choose rotation of camera module by uncommenting below.
#camera.rotation = 0
#camera.rotation = 90
camera.rotation = 180
#camera.rotation = 270

# Screen position and size of preview window. Use camera.start_preview() for default fullscreen.
camera.start_preview(fullscreen=False, window=(1230, 50, 640, 480)) #<---X/Y screen position + window size.

X=0 #<---X axis.
Y=0 #<---Y axis.
C=0 #<---Picture resolution.
V=0 #<---Video Resolution.
E=0 #<---Exposure modes.
W=0 #<---White balance.
F=0 #<---Effects.

# Key bindings for curses, invert X/Y axis according to camera rotation.
try:
    while True:
        char = screen.getch()
        if char == ord('q'): #<---Quit
            break
        elif char == curses.KEY_UP:
            pantilthat.servo_two(X)
            print ("up", X)
            X-=1 #<---Invert here
        elif char == curses.KEY_DOWN:
            pantilthat.servo_two(X)
            print ("down", X)
            X+=1 #<---Invert here
        elif char == curses.KEY_RIGHT:
            pantilthat.servo_one(Y)
            print ("right", Y)
            Y-=1 #<---Invert here
        elif char == curses.KEY_LEFT:
            pantilthat.servo_one(Y)
            print ("left", Y)
            Y+=1 #<---Invert here
        elif char == ord('p'):
            print ("Smile!")
            camera.capture("/home/bigbrother/Bilder/Pic_{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.jpg".format(datetime.now())) #<---Choose Output folder here
        elif char == ord ('r'):
            camera.start_recording("/home/bigbrother/Videos/Vid_{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}.h264".format(datetime.now())) #<---Choose Output folder here
            print ("Recording started")
        elif char == ord ('s'):
            camera.stop_recording()
            print ("Recording stopped")

# Selection of picture resolutions
        elif char == ord ('c'):
            if C==0:
                camera.resolution = (2592, 1944) #<--- 4:3
                C+=1
                print (camera.resolution)
            elif C==1:
                camera.resolution = (1920, 1080) #<--- 16:9
                C+=1
                print (camera.resolution)
            elif C==2:
                camera.resolution = (1640, 1232) #<--- 4:3
                C+=1
                print (camera.resolution)
            elif C==3:
                camera.resolution = (1640, 922) #<--- 16:9
                C+=1
                print (camera.resolution)
            elif C==4:
                camera.resolution = (1280, 720) #<--- 16:9
                C+=1
                print (camera.resolution)
            elif C==5:
                camera.resolution = (800, 600) #<---4:3
                C+=1
                print (camera.resolution)
            elif C==6:
                camera.resolution = (640, 480) #<---4:3
                C+=1
                print (camera.resolution)
            elif C==7:
                camera.resolution = (3280, 2464) #<--- 4:3
                C-=7
                print (camera.resolution)

# Selection of video resolutions
        elif char == ord ('v'):
            if V==0:
                camera.framerate = 30
                camera.resolution = (1920, 1080) #<---30 Fps 16:9
                V+=1
                print (camera.resolution, camera.framerate)
            elif V==1:
                camera.framerate = 42
                camera.resolution = (1296, 972) #<---42 Fps 4:3
                V+=1
                print (camera.resolution, camera.framerate)
            elif V==2:
                camera.framerate = 49
                camera.resolution = (1280, 720) #<---49 Fps 16:9
                V+=1
                print (camera.resolution, camera.framerate)
            elif V==3:
                camera.framerate = 49
                camera.resolution = (1024, 768) #<---49 Fps 4:3
                V+=1
                print (camera.resolution, camera.framerate)
            elif V==4:
                camera.framerate = 49
                camera.resolution = (800, 600) #<---49 Fps 4:3
                V+=1
                print (camera.resolution, camera.framerate)
            elif V==5:
                camera.framerate = 60
                camera.resolution = (640, 480) #<---60 Fps 4:3
                V+=1
                print (camera.resolution, camera.framerate)
            elif V==6:
                camera.framerate = 90
                camera.resolution = (640, 480) #<---90 Fps 4:3
                V-=6
                print (camera.resolution, camera.framerate)

# Selection of exposure modes
        elif char == ord ('x'):
            if E==0:
                camera.exposure_mode = 'auto'
                print (camera.exposure_mode)
                E+=1
            elif E==1:
                camera.exposure_mode = 'off'
                print (camera.exposure_mode)
                E+=1
            elif E==2:
                camera.exposure_mode = 'night'
                print (camera.exposure_mode)
                E+=1
            elif E==3:
                camera.exposure_mode = 'backlight'
                print (camera.exposure_mode)
                E+=1
            elif E==4:
                camera.exposure_mode = 'spotlight'
                print (camera.exposure_mode)
                E+=1
            elif E==5:
                camera.exposure_mode = 'sports'
                print (camera.exposure_mode)
                E+=1
            elif E==6:
                camera.exposure_mode = 'snow'
                print (camera.exposure_mode)
                E+=1
            elif E==7:
                camera.exposure_mode = 'beach'
                print (camera.exposure_mode)
                E+=1
            elif E==8:
                camera.exposure_mode = 'verylong'
                print (camera.exposure_mode)
                E+=1
            elif E==9:
                camera.exposure_mode = 'antishake'
                print (camera.exposure_mode)
                E+=1
            elif E==10:
                camera.exposure_mode = 'fireworks'
                print (camera.exposure_mode)
                E-=10

# Selection of white balance modes
        elif char == ord ('w'):
            if W==0:
                camera.awb_mode = 'auto'
                print (camera.awb_mode)
                W+=1
            elif W==1:
                camera.awb_mode = 'off'
                print (camera.awb_mode)
                W+=1
            elif W==2:
                camera.awb_mode = 'sunlight'
                print (camera.awb_mode)
                W+=1
            elif W==3:
                camera.awb_mode = 'cloudy'
                print (camera.awb_mode)
                W+=1
            elif W==4:
                camera.awb_mode = 'shade'
                print (camera.awb_mode)
                W+=1
            elif W==5:
                camera.awb_mode = 'tungsten'
                print (camera.awb_mode)
                W+=1
            elif W==6:
                camera.awb_mode = 'fluorescent'
                print (camera.awb_mode)
                W+=1
            elif W==7:
                camera.awb_mode = 'flash'
                print (camera.awb_mode)
                W+=1
            elif W==8:
                camera.awb_mode = 'horizon'
                print (camera.awb_mode)
                W-=8

# Selection of camera effects
        elif char == ord ('f'):
            if F==0:
                camera.image_effect = 'none'
                print (camera.image_effect)
                F+=1
            elif F==1:
                camera.image_effect = 'negative'
                print (camera.image_effect)
                F+=1
            elif F==2:
                camera.image_effect = 'solarize'
                print (camera.image_effect)
                F+=1
            elif F==3:
                camera.image_effect = 'sketch'
                print (camera.image_effect)
                F+=1
            elif F==4:
                camera.image_effect = 'denoise'
                print (camera.image_effect)
                F+=1
            elif F==5:
                camera.image_effect = 'emboss'
                print (camera.image_effect)
                F+=1
            elif F==6:
                camera.image_effect = 'oilpaint'
                print (camera.image_effect)
                F+=1
            elif F==7:
                camera.image_effect = 'hatch'
                print (camera.image_effect)
                F+=1
            elif F==8:
                camera.image_effect = 'gpen'
                print (camera.image_effect)
                F+=1
            elif F==9:
                camera.image_effect = 'pastel'
                print (camera.image_effect)
                F+=1
            elif F==10:
                camera.image_effect = 'watercolor'
                print (camera.image_effect)
                F+=1
            elif F==11:
                camera.image_effect = 'film'
                print (camera.image_effect)
                F+=1
            elif F==12:
                camera.image_effect = 'blur'
                print (camera.image_effect)
                F+=1
            elif F==13:
                camera.image_effect = 'saturation'
                print (camera.image_effect)
                F+=1
            elif F==14:
                camera.image_effect = 'colorswap'
                print (camera.image_effect)
                F+=1
            elif F==15:
                camera.image_effect = 'washedout'
                print (camera.image_effect)
                F+=1
            elif F==16:
                camera.image_effect = 'posterise'
                print (camera.image_effect)
                F+=1
            elif F==17:
                camera.image_effect = 'colorpoint'
                print (camera.image_effect)
                F+=1
            elif F==18:
                camera.image_effect = 'colorbalance'
                print (camera.image_effect)
                F+=1
            elif F==19:
                camera.image_effect = 'cartoon'
                print (camera.image_effect)
                F+=1
            elif F==20:
                camera.image_effect = 'deinterlace1'
                print (camera.image_effect)
                F+=1
            elif F==21:
                camera.image_effect = 'deinterlace2'
                print (camera.image_effect)
                F-=21
        elif char == 10:
            pantilthat.servo_one(0)
            pantilthat.servo_two(-70)
            print ("stop")
            camera.stop_preview()

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()