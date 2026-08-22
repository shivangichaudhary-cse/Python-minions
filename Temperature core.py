temperature = float(input("Temperature : "))
unit = input("C , F or K: ")

if unit == "C" : 
  class temp_c :
    unit_c = input("Convert to F or K : ")
    if unit_c == "F" :
      print((temperature*9/5)+32)
      
    if unit_c == "K" :
      print(temperature + 273.15)
     
      
if unit == "F" :
  class temp_f :
    unit_f = input("Convert to C or K : ")
    if unit_f == "C" :
      print((temperature - 32) * 5/9 )
  
    if unit_f == "K" :
      print((temperature - 32) * 5/9 + 273.15)
 
      
if unit == "K" :
  class temp_k :
    unit_k = input("Convert C or F")
    if unit_k == "C" :
      print(temperature - 273.15)
  
    if unit_k == "F":
      print((temperature - 273.15) * 9/5 + 32)

unit_c = "C"
unit_f = "F"
unit_k = "K"

if unit == unit_c =="C" :
 class weather_c :
   if unit == unit_c and temperature >= 30 :
     print("Its a hot day")  
     
   if unit == unit_c and temperature <= 30 and temperature >= 15 :
     print("It's a lovely day")
    
   if unit == unit_c and temperature <= 15 :
     print("It's a cold day") 

if unit == unit_f =="F" :
 class weather_f :    
   if unit == unit_f and temperature >= 86 :
     print("Its a hot day")
    
   if unit == unit_f and temperature <= 86 and temperature >= 60 :
     print("It's a lovely day")
  
   if unit == unit_f and temperature <= 60 :
     print("It's a cold day")
     
if unit == unit_k =="K" :
 class weather_k :    
   if unit == unit_k and temperature >= 303.15 :
     print("Its a hot day")
    
   if unit == unit_k and temperature <= 303.15 and temperature >= 288.15 :
     print("It's a lovely day")
  
   if unit == unit_k and temperature <= 288.15 :
     print("It's a cold day")
