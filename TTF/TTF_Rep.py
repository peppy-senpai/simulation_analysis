
import random
import math

   
def Failure():
    global S
    global Slast
    global Tlast
    global Area
    global NextFailure
    global NextRepair
    
    S = S - 1
    if S == 1:
        NextFailure = Clock + math.ceil(6*random.random())
        NextRepair = Clock + 2.5
    
    Area = Area + Slast * (Clock - Tlast)
    Tlast = Clock
    Slast = S
    
def Repair():
    global S
    global Slast
    global Tlast
    global Area
    global NextFailure
    global NextRepair
    
    S = S + 1
    
    if S == 1:
        NextRepair = Clock + 2.5
        NextFailure = Clock + math.ceil(6*random.random())
    
    Area = Area + Slast * (Clock - Tlast)
    Tlast = Clock
    Slast = S
    
def Timer():
    global Clock
    global NextFailure
    global NextRepair
    
    if NextFailure < NextRepair:
        result = "Failure"
        Clock = NextFailure
        NextFailure = Infinity
    else:
        result = "Repair"
        Clock = NextRepair
        NextRepair = Infinity
    return result
    
    
Infinity = float('inf')
random.seed(1234)
SumS = 0
SumY = 0
for Reps in range(0,100,1):
    NextFailure = math.ceil(6*random.random())
    NextRepair = Infinity

    S = 2.0
    Slast = 2.0
    Clock = 0.0
    Tlast = 0.0
    Area = 0.0 
    while S > 0:
        NextEvent = Timer()
        if NextEvent == "Failure":
            Failure()
        else:
            Repair()
            
    SumS = SumS + Area/Clock
    SumY = SumY + Clock
        
print("Average failure at time " +  str(SumY/100) +
 " with average # of functional components " + str(SumS/100))

