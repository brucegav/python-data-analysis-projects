# Program to compute the sequential day of the year
# Takes a date in mm/dd/yyyy format and returns which day of the year it is (1-365/366)

def is_leap_year(year):
    """Check if the given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_valid_date(month, day, year):
    """Verify if the given date is valid."""
    # List of days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust February for leap year
    if is_leap_year(year):
        days_in_month[1] = 29
    
    # Basic validation
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if day > days_in_month[month-1]:
        return False
    if year < 1:  # Assuming we don't handle dates before year 1
        return False
        
    return True

def compute_day_of_year(month, day, year):
    """Compute the sequential day of the year using the specified formula."""
    # Step 1: Calculate initial day number
    day_num = 31 * (month - 1) + day
    
    # Step 2: Adjust for months after February
    if month > 2:
        day_num = day_num - ((4 * month + 23) // 10)
    
    # Step 3: Adjust for leap year
    if is_leap_year(year) and month > 2:
        day_num += 1
        
    return day_num

def main():
    # Get date input from user
    print("Enter a date in mm/dd/yyyy format:")
    try:
        date_input = input().strip()
        month, day, year = map(int, date_input.split('/'))
        
        # Validate the date
        if not is_valid_date(month, day, year):
            print("Not a valid date.")
            return
            
        # Compute and display the day of the year
        result = compute_day_of_year(month, day, year)
        print(f"Day of year: {result}")
        
    except ValueError:
        print("Not a valid date.")
        return

# Run the program
if __name__ == "__main__":
    main()