def get_oppo_seat_and_type(seat_num):
    the_key = seat_num%6 # this variable determines what type of seat by modding 6
    switcher = {
            0: "WS",
            1: "WS",
            2: "MS",
            3: "AS",
            4: "AS",
            5: "MS",
    }
    oppo_seat = switcher.get(the_key, "error finding type of seat")

    the_key2 = seat_num%12 # this variable determines oppoSeat by modding 12
    switcher2 = {
            0: -11,
            1: 11,
            2: 9,
            3: 7,
            4: 5,
            5: 3,
            6: 1,
            7: -1,
            8: -3,
            9: -5,
            10: -7,
            11: -9,
    }
    modifier = switcher2.get(the_key2,"error finding oppoSeat")
    type_seat = seat_num + modifier
    print("%s %s"%(type_seat, oppo_seat))

# beat comment is here desu
seats = []
seat_amount = int(input())
for i in range(0,seat_amount):
    seats.append(int(input()))
for i in seats:
    get_oppo_seat_and_type(i)
