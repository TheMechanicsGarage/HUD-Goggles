import time
import picamera
import RPi.GPIO as GPIO
from gpiozero import Button
from signal import pause


button1 = Button(18)
button2 = Button(25)
button3 = Button(19)


def capture_image():
	imagename=time.strftime("%Y%b%d_%H:%M:%S")
	time.sleep(2)
	camera.capture('/home/pi/Pictures/%s.jpg'%imagename, resize=(1920,2560))
	camera.annotate_foreground = picamera.Color.from_rgb_bytes(0,0,255)
	camera.annotate_background = picamera.Color.from_rgb_bytes(255,255,255)
	camera.annotate_text = 'VIEW CAPTURED'
	time.sleep(2)
	camera.annotate_text = ''

def record_video():
	videoname=time.strftime("%Y%b%d %H:%M:%S")
        camera.start_recording('/home/pi/Videos/%s.h264'%videoname, resize=(1080,1920))
	camera.annotate_foreground = picamera.Color.from_rgb_bytes(0,0,255)
        camera.annotate_background = picamera.Color.from_rgb_bytes(255,255,255)
	camera.annotate_text='%s'%videoname
	camera.wait_recording()

def stop_video():
	camera.annotate_text = ''
	camera.stop_recording()


button1.when_pressed = capture_image
button2.when_pressed = record_video
button3.when_pressed = stop_video


with picamera.PiCamera() as camera:
	camera.led = False
        camera.resolution=(480,640)
	#camera.framerate=60
	camera.rotation=90
	#camera.sharpness = 0
	#camera.contrast = 0
	#camera.brightness = 50
	#camera.saturation = 0
	#camera.ISO = 0
	#camera.video_stabilization = False
	#camera.exposure_compensation = 0
	#camera.exposure_mode = 'auto'
	#camera.meter_mode = 'average'
	#camera.awb_mode = 'auto'
	#camera.image_effect = 'none'
	#camera.color_effects = None
	#camera.hflip = False
	#camera.vflip = False
	#camera.crop = (0.0, 0.0, 1.0, 1.0)
        camera.start_preview()
	while True:
                time.sleep(1)



pause()


