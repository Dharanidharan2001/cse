import sys
a=[1,2,4,'a',8,0]
for i in a:
   try:
      c=2/i
      print(c)
   except:
      print("oops",sys.exc_info()[0],"occured")
