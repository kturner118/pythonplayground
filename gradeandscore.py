score = input("Enter Score: ")

grade = float(score)

if 0.0 <= score <= 1.0:
    print (grade) 
    
elif score < 0.6:
    grade = 'F'
   
    
elif 0.6 <= score < 0.7: 
    grade = 'D'
    
elif 0.7 <= score <0.8:
    grade = 'c' 
    
elif 0.8 <= score <0.9:
    grade = 'B'
    
elif 0.9<= score <= 1.0:
    grade = 'A' 
    
print (grade) 
