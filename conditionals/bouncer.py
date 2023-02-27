age = input("How old are you? ")
if age:
	age = int(age)
	if age >= 18 and age < 21:
    	print("You can enter, but need a wristband!")
    elif age >= 21:
        print("You can enter, and you can drink!")
    else:
        print("You're too young, child.")
else:
    print("enter an age!")

# alternative ways to say the samething
# if  age and (age >= 18 and age < 21):