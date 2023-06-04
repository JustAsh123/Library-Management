def date_inc_by_7(date):
    ddmmyy = date.split("-")
    ddmmyy[0] =int(ddmmyy[0])
    ddmmyy[1] =int(ddmmyy[1])
    ddmmyy[2] =int(ddmmyy[2])
    ddmmyy[0]+=7
    if (ddmmyy[0] > 31) and (ddmmyy[1] == 1 or ddmmyy[1] == 3 or ddmmyy[1] == 5 or ddmmyy[1] == 7 or ddmmyy[1] == 8 or ddmmyy[1] == 10 or ddmmyy[1] == 12):
        ddmmyy[0] =6
        if ddmmyy[1]==12:
            ddmmyy[2]+=1
        else:
            ddmmyy[1]+=1
    elif (ddmmyy[0] > 30) and (ddmmyy[1] == 4 or ddmmyy[1] == 6 or ddmmyy[1] == 9 or ddmmyy[1] == 11):
        ddmmyy[0] =6
        if ddmmyy[1]==12:
            ddmmyy[2]+=1
        else:
            ddmmyy[1]+=1
    ddmmyy[0] =str(ddmmyy[0])
    ddmmyy[1] =str(ddmmyy[1])
    ddmmyy[2] =str(ddmmyy[2])
    return(ddmmyy[0]+"-"+ddmmyy[1]+"-"+ddmmyy[2])
