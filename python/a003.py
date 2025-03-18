m_d = str(input())
m, d = m_d.split(" ")
m, d = int(m), int(d)
s = (m*2 + d) % 3
if s == 0 :
    print("普通")
elif s == 1 :
    print("吉")
else :
    print("大吉")