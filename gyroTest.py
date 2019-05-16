
from gyro import *

sensitivity = 10

while(1):
    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)
     
    acceleration_xout_scaled = acceleration_xout
    acceleration_yout_scaled = acceleration_yout
    acceleration_zout_scaled = acceleration_zout

    x_rotation = get_x_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    y_rotation = get_y_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)

    x_rotation -= 2
    y_rotation -= 8


    if(x_rotation < (sensitivity) and x_rotation > -(sensitivity) and y_rotation < (sensitivity) and y_rotation > -(sensitivity)):
        print "none"    
    elif (x_rotation < (sensitivity) and x_rotation > -(sensitivity) and y_rotation < 0):
        print "right"
    elif (x_rotation < (sensitivity) and x_rotation > -(sensitivity) and y_rotation > 0):
        print "left"
    elif (x_rotation < 0 and y_rotation < (sensitivity) and y_rotation > -(sensitivity)):
        print "forward"
    elif (x_rotation > 0 and y_rotation < (sensitivity) and y_rotation > -(sensitivity)):
        print "back"
    
