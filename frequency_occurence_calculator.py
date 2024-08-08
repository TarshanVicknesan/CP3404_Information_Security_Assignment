"""From reach row having 7 letters, now each collumn has each of its letter occurences calculated"""
import csv
from collections import Counter
import re


def main():
    ciphertext = input("Ciphertext: ")
    key_length = int(input("Key length: "))
    columns = create_columns(ciphertext, key_length)
    column_letter_counts = [count_letter_occurrences(column) for column in columns]
    write_column_counts_to_csv(column_letter_counts, 'column_letter_counts.csv')
    print("Saved to 'column_letter_counts.csv'.")


def create_columns(ciphertext, key_length):
    """Divide the ciphertext into columns based on the key length."""
    # Initialize empty columns
    columns = ['' for _ in range(key_length)]

    # Distribute letters into columns
    for i, char in enumerate(ciphertext):
        column_index = i % key_length
        columns[column_index] += char

    return columns


def count_letter_occurrences(text):
    """Count occurrences of each letter in the text."""
    letters = re.findall(r'[a-zA-Z]', text.lower())
    return Counter(letters)


def write_column_counts_to_csv(column_letter_counts, filename):
    """Save letter counts for each column to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Column'] + [chr(i) for i in range(ord('a'), ord('z') + 1)])

        # Write counts for each column
        for index, letter_counts in enumerate(column_letter_counts):
            row = [f'Column {index + 1}'] + [letter_counts.get(chr(i), 0) for i in range(ord('a'), ord('z') + 1)]
            writer.writerow(row)


main()
