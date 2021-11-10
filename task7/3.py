weight = int(input())
height = float(input())

BMI = weight/height**2
if(BMI < 18.5):
    print("Your BMI is", round(BMI), "you are underweight")
elif BMI > 18.5 and BMI < 25:
    print("Your BMI is", round(BMI), "you have normal weight")
elif BMI > 25 and BMI < 30:
    print("Your BMI is", round(BMI), "you are slightly overweight")
elif BMI > 30 and BMI < 35:
    print("Your BMI is", round(BMI), "you are obese")
elif BMI > 35:
    print("Your BMI is", round(BMI), "you are clinically obese")    

# Under 18.5 they are underweight
# ● Over 18.5 but below 25 they have a normal weight
# ● Over 25 but below 30 they are slightly overweight
# ● Over 30 but below 35 they are obese
# ● Above 35 they are clinically obese.