input_score= input("Enter score:") 
score=float(input_score) 
grade= A if score == 1.0 else F
try:
  score is >= 0.0 or <= 1.0 
  print(grade)
 except:
 print ('error outside range') 
  
