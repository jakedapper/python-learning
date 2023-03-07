nums = [1,2,3]

[x * 10 for x in nums]

# list comprehension v. for loops
    # for loop
    
    numbers = [1,2,3,4,5,6,7,8]
    doubled_numbers = []

    for num in numbers:
        doubled_number = num * 2
        doubled_numbers.append(doubled_number)
    
    # list ccomprehension
   
    numbers  = [1,2,3,4,5,6,7,8]
    doubled_numbers = [num * 2 for num in numbers]
