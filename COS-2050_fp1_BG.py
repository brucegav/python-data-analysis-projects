# Program to create a vertical bar histogram of quiz scores
# Reads scores from "histogram.txt" and displays frequency of each score

def read_scores():
    """
    Read scores from histogram.txt file.
    Returns a list of valid scores or None if there's an error.
    """
    try:
        scores = []
        with open("histogram.txt", "r") as file:
            for line in file:
                # Convert line to integer and validate range
                score = int(line.strip())
                if 0 <= score <= 10:
                    scores.append(score)
                else:
                    print(f"Warning: Ignoring invalid score {score} (must be 0-10)")
        return scores
    except FileNotFoundError:
        print("Error: histogram.txt not found")
        return None
    except ValueError:
        print("Error: File contains invalid data")
        return None

def count_scores(scores):
    """
    Count occurrences of each score (0-10).
    Returns a list where index represents score and value represents count.
    """
    # Initialize list with 11 zeros (for scores 0-10)
    counts = [0] * 11
    
    # Count occurrences of each score
    for score in scores:
        counts[score] += 1
        
    return counts

def draw_histogram(counts):
    """
    Draw vertical bar histogram using * characters.
    Each * represents one occurrence of that score.
    """
    print("\nScore Distribution Histogram")
    print("(Each * represents one student)\n")
    
    # Draw histogram bars for each score
    for score in range(11):
        # Format score with 2 digits for alignment
        print(f"{score:2d} | ", end="")
        
        # Print stars for each count
        for i in range(counts[score]):
            print("*", end="")
        print()  # New line after each score
    
    # Print x-axis legend
    print("   +", "-" * 40)
    print("    Score Frequency")

def main():
    # Read scores from file
    scores = read_scores()
    
    if scores is not None:
        # Count occurrences of each score
        counts = count_scores(scores)
        
        # Draw the histogram
        draw_histogram(counts)
        
        # Print total number of scores
        total_scores = sum(counts)
        print(f"\nTotal number of scores: {total_scores}")

# Run the program
if __name__ == "__main__":
    main()