#!usr/bin/env python
# -*- coding: utf-8 -*-

from dronekit import connect, VehicleMode
import time

#UDP connect
vehicle = connect('127.0.0.1:14550', wait_ready=True)
print("connected")
print(vehicle)

# #Move(P59)
# #new format
# target_alt = 10

# guided = VehicleMode('GUIDED')
# print('Vehicle mode is {}'.format(guided))

# vehicle.wait_for_armable(30)
# print('Vehicle is armable')

# vehicle.wait_for_mode(guided, timeout=5)
# print('mode changed')

# vehicle.arm(wait=True, timeout=5)
# print('Armed state {}'.format(vehicle.armed))

# vehicle.wait_simple_takeoff(target_alt, timeout=10)
# print('takeoff!')

# msg = vehicle.message_factory.set_position_target_local_ned_encode(0,0,0, mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
# 0b0000111111000111, 0,0,0, velocity_x, velocity_y, velocity_z, 0,0,0,0,0)
# msg = vehicle.message_factory.command_long_encode(0,1, mavutil.mavlink.MAV_CMD_CONDITION_YAW, 
# 0,90,0,1,1,0,0,0)

# for x in range(0, duration):
#     vehicle.send_mavlink(msg)

# # vehicle.wait_for_mode(VehicleMode('LOITER'))

# vehicle.close



#Take Off(P50)
# 1.arming available
# 2.flignt mode -> `GUIDE`
# 3.arming
# 4.wait arming
# 5.take Off
# 6.check alt
#****************************************************************************#
# #Take Off(P50)
# while not vehicle.is_armable:
#     print('Waiting for vehicle to initialize...')
#     time.sleep(1)

# vehicle.mode = VehicleMode('GUIDED')
# vehicle.armed = True
# print('Arming motors')

# #Take Off(P51) ｱｰﾐﾝｸﾞが完了するまで待つ
# while not vehicle.armed:
#     print('Waiting for arming...')
#     time.sleep(1)

# targetAltitude = 20
# vehicle.simple_takeoff(targetAltitude)
# print('Take off')

# #Take Off(P52)目標の高度に達するまで待つ
# while True:
#     print('Altitude',vehicle.location.global_frame.alt)
#     if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95:
#         print('Reach TargetAltitude')
#         break
#     time.sleep(1)

# vehicle.close

#****************************************************************************#
# another function
#wait_for_armable, wait_for_mode, wait_foralt, wait_for_takeoff, arm, disarm
#****************************************************************************#

#new format
target_alt = 10

guided = VehicleMode('GUIDED')
print('Vehicle mode is {}'.format(guided))

vehicle.wait_for_armable(30)
print('Vehicle is armable')

vehicle.wait_for_mode(guided, timeout=5)
print('mode changed')

vehicle.arm(wait=True, timeout=5)
print('Armed state {}'.format(vehicle.armed))

vehicle.wait_simple_takeoff(target_alt,timeout=10)
print('takeoff!')

# vehicle.wait_for_mode(VehicleMode('LOITER'))

vehicle.close

# # ****************************************************************************#
# # homelocation
# while not vehicle.home_location:
#     cmds = vehicle.commands
#     cmds.download()
#     cmds.wait_ready()
#     if not vehicle.home_location:
#         print("Waiting home location...")
# print('\n HomeLocation : %s'%vehicle.home_location)

## ****************************************************************************#
# #get param
# print('RTL_ALT_is {}' .format(vehicle.parameters['RTL_ALT']))
# vehicle.parameters['RTL_ALT'] =2000
# print('RTL_ALT_is {}' .format(vehicle.parameters['RTL_ALT']))

# #param list
# for key, value in vehicle.parameters.iteritems():
#     print("key:%s Value:%s" %(key, value))

##****************************************************************************#
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


