def file_beat(num):
    if num < 6:
        return file_beat(num + 1)
    else:
        return num

print(file_beat(0))

