import sys

def perform_operations(input1, input2):
    print(f"Input 1: {input1}")
    print(f"Input 2: {input2}")
    
    # Perform basic arithmetic operations
    sum_result = float(input1) + float(input2)
    difference_result = float(input1) - float(input2)
    product_result = float(input1) * float(input2)
    
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Product: {product_result}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide exactly two inputs.")
        sys.exit(1)
    
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    
    perform_operations(input1, input2)
