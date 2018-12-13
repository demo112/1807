import re
def sun_angle(time):
    #replace this for solution
    pattern = r'(\d+):(\d+)'
    t = re.match(pattern,time).groups()
    hour = int(t[0]) - 6
    min = int(t[1])
    now = hour * 60 + min
    if 720 < now  or now < 0:
        return "I don't see the sun!"
    else:
        percent = now / 12 / 60
        angle = percent * 180
        return angle

if __name__ == '__main__':
    # print("Example:")
    # print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")