import random 

count = 0
rand = random.randint(1, 100)
def LessOrGreater(one, two):
   if (one -10)> two :
       print("try a smaller one ")
   elif (one +10)< two :
       print("try a biger one ")
    
while count < 6:
    _in = int(input("enter a number between 1 and 100"))
    if _in != rand :
        count+=1
        print("attempt ",count)
        LessOrGreater(_in,rand)
    else :
        print("great job ! you won ")       
     
    

