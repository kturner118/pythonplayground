input_hours = input("Enter hours:") 

input_rate = input("Enter rate:") 

hours = float(input_hours) 

rate = float(input_rate)

if hours <=40: 
  pay= rate * hours 
  
 else:
  overtime = hours - 40
  pay = rate * 40 + (1.5 * rate * overtime) 
  print (pay) 
