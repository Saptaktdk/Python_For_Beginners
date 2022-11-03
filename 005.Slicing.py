fact = "Bankai can usually only be achieved by Captain-level Soul Reapers."
print(fact[0])  #starts from leftmost index
print(fact[2])

print(fact[-1]) #starts from rightmost index
print(fact[-3])

#Slicing a string : we can get a substring from a string
print(fact[1:4]) #left index inclusive, right index exclusive
print(fact[:]) #prints the whole string

#Slicing a tuple
Bleach = ("Bankai", "Shikai", "Captain", "Hollow", "Quincy")
print(Bleach[2:4])
print(Bleach[2:4][0]) #prints the first element of the subarray
print(Bleach[2:4][0][3:6]) #prints the substring of the first element of the ssubarray

#Slicing a dictionary
Captains = {"Hirako":"Shinji","Ichimaru":"Gin","Hitsugaya":"Toshiro","Urahara":"Kisuke","Kyoraku":"Shunsui"}
print(Captains["Hirako"][-1])
print(Captains["Hirako"][2:5])

