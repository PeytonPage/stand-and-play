from gyro import *
while(1):
    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)
     
    acceleration_xout_scaled = acceleration_xout / 16384.0
    acceleration_yout_scaled = acceleration_yout / 16384.0
    acceleration_zout_scaled = acceleration_zout / 16384.0

    x_rotation = get_x_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    y_rotation = get_y_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)

    print "x: {}, y: {}".format(x_rotation, y_rotation)
