#  Interview question, solution by Aaron Mark #


def is_this_the_angle(flot, angle):
    if angle - 2.75 <= flot <= angle + 2.75:
        return True


def time_to_angle(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    return angle


def all_times_of_certain_angle(angle):
    if angle > 180:
        angle = 360 - angle

    times_list = []
    for i in range(12):
        for j in range(60):
            flot = time_to_angle("{:02d}:{:02d}".format(i, j))
            if is_this_the_angle(flot, angle):
                times_list.append("{:02d}:{:02d}".format(i, j))

    return times_list


def time_to_minutes(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


if __name__ == '__main__':

    ninety_degrees_angles = all_times_of_certain_angle(90)
    print("90º angles:", ninety_degrees_angles)
    print("There are", len(ninety_degrees_angles))

    one_eighty_degrees_angles = all_times_of_certain_angle(180)
    print("180º angles:", one_eighty_degrees_angles)
    print("There are", len(one_eighty_degrees_angles))

