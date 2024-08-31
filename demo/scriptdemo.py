
def calculate_sum_of_natural_numbers(n):
    return sum(range(1, n + 1))

def main():
    number_of_terms = 10
    result = calculate_sum_of_natural_numbers(number_of_terms)
    print(f"The sum of the first {number_of_terms} natural numbers is: {result}")

if __name__ == "__main__":
    main()
