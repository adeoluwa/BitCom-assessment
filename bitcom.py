# import psycopg2
# import psycopg2
from collections import Counter
import random

# Question number 1, Mean color problem
colors = {
     'MONDAY': 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'TUESDAY': 'ASH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE',
    'WEDNESDAY': 'GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE',
    'THURSDAY': 'BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN',
    'FRIDAY': 'GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE'
}

all_colors = [color.strip() for day_colors in colors.values() for color in day_colors.split(',')]

color_counts = Counter(all_colors)

mean_color = color_counts.most_common(1)[0][0]

print(f'The mean color of the shirst worn by workers for the week is : {mean_color}')
# The Mean color is BLUE

# .................
# Question Number 2
most_worn_color = color_counts.most_common(1)[0][0]
print(f"The color mostly worn throughout the week is:{most_worn_color}") 
# The most worn color is BLUE

# Question Number 3 
color_values = {color: sum(ord(char.upper()) - 64 for char in color) for color in all_colors}

sorted_colors = sorted(all_colors, key=lambda x: color_values[x])

median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index] if len(sorted_colors) % 2 != 0 else (sorted_colors[median_index - 1] + sorted_colors[median_index]) /2

print(f"The median color is: {median_color}")
# Median Color is Green

# Bonus Question 4
mean_value = sum(color_values.values()) / len(color_values)

variance = sum((value -mean_value) ** 2 for value in color_values.values()) / len(color_values)

print(f"The Variance of the colors is: {variance}")
# The Variance of the colors is: 357.4166666666667


#Bonus Question 5
count_of_red = Counter(all_colors)['RED']
total_colors = len(all_colors)
red_probability = count_of_red / total_colors
print(f"The probability ofchosing the color red at random is: {red_probability}")
# The probability ofchosing the color red at random is: 0.09473684210526316

# Question Number 6: Saving to Postgres Database
# conn = psycopg2.connect(
#     dbname = "bfbsmlgo",
#     user = "bfbsmlgo",
#     password = "tf4LrfSSQ-Z1cc0bhgFDgYjTXeAC3WcG",
#     host = "postgres://bfbsmlgo:tf4LrfSSQ-Z1cc0bhgFDgYjTXeAC3WcG@bubble.db.elephantsql.com/bfbsmlgo"
# )
# API KEY: 685c8954-fff7-4092-b14e-19830ee17f28
# cur = conn.cursor()

# Inserting color frequencies into the database
# for color, frequency in color_counts.items():
#     cur.execute("INSERT INTO color_frequencies (color, frequency)")

# commit changes and closing connection
# conn.commit()
# cur.close()
# conn.close()

# print("Color frequencies saved to the database")

#Question  Number 8
binary_number = ''.join(random.choice(['0','1']) for _ in range(4))

decimal_number = int(binary_number, 2)

print(f"Generated Binary Number: {binary_number}")
# Generated Binary Number: 1111

print(f"Equivalent Decimal Number: {decimal_number}")
#Equivalent Decimal Number: 15


#Question Number 9
def fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    return fibonacci_sequence

fib_sequence = fibonacci(50)
fib_sum = sum(fib_sequence)

print(f"The sum of the first 50 FIbonacci numbers is: {fib_sum}")
# The sum of the first 50 FIbonacci numbers is: 20365011073