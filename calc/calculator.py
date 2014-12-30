import arithmetic

def decode_expression(expression):
#"""decodes expression for evaluation"""
    
    operator = expression.pop(0)
    
    nums = []
    
    for i in expression:
         nums.append(int(i))
    
    print evaluate_expression(nums, operator)
    

def evaluate_expression(nums, operator):
#"""passes expressions to functions for evaluation"""

    if operator in arithmetic.evaluation_methods:
        return arithmetic.evaluation_methods[operator](nums)
    else:
        print "Please enter a valid operator followed by operands."
     

def main():
#"""accepts an expression, decodes it, evaluates it, and returns the output it to the user. """

    print """Hello! My name is Jan, and I'm a prefix calculator.\nPlease place your operator to the left of its operands and we will be best friends forever.\nYou can enter a +, -, *, /, square, cube, power, or % operator."""
        
    while True:        
        expression = raw_input("What would you like to calculate?\n>").lower().split()
        
        decode_expression(expression)
        
        calculate_again = raw_input("Would you like me to evaluate another expression?\n>").lower()
        
        if calculate_again[0] == "n":
            print "Thanks for being so expressive. See you again soon!"
            break
        elif calculate_again[0] != "y":
            print "I'm sorry, I didn't understand."
            
if __name__ == "__main__":
  main()
