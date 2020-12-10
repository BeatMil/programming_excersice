def parking_exit(lst):
    final = []
    me_next_floor = -1 # where to place player in the next floor

    for f in lst :
        if me_next_floor > -1:
            if f[me_next_floor] == 1:
                text = final[-1]
                the_num = int(text[-1]) + 1
                result = str(text[:-1]) + str(the_num)
                final[-1] = result
                continue
            else:
                f[me_next_floor] = 2

        try:
            me_index = f.index(2)
            stair = f.index(1)
        except ValueError:
            if f.count(1) == 0:
                # bottom floor
                last_index = len(f) - 1
                distance = last_index - me_index
                if distance < 0:
                    final.append("L%s"%abs(distance))
                elif distance == 0:
                  pass  
                else:
                    final.append("R%s"%abs(distance))
                break

        me_next_floor = stair

        # get direction
        distance = stair - me_index
        if distance < 0:
            final.append("L%s"%abs(distance))
        else:
            final.append("R%s"%abs(distance))

        final.append("D1")

    return final

beat = [
        [2,0,0,0,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,0],
        ]
print(parking_exit(beat))
