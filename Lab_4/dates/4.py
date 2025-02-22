from datetime import datetime

# Define two dates
date1 = datetime(2025, 2, 22, 12, 0, 0)  # Example date 1
date2 = datetime(2025, 3, 3, 5, 0, 0)  # Example date 2

# Calculate difference in seconds
difference = (date2 - date1).total_seconds()

print(f"Difference between the two dates in seconds: {difference} seconds")