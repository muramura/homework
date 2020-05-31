from dronekit import connect, VehicleMode
import time

vehicle = connect('127.0.0.1:14550', wait_ready=True)

print("connected")
print(vehicle)

vehicle.armed = True


# while not vehicle.mode.name == 'GUIDE' and not vehicle.armed:
#     time.sleep(1)

# vehicle.simple_takeoff
# vehicle.groundspeed
# vehicle.gimbal