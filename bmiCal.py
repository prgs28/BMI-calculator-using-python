
height = float(input("enter the height of person in inches"))
weight = float(input("enter the weight of person in pounds"))
bmi=(weight*(703/(height*height)))
print("your bmi is:", bmi)
if(bmi>=18.5 and bmi<=25):
    print("you have optimal bmi")
elif(bmi<18.5):
    print("you are underweight")
else:
    print("you are overweight")

