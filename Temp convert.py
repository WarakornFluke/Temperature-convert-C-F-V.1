#From C --> F
print("Put Temperature with unit (c or C) ")
temp = input("Temperature in Celsius (C) :")

degree= int(temp[:-1])
unit= temp[-1].upper()

if unit=="C":
    result=(9*degree)/5+32
    unit_result = "F"

answerC = print("Temperature is =",temp,"equal to", unit_result," =",result) 
#From F --> C
print("Put Temperature with unit (f or F) ")
temp = input("Temperature in Fahrenheit (F) :")

degree= int(temp[:-1])
unit= temp[-1].upper()

if unit=="F":
    result=(degree-32)*5/9
    unit_result = "C" 

answerF = print("Temperature is =",temp,"equal to", unit_result," =",result) 