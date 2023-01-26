year = int(input("Введите год: "))
day_all = 0
for month in range(13):
    if month in (1,3,5,7,8,10,12):
        for day in range(32):
            day_all += sum(map(int, str(day)))
    if month == 2:
        if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            print("Год високосный")
            for day in range(30):
                day_all += sum(map(int, str(day)))
                
        else:
            print("Год не високосный")
            for day in range(29):
                day_all += sum(map(int, str(day)))           
    if month in (4,6,9,11):
        for day in range(31):
            day_all += sum(map(int, str(day)))
print(day_all)
 
                
        