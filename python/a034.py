try :
    while True :
        dec_num = int(input())
        print(bin(dec_num).replace("0b", ""))
except EOFError :
    pass