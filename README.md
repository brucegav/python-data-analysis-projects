# Python Programming Fundamentals - Final Projects

A collection of Python programs demonstrating core programming concepts including file I/O, data processing, mathematical computations, and algorithm implementation. These projects showcase problem-solving skills and Python programming fundamentals.

## Projects Overview

### 1. Quiz Score Histogram Generator (`COS-2050_fp1_BG.py`)
Creates a vertical bar histogram displaying the frequency distribution of quiz scores.

**Features:**
- Reads quiz scores from `histogram.txt`
- Validates score ranges (0-10)
- Generates ASCII art histogram using asterisks
- Handles file errors gracefully

**Usage:**
```bash
python COS-2050_fp1_BG.py
```

**Sample Output:**
```
Score Distribution Histogram
(Each * represents one student)

 0 | 
 1 | 
 2 | 
 6 | *
 7 | **
 8 | ***
 9 | *
10 | *
   +----------------------------------------
    Score Frequency

Total number of scores: 8
```

### 2. Sum of Squares Calculator (`COS-2050_fp2_BG.py`)
Processes a list of numbers from a file and calculates the sum of their squares.

**Features:**
- Implements three core functions: `squareEach()`, `sumList()`, `toNumbers()`
- Reads numbers from user-specified file
- Modifies lists in-place for efficiency
- Comprehensive error handling for file operations

**Functions:**
- `squareEach(nums)`: Squares each element in the list in-place
- `sumList(nums)`: Returns the sum of all numbers in the list
- `toNumbers(strList)`: Converts string list to numeric list in-place

**Usage:**
```bash
python COS-2050_fp2_BG.py
```

### 3. Day of Year Calculator (`COS-2050_fp3_BG.py`)
Computes the sequential day of the year (1-365/366) from a given date.

**Features:**
- Accepts dates in mm/dd/yyyy format
- Handles leap year calculations
- Validates date inputs thoroughly
- Implements mathematical formula for day computation

**Algorithm:**
1. Calculate initial day number: `31 * (month - 1) + day`
2. Adjust for months after February: subtract `(4 * month + 23) // 10`
3. Add 1 for leap years when month > 2

**Usage:**
```bash
python COS-2050_fp3_BG.py
```

**Example:**
```
Enter a date in mm/dd/yyyy format:
3/15/2024
Day of year: 75
```

### 4. Fuel Efficiency Calculator (`COS-2050_fp4_BG.py`)
Calculates Miles Per Gallon (MPG) for multi-leg journeys.

**Features:**
- Tracks odometer readings and fuel consumption
- Calculates MPG for individual legs and total trip
- Interactive input for multiple journey segments
- Provides comprehensive trip summary

**Usage:**
```bash
python COS-2050_fp4_BG.py
```

**Sample Session:**
```
Enter the starting odometer reading: 12000

Enter the odometer reading and gallons used for each leg
(separated by a space, or press Enter with no input to end):

Leg 1 (odometer gallons): 12150 5.2
Leg 1 MPG: 28.8

Leg 2 (odometer gallons): 12300 4.8
Leg 2 MPG: 31.3

Trip Summary:
Total distance: 300.0 miles
Total fuel used: 10.0 gallons
Overall MPG: 30.0
```

## File Requirements

### Input Files
- `histogram.txt`: Contains quiz scores (one per line, range 0-10)
- `numbers.txt`: Contains space-separated numbers for sum of squares calculation

### Sample Data Files Included
- **histogram.txt**: Sample quiz scores (8, 7, 8, 9, 8, 7, 10, 6)
- **numbers.txt**: Sample numbers (13, 34, 14, 53, 56, 76)

## Technical Implementation

### Programming Concepts Demonstrated
- **File I/O**: Reading from text files with proper resource management
- **Error Handling**: Try-catch blocks for file operations and data validation
- **Data Validation**: Input validation for dates, numbers, and file formats
- **List Processing**: In-place modifications and data transformations
- **Mathematical Computations**: Date algorithms and statistical calculations
- **Modular Programming**: Well-structured functions with single responsibilities
- **User Interface**: Interactive command-line interfaces with clear prompts

### Python Features Used
- File handling with `with` statements
- List comprehensions and built-in functions
- String manipulation and parsing
- Exception handling with specific error types
- Function definition and parameter passing
- Mathematical operations and formulas

## How to Run

### Prerequisites
- Python 3.x
- Text files for data input (histogram.txt, numbers.txt)

### Running Individual Programs
```bash
# Histogram generator
python COS-2050_fp1_BG.py

# Sum of squares calculator
python COS-2050_fp2_BG.py

# Day of year calculator
python COS-2050_fp3_BG.py

# Fuel efficiency calculator
python COS-2050_fp4_BG.py
```

### Setting Up Data Files
1. Create `histogram.txt` with quiz scores (one per line, 0-10)
2. Create `numbers.txt` with space-separated numbers
3. Ensure files are in the same directory as the Python scripts

## Error Handling

All programs include comprehensive error handling for:
- **File not found errors**
- **Invalid data formats**
- **Out-of-range values**
- **User input errors**
- **Mathematical edge cases**

## Educational Value

These projects demonstrate fundamental programming skills including:
- Problem decomposition and algorithm design
- File processing and data manipulation
- Input validation and error handling
- Mathematical computation implementation
- User interface design for console applications
- Code organization and documentation

## Sample Test Cases

### Histogram Generator Test
```
Input file (histogram.txt): 8, 7, 8, 9, 8, 7, 10, 6
Expected: Histogram showing frequencies for each score
```

### Sum of Squares Test
```
Input file (numbers.txt): 13 34 14 53 56 76
Expected: Sum of squares = 169 + 1156 + 196 + 2809 + 3136 + 5776 = 13242
```

### Day of Year Test
```
Input: 3/15/2024 (leap year)
Expected: Day 75
Input: 12/31/2023 (non-leap year)
Expected: Day 365
```

## Course Context

Final project for COS-2050 (Computer Science Programming course) demonstrating mastery of:
- Python syntax and semantics
- Algorithm implementation
- Data processing techniques
- File I/O operations
- Error handling strategies
- Program documentation and testing