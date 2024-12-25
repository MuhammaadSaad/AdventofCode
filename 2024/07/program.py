from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluate the expression based on the numbers and operators provided."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))  # Concatenate numbers
 
    return result

def can_make_true(test_value, numbers,part2=False):
    """Check if the test value can be made true with the given numbers."""
    n = len(numbers)
    # Generate all combinations of operators (+, *) for the positions between numbers
    
    if part2:
        for operators in product(['+', '*', '||'], repeat=n-1):
            if evaluate_expression(numbers, operators) == test_value:
                return True
    else:
        for operators in product(['+', '*'], repeat=n-1):
            if evaluate_expression(numbers, operators) == test_value:
                return True
    return False

def main():
    f = open("input.txt").read().strip().split("\n")
    input_data =f

    total_calibration_result = 0

    for line in input_data:
        test_value, numbers_str = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers_str.strip().split()))

        if can_make_true(test_value, numbers,False):
            total_calibration_result += test_value
        if can_make_true(test_value, numbers,True):
            total_calibration_result += test_value
    print("Total Calibration Result:", total_calibration_result)

if __name__ == "__main__":
    main()