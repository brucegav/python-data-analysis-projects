# Program to compute sum of squares of numbers from a file
# Implements three functions: squareEach, sumList, and toNumbers
# Then uses them to process numbers from a file

def squareEach(nums):
    """
    Modifies a list by squaring each element in place.
    
    Args:
        nums: List of numbers to be squared
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    """
    Returns the sum of all numbers in the list.
    
    Args:
        nums: List of numbers to sum
    Returns:
        Sum of all numbers in the list
    """
    return sum(nums)

def toNumbers(strList):
    """
    Converts a list of strings to a list of numbers.
    Modifies the list in place.
    
    Args:
        strList: List of strings representing numbers
    """
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def main():
    # Prompt for file name
    filename = input("Enter the name of the file: ")
    
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            # Read the line and split into a list
            numbers = file.readline().strip().split()
            
            # Convert strings to numbers
            toNumbers(numbers)
            
            # Square each number
            squareEach(numbers)
            
            # Calculate the sum
            result = sumList(numbers)
            
            # Display the result
            print(f"The sum of squares is: {result}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ValueError:
        print("Error: File contains invalid numbers")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the program
if __name__ == "__main__":
    main()