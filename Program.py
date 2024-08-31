def HuaQu_height(language):
    height = 1
    if language == "1":
        height = float(input("How tall are you? "))  # Convert to float for BMI calculation
    elif language == "2":
        height = float(input("你有多高? "))  # Convert to float for BMI calculation
    return height

def JiSuan_BMI(w, h, language):
    try:
        BMI = w / (h * h)
        if language == "1":
            print(f"Your BMI [Body Mass Index] is {BMI:.2f}.")
        elif language == "2":
            print(f"你的 BMI [体质指数] 是 {BMI:.2f}。")
    except ZeroDivisionError:
        if language == "1":
            print("Sorry, the height and weight you entered cannot be 0. Please re-enter.")
        elif language == "2":
            print("抱歉，您输入的身高和体重不能为 0，请重新输入。")
        # Re-enter height and weight
        height = HuaQu_height(language)
        weight = HuaQu_weight(language)
        JiSuan_BMI(weight, height, language)

def HuaQu_weight(language):
    weight = 1
    if language == "1":
        weight = float(input("How heavy are you? "))  # Convert to float for BMI calculation
    elif language == "2":
        weight = float(input("你有多重? "))  # Convert to float for BMI calculation
    return weight

def Hello_name(language):
    if language == "1": 
        name = input("What is your name? ")
        print(f"Hello, {name}, I want to ask you some questions.")
    elif language == "2":
        name = input("你的名字是什么?")
        print(f"你好, {name}, 我想问你一些问题。")

def PanDuan_age_en(age):
    if age < 4 and age > 0:
        print("You are a baby.")
    elif age >= 4 and age < 13:
        print("You are a child.")
    elif age >= 13 and age < 18:
        print("You are an adolescent.")
    elif age >= 18 and age < 65:
        print("You are a middle-aged person.")
    elif age >= 65 and age < 90:
        print("You are an old person.")
    elif age >= 90:
        print("You are a SUPER-HUMAN/miracle!")
    elif age <= 0:
        print("Are you a human?")
        age = int(input("Please re-enter your age: "))
        PanDuan_age_en(age)

def PanDuan_age_zh(age):
    if age < 4 and age > 0:
        print("你是一个婴儿。")
    elif age >= 4 and age < 13:
        print("你是一个幼儿。")
    elif age >= 13 and age < 18:
        print("你是一个青少年。")
    elif age >= 18 and age < 65:
        print("你是一个成年人。")
    elif age >= 65 and age < 90:
        print("你是一个老人。")
    elif age >= 90:
        print("你是一个超级人类、奇迹！")
    elif age <= 0:
        print("你还是一个人类吗?")
        age = int(input("请重新输入你的年龄。"))
        PanDuan_age_zh(age)

def HuaQu_age(language):
    if language == "1":
        age = int(input("How old are you? "))  # Directly convert input to int
        PanDuan_age_en(age)
    elif language == "2":
        age = int(input("你几岁了? "))  # Directly convert input to int
        PanDuan_age_zh(age)

def HuaQu_language():
    language = input("请输入你的语言/Please enter your language:\n[1, English 2, 中文] ")
    
    # Ensure language is either 1 or 2
    while language not in ["1", "2"]:
        print("Invalid input. Please enter 1 or 2.")
        language = input("请输入你的语言/Please enter your language:\n[1, English 2, 中文] ")

    return language

# Main program starts here
language = HuaQu_language()  # Get the language and assign it to the variable
Hello_name(language)  # Greet the user
HuaQu_age(language)    # Ask for the user's age
height = HuaQu_height(language)  # Capture height
weight = HuaQu_weight(language)    # Capture weight
JiSuan_BMI(weight, height, language)  # Call BMI function with captured values
