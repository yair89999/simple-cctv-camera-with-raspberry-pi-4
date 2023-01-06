from gpiozero import MotionSensor
import cv2

vid = cv2.VideoCapture(0) # the camera(throught usb)
pir = MotionSensor(4) # the rpi motion sensor(throught the pins)

def take_a_pic():
    ret,frame = vid.read()
    return frame
while True:
    pir.wait_for_motion()
    print("You moved")
    taken_image = take_a_pic()
    print("image taken")
    cv2.imwrite("image.png",taken_image)
    print("image saved")
    
    pir.wait_for_no_motion()
    print("Stoped moving")