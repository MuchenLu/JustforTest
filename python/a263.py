import datetime

try :
    while True :
        start = str(input())
        start = [int(i) for i in start.split(" ")]
        end = str(input())
        end = [int(i) for i in end.split(" ")]

        start = datetime.datetime(start[0], start[1], start[2])
        end = datetime.datetime(end[0], end[1], end[2])

        day_difference = abs((start - end).days)
        print(day_difference)
except EOFError :
    pass