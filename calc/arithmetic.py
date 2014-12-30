def add(nums):
    result = 0
    for i in nums:
        result = result + i
    return result

def subtract(nums):
    result = 0
    for i in nums:
        result = result - i
    return result
        
def multiply(nums):
    result = 1
    for i in nums:
        result = result * i
    return result

def divide(nums):
    result = nums[0]
    for i in nums[1:]:
        if i != 0:
            result = result / i
        else:
            i += 1
    return result

def square(nums):
    result = nums[0] ** 2
    print "This is the square of your first value."   
    return result

def cube(nums):
    result = nums[0] ** 3
    print "This is the cube of your first value."   
    return result

def power(nums):
    result = nums[0]
    for i in nums[1:]:
        result = result ** i 
    return result

def mod(nums):
    result = nums[0]
    for i in nums[1:]:
        if i != 0:
            result = result % i 
        else:
            i += 1
    return result

evaluation_methods = {"+": add, "-": subtract, "*": multiply, "/": divide, "square": square, "cube": cube, "power": power, "%": mod}
