import math
W = float(input("Enter width:"))
print(W)
H = float(input("Enter Height:")) 
print(H)
WHRatio = W/H
if WHRatio < 1:
 epsr = float(input("enter Releative permitivity"))
 x=1+12*(H/W)
 y=(1-WHRatio)**2
 Epseff=((epsr+1)/2)+((epsr-1)/2)*((1/math.sqrt(x))+0.04*y)
 print(Epseff)
 temp=8*(H/W)+(25/100)*(W/H)
 Zo = 60/math.sqrt(Epseff)*math.log(temp)
 print(Zo)
else:
 x=1+12*(H/W)
 y=(1-WHRatio)**2
 Epseff=((epsr+1)/2)+((epsr-1)/2*math.sqrt(x))
 print(Epseff)
 Zo = 120*3.14/(math.sqrt(Epseff)*((W/H)+1.393+(2/3)*math.log((W/H)+1.444)))
 print(Zo)