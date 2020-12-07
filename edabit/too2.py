def get_number_of_apples(n, p):
    percent = int( p[:-1] )
    result = int(n * ((100 - percent)/100))
    if result < 1:
        return "The childen did not get any apples"
    else:
        return result
