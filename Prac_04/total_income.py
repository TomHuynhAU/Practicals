def print_report(incomes, num_of_months):
    """Print income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_of_months = int(input("How many months? "))

    for month in range(1, num_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes, num_of_months)


if __name__ == '__main__':
    main()
