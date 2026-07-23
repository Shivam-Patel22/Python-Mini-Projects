def BMI():
    height=float(input("Enter Height in CentiMeter="))
    weight=float(input("Enter Weight in Kilograms="))
    bmi=(weight /(height**2))*10000
    print("Your BMI=",bmi)
    if bmi<18:
        print("Underweight")
    elif bmi> 18 and bmi<25:
        print("Normal Weight")
    elif bmi >25 and bmi<30:
        print("Over Weight")
    else:
        print("Obese")
BMI()