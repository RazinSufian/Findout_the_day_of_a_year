day_list=["Monday","Tuesday","Wendsday","Thursday","Friday","Saturday","Sunday"]
day_list_2=["Monday","Sunday","Saturday","Friday","Thursday","Wendsday","Tuesday"]
year=int(input("Enter your year:"))
step_check=year-1900
days=0
step=1
start=1900

if step_check<0:
    step=-1
    start=1899
    year=year-1
for i in range(start,year,step):
    if (i%100==0) and (i%400==0):
        print(i,":LeapYear")
        days=days+366
    elif(i%4==0) and (i%100!=0):
        print(i,":LeapYear")
        days=days+366
    else:
        print(i,":NotLeapYear")
        days=days+365
print(days)
if step==1:
    print(f"The day is {day_list[days%7]}")
if step==-1:
    print(f"The day is {day_list_2[days%7]}")

#problem strats from 1772 why????????????
