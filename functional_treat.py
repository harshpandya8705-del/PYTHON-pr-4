"""
Functional Treat: Data Analyzer and Transformer
A menu-driven Python project demonstrating functions and list operations.
"""

dataset = []
dataset_summary = {"count": 0, "total": 0, "average": 0.0}


def show_menu():
    """Display the application's main menu."""
    print("\n" + "=" * 58)
    print("       FUNCTIONAL TREAT - DATA ANALYZER & TRANSFORMER")
    print("=" * 58)
    print("1. Input data (1D or 2D list)")
    print("2. Display data and built-in function summary")
    print("3. Calculate factorial / Fibonacci (recursion)")
    print("4. Filter data using a lambda threshold")
    print("5. Sort data (in-place or new sorted list)")
    print("6. Display dataset statistics (multiple return values)")
    print("7. Show dataset summary using **kwargs")
    print("8. Flatten and analyze a 2D list")
    print("9. Exit")
    print("-" * 58)


def read_numbers(prompt):
    """Read space-separated numeric values and return them as a list of floats/ints."""
    raw = input(prompt).strip()
    if not raw:
        raise ValueError("Please enter at least one number.")
    values = []
    for token in raw.split():
        number = float(token)
        values.append(int(number) if number.is_integer() else number)
    return values


def input_data():
    """Allow the user to enter a one-dimensional or two-dimensional list."""
    global dataset
    print("\nChoose input type:\n1. 1D list\n2. 2D list (rows separated by ';')")
    choice = input("Your choice: ").strip()
    if choice == "1":
        dataset = read_numbers("Enter numbers separated by spaces: ")
    elif choice == "2":
        raw = input("Enter rows separated by ';' and values by spaces: ").strip()
        rows = []
        for row_text in raw.split(";"):
            if row_text.strip():
                row = []
                for token in row_text.split():
                    number = float(token)
                    row.append(int(number) if number.is_integer() else number)
                if row:
                    rows.append(row)
        if not rows:
            raise ValueError("Please enter at least one non-empty row.")
        dataset = rows
    else:
        print("Invalid input type.")
        return
    refresh_global_summary()
    print("Data stored successfully.")
    display_data()


def flatten_data(data):
    """Return a flat list of values from either a 1D or 2D list."""
    if data and isinstance(data[0], list):
        return [value for row in data for value in row]
    return list(data)


def refresh_global_summary():
    """Update the module-level summary dictionary using the global keyword."""
    global dataset_summary
    values = flatten_data(dataset)
    dataset_summary = {
        "count": len(values),
        "total": sum(values) if values else 0,
        "average": (sum(values) / len(values)) if values else 0.0,
    }


def display_data():
    """Print a 1D list or a formatted 2D grid."""
    if not dataset:
        print("No data available. Please input data first.")
        return
    print("\nCurrent dataset:")
    if isinstance(dataset[0], list):
        for row in dataset:
            print("  " + " | ".join(f"{value:g}" if isinstance(value, float) else str(value) for value in row))
    else:
        print(" ", dataset)


def get_basic_summary(data):
    """Use built-in functions to calculate basic dataset characteristics."""
    values = flatten_data(data)
    if not values:
        return None
    return {
        "Total elements": len(values),  # len()
        "Minimum": min(values),         # min()
        "Maximum": max(values),         # max()
        "Sum": sum(values),              # sum()
        "Average": sum(values) / len(values),
    }


def calculate_average(*numbers):
    """Accept any number of positional arguments and return their average."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def summarize_dataset(**details):
    """Accept keyword arguments and print a flexible dataset summary."""
    print("\nDataset summary (**kwargs):")
    for key, value in details.items():
        print(f"- {key.replace('_', ' ').title()}: {value}")


def factorial(n):
    """Recursively calculate n! for a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Recursively return the first n Fibonacci numbers."""
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")
    if n <= 1:
        return [0] if n == 1 else []
    sequence = fibonacci(n - 1)
    next_value = sequence[-1] + (sequence[-2] if len(sequence) > 1 else 0)
    return sequence + [next_value]


def filter_by_threshold(data, threshold, keep_above=True):
    """Use lambda with filter() to keep values above or below a threshold."""
    values = flatten_data(data)
    condition = (lambda value: value >= threshold) if keep_above else (lambda value: value <= threshold)
    return list(filter(condition, values))


def transform_values(data):
    """Use map() and lambda to return the squares of all values."""
    return list(map(lambda value: value ** 2, flatten_data(data)))


def sort_data(data, descending=False, in_place=False):
    """Sort a list; demonstrate list.sort() versus sorted()."""
    values = flatten_data(data)
    if in_place:
        values.sort(reverse=descending)  # sort() changes the list it is called on
        return values
    return sorted(values, reverse=descending)  # sorted() returns a new list


def dataset_statistics(data):
    """Return minimum, maximum, sum and average as four separate values."""
    values = flatten_data(data)
    if not values:
        raise ValueError("No data available.")
    return min(values), max(values), sum(values), calculate_average(*values)


def display_summary():
    """Display built-in statistics and demonstrate *args."""
    if not dataset:
        print("Please input data first.")
        return
    summary = get_basic_summary(dataset)
    print("\nData Summary (built-in functions):")
    for key, value in summary.items():
        print(f"- {key}: {value:.2f}" if isinstance(value, float) else f"- {key}: {value}")
    print(f"- Average via *args function: {calculate_average(*flatten_data(dataset)):.2f}")


def main():
    """Run the menu-driven Data Analyzer and Transformer."""
    print("Welcome to Functional Treat!")
    while True:
        show_menu()
        choice = input("Please enter your choice: ").strip()
        try:
            if choice == "1":
                input_data()
            elif choice == "2":
                display_data()
                display_summary()
            elif choice == "3":
                task = input("Enter F for factorial or B for Fibonacci: ").strip().lower()
                number = int(input("Enter a non-negative integer: "))
                if task == "f":
                    print(f"Factorial of {number} = {factorial(number)}")
                elif task == "b":
                    print(f"First {number} Fibonacci terms: {fibonacci(number)}")
                else:
                    print("Invalid recursion option.")
            elif choice == "4":
                if not dataset:
                    print("Please input data first.")
                    continue
                threshold = float(input("Enter threshold: "))
                direction = input("Keep values A)bove/equal or B)elow/equal? ").strip().lower()
                result = filter_by_threshold(dataset, threshold, direction != "b")
                print("Filtered values:", result)
                print("Squared values using map() + lambda:", transform_values(dataset))
            elif choice == "5":
                if not dataset:
                    print("Please input data first.")
                    continue
                direction = input("A)scending or D)escending? ").strip().lower()
                method = input("I)n-place sort() or N)ew sorted() list? ").strip().lower()
                result = sort_data(dataset, direction == "d", method == "i")
                print("Sorted values:", result)
            elif choice == "6":
                if not dataset:
                    print("Please input data first.")
                    continue
                minimum, maximum, total, average = dataset_statistics(dataset)
                print("\nDataset Statistics:")
                print(f"- Minimum: {minimum}")
                print(f"- Maximum: {maximum}")
                print(f"- Sum: {total}")
                print(f"- Average: {average:.2f}")
            elif choice == "7":
                if not dataset:
                    print("Please input data first.")
                    continue
                values = flatten_data(dataset)
                summarize_dataset(
                    total_elements=len(values),
                    minimum=min(values),
                    maximum=max(values),
                    sum_of_values=sum(values),
                    average=calculate_average(*values),
                    data_type="2D list" if isinstance(dataset[0], list) else "1D list",
                )
                print("Global summary:", dataset_summary)
            elif choice == "8":
                if not dataset:
                    print("Please input data first.")
                    continue
                if isinstance(dataset[0], list):
                    print("Flattened 2D data:", flatten_data(dataset))
                else:
                    print("Current input is 1D. Enter 2D data using option 1 to use this feature.")
            elif choice == "9":
                print("Thank you for using Functional Treat. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-9.")
        except (ValueError, RecursionError) as error:
            print("Input error:", error)


if __name__ == "__main__":
    main()
