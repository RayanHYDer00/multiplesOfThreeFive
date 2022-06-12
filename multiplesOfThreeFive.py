# Program for calculating the sum of the natural numbers that are multiples of 3 or 5 depending on the user input
def check_multiples(num):
    total = 0
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            total += i
            print(f"The selected natural number of the multiple of 3 and 5 are: ", i)
    print(f"The sum of the multiple of 3 and 5 below {num} is: ", total)

# Press the green button in the gutter to run the script.
check_multiples(int(input("Please enter a number for calculating the Sum of multiples of 3 or 5: ")))

