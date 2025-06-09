# Program to calculate fuel efficiency for a multi-leg journey
# This program prompts for odometer readings and fuel usage for each leg of a trip
# and calculates MPG (Miles Per Gallon) for each leg and the total trip

def main():
    # Get initial odometer reading
    start_odometer = float(input("Enter the starting odometer reading: "))
    
    # Initialize variables to store journey data
    previous_reading = start_odometer
    total_miles = 0
    total_gallons = 0
    leg_number = 1
    
    print("\nEnter the odometer reading and gallons used for each leg")
    print("(separated by a space, or press Enter with no input to end):")
    
    while True:
        # Get input for each leg
        leg_input = input(f"\nLeg {leg_number} (odometer gallons): ")
        
        # Check if user wants to end input
        if leg_input.strip() == "":
            break
            
        try:
            # Split input into odometer reading and gallons
            current_reading, gallons = leg_input.split()
            current_reading = float(current_reading)
            gallons = float(gallons)
            
            # Calculate miles for this leg
            miles = current_reading - previous_reading
            
            # Calculate MPG for this leg
            mpg = miles / gallons
            
            # Print leg results
            print(f"Leg {leg_number} MPG: {mpg:.1f}")
            
            # Update totals
            total_miles += miles
            total_gallons += gallons
            previous_reading = current_reading
            leg_number += 1
            
        except ValueError:
            print("Error: Please enter two numbers separated by a space")
            continue
    
    # Calculate and display total MPG if any legs were entered
    if leg_number > 1:
        total_mpg = total_miles / total_gallons
        print("\nTrip Summary:")
        print(f"Total distance: {total_miles:.1f} miles")
        print(f"Total fuel used: {total_gallons:.1f} gallons")
        print(f"Overall MPG: {total_mpg:.1f}")
    else:
        print("\nNo leg data was entered.")

# Run the program
if __name__ == "__main__":
    main()
