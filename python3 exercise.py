Speed = int(input("enter your Speed:"))
Average = int(input("enter the average speed:"))
points = (Average - Speed)/5

if Speed < 60:
    print("OK")
else:
    if points >= 12:
        print("Demerit points" + str(points))
    else:
        print("Time to go to jail")


