"""
Project: File Text Analytics Tool
---------------------------------
Reads a text file, cleans the text using regex, 
counts word frequencies using collections.Counter, 
and displays top N frequent words.

Time Complexity: O(n) — where n is number of words in the file
Space Complexity: O(k) — where k is number of unique words
"""

import re
from collections import Counter

def analyze_file(filename, top_n=10):
    """Analyze word frequency in a given text file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()

        # Clean text: remove punctuation and special chars
        words = re.findall(r'\b[a-z]+\b', text)

        # Count word frequency
        word_counts = Counter(words)

        # Display results
        print(f"\nTop {top_n} most frequent words in '{filename}':\n")
        for word, count in word_counts.most_common(top_n):
            print(f"{word:<15} : {count}")

    except FileNotFoundError:
        print("⚠️ File not found. Please check the filename and try again.")

# Example usage
if __name__ == "__main__":
    analyze_file("sample.txt", top_n=10)
