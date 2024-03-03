import pandas as pd

def count_books_from_sales_data(sales_file):
    sales_data = pd.read_csv(sales_file)
    total_books = sales_data['Book Title'].nunique()
    return total_books

# Example usage:
sales_file = 'sales_data.csv'
total_books = count_books_from_sales_data(sales_file)
print("Total books from sales data:", total_books)
