def late_fees(d1, m1, y1, d2, m2, y2,):
    if y1 == y2 or y1 > y2:
        fine = 0
        else
            fine = (y1 - y2) * 3600:
    if m1 == m2 or m1 > m2 :
        fine=0
        else
            fine = (m1 - m2) * 300:
    if d1 == d2 or d1 > d2:
        fine=0
        else
            fine = (d1 - d2) * 10:
        print("Good boy. So no late fees")
    else:
        print("nothing")