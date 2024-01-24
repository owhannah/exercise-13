# Print the multiplication table 

def print_multiplication_table(number, table_width=20, column_width=7):

    # Print the header
    print(f"\nMultiplication Table for {number}:\n")
    print(f"+{'~' * (table_width - 2)}+")

    # Print the column headers
    print(f"|{'Multiplicand':^{column_width}}|{'Product':^{column_width}}*")
    print(f"+{'~' * (table_width - 2)}+")

    # Print the multiplication table
    for i in range(1, 11):
        product = number * i
        print(f":{number:^{column_width}}:{product:^{column_width}}:")

    # Print the table bottom border
    print(f"+{'~' * (table_width - 2)}+\n")

# Print multiplication tables from 1 to 10 with custom formatting
for multiplier in range(1, 11):
    print_multiplication_table(multiplier)