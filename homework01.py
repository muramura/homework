#!usr/bin/env python
# -*- coding: utf-8 -*-
print( "Did you start 'sim_vehicle.py -v ArduCopter ??'" ) 


from dronekit import connect, VehicleMode    
import time                   

#UDP connect
vehicle = connect('127.0.0.1:14550', wait_ready=True)
print("connected")
print(vehicle)

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

#Ctrl+cが押されるまでループ
try:
    while True:
        # vehicleオブジェクト内のステータスを表示
        print("--------------------------" )
        print(" GPS: %s" % vehicle.gps_0 )
        print(" Battery: %s" % vehicle.battery )
        print(" Last Heartbeat: %s" % vehicle.last_heartbeat )
        print(" Is Armable?: %s" % vehicle.is_armable )
        print(" System status: %s" % vehicle.system_status.state )
        print(" Mode: %s" % vehicle.mode.name )

        time.sleep(1)

except( KeyboardInterrupt, SystemExit):  
    print( "SystemExit" )

vehicle.close()


print("close")   