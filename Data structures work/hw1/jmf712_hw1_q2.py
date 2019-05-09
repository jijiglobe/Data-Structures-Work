def shift(list, step, direction = "right"):
    copy = []
    for x in range(len(list)):
        copy.append(0)
    if direction == "right":
        index = 0
    else:
        index = len(list)
    for x in list:
        if direction == "right":
            copy[(index + step) % len(list)] = x
        else:
            copy[(index - step) % len(list)] = x
        index+=1
    index = 0
    for x in copy:
        list[index] = x
        index += 1
