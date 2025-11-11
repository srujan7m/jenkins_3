
import sys

if len(sys.argv) == 3:
        script_name = sys.argv[0]
        weight = float(sys.argv[1])
        height = float(sys.argv[2]) 
else:
        script_name = sys.argv[0]
        weight = 70.0
        height = 1.75   

bmi = weight / (height ** 2)


if bmi < 18.5:
     print( "Underweight")
elif bmi < 25:
        print("Normal weight")
elif bmi < 30:
     print( "Overweight")
else:
        print("Obesity")