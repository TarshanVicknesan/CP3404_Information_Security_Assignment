"""Splits paragraph into rows of 7 letters"""
import csv


def main():
    paragraph = input("Ciphertext: ")
    max_length = int(input("Row length: "))
    chunks = chunk_paragraph(paragraph, max_length)
    write_chunks_to_csv(chunks, 'output.csv')
    print("Saved to 'output.csv'.")


def chunk_paragraph(paragraph, max_length):
    """Divide a paragraph into chunks of specified length."""
    return [paragraph[i:i + max_length] for i in range(0, len(paragraph), max_length)]


def write_chunks_to_csv(chunks, filename):
    """Save chunks to a CSV file with each letter in its own cell."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for chunk in chunks:
            writer.writerow(list(chunk))


main()
