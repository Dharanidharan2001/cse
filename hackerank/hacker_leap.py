def is_leap(year):
    leap = False
    
   
    if year % 4 == 0 and year % 400 == 0:
        return 'True'
    else:
        if year % 100:
           return 'False'
    
    return leap

year = int(input())
