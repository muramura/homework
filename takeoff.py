from dronekit import connect, VehicleMode
import time

#UDP connect
vehicle = connect('127.0.0.1:14551', wait_ready=True)

print("connected")
print(vehicle)

#Take Off(P50)
# 1.arming available
# 2.flignt mode -> `GUIDE`
# 3.arming
# 4.wait arming
# 5.take Off
# 6.check alt
#****************************************************************************#

while not vehicle.is_armable:
    print('Waiting for vehicle to initialize...')
    time.sleep(1)
print('Arming motors')
vehicle.mode = VehicleMode('GUIDED')
vehicle.armed = True

while not vehicle.armed:
    print('Waiting for arming...')
    time.sleep(1)

targetAltitude = 20
vehicle.simple_takeoff(targetAltitude)
print('Take off')

while True:
    print('Altitude',vehicle.location.global_frame.alt)
    if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95:
        print('Reach TargetAltitude')
        break
    time.sleep(1)
vehicle.close

#****************************************************************************#
# # another function
# wait_for_armable, wait_for_mode, wait_foralt, wait_for_takeoff, arm, disarm
#another format

# target_alt = 10

# guided = VehicleMode('GUIDED')
# print('Vehicle mode is {}'.format(guided))

# vehicle.wait_for_armable(30)
# print('Vehicle is armable')

# vihicle_mode = vehicle.wait_for_mode(guided, timeout=5)
# print('Vehicle mode is {}'.format(vihicle_mode))

# vehicle.arm(wait=True, timeout=5)
# print('Armed state {}'.format(vehicle.armed))

# vehicle.wait_simple_takeoff(10)
# print('takeoff!')

# while True:
#     print('Altitude',vehicle.location.global_frame.alt)
#     if vehicle.location.global_relative_frame.alt >= target_alt * 0.95:
#         print('Reach TargetAltitude')
#         break
#     time.sleep(1)

# vehicle.wait_for_mode(VehicleMode('LOITER'))
# vehicle.close

#****************************************************************************#
# # homelocation
# while not vehicle.home_location:
#     cmds = vehicle.commands
#     cmds.download()
#     cmds.wait_ready()
#     if not vehicle.home_location:
#         print("Waiting home location...")
# print('\n HomeLocation : %s'%vehicle.home_location)

#****************************************************************************#
# #get param
# print('RTL_ALT_is {}' .format(vehicle.parameters['RTL_ALT']))
# vehicle.parameters['RTL_ALT'] =2000
# print('RTL_ALT_is {}' .format(vehicle.parameters['RTL_ALT']))

# #param list
# for key, value in vehicle.parameters.iteritems():
#     print("key:%s Value:%s" %(key, value))

#****************************************************************************#
# #Listener
# def location_callback(self, attr, val):
#     print(attr)
#     print(val)
# vehicle.add_attribute_listener('location.global_frame', location_callback)
# time.sleep(10)
# vehicle.remove_attribute_listener('location.global_frame', location_callback)
# vehicle.close

# while not vehicle.mode.name == 'GUIDE' and not vehicle.armed:
#     time.sleep(1)


