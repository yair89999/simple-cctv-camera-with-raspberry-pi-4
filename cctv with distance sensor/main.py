import cv2                            # camera
from gpiozero import DistanceSensor   # distance sensor
import os
import time
import datetime

camera = cv2.VideoCapture(0)
distance_sensor = DistanceSensor(echo=17,trigger=4)
distance_sensor.max_distance = 2 # change the max distance of the sensor(default is 1)


def get_distance():
    return distance_sensor.distance*100
def calibrate_distance_sensor_distance():
    start = time.time()
    distances = []
    while time.time() - start < 5:
        distances.append(get_distance())
    print(distances)
    average = sum(distances) / len(distances)
    average = str(int(average))
    return average

distance_to_check = calibrate_distance_sensor_distance()
print(distance_to_check)

def get_image():
    ret,frame = camera.read()
    return frame


def main():
    while True:
        distance = get_distance()
        if distance_to_check != str(int(distance)):
            print("someone entered")
            image = get_image() # the image of who entered
            now_time = datetime.datetime.now()
            cv2.imwrite("images/"+str(now_time)+".png",image)
            
            while distance_to_check != str(int(distance)):
                print(distance_to_check,distance)
                distance = get_distance()
        else:
            print("no movement")
main()
