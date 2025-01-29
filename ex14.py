import math

def position(initial_pos,distance,angle,slope_angle):
    angle_rad = math.radians(angle)
    slope_rad = math.radians(slope_angle)

    #distance x,y
    horizontal_distance = distance*math.cos(angle_rad)
    vertical_distance = distance*math.sin(angle_rad)

    #displacement x,y,z
    dis_x = horizontal_distance*math.cos(slope_rad)
    dis_y = horizontal_distance*math.sin(slope_rad)
    dis_z = vertical_distance

    #final position
    final_position = [initial_pos[0]+dis_x, initial_pos[1]+dis_y, initial_pos[2]]

    return final_position


initial_pos = [0,0,0]
distance = 15
angle = 30
slope_angle = 15

final_position = position(initial_pos, distance, angle, slope_angle)

print(final_position)