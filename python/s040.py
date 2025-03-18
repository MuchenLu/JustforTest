start_end = str(input())
start_end = start_end.split(" ")
start = int(start_end[0])
end = int(start_end[1])
end += 1
anss = []
for i in range(start, end) :
    num_list = list(str(i))
    num_len = len(num_list)
    summon = 0
    for num in num_list :
        summon += int(num) ** num_len
    if i == summon :
        anss.append(i)

if len(anss) > 0 :
    for ans in anss :
        if ans != anss[-1] :
            print(ans, end = " ")
        else :
            print(ans, end = "")
else :
    print("none")