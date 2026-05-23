
def int_input_bigSize(prompt):
    try:
        val = int(input(prompt))
        if val <= 0 or val > 1000:
            print("Please enter a positive integer between 1 and 1000.")
            return
        
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    return val


def int_input(prompt):
    try:
        val = int(input(prompt))
        if val <= 0:
            print("Please enter a positive integer.")
            return
        
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    return val


def int_exit_input(prompt):
    try:
        val = int(input(prompt))
        if val < 0:
            print("Please enter a non-negative integer.")
            return
        
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    return val