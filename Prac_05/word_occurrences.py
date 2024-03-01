"""
Word Occurrences Counter
Estimated time: 30 minutes
"""


def count_word_occurrences(text):
    word_counts = {}
    words = text.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def print_word_occurrences(word_counts):
    max_word_length = max(len(word) for word in word_counts.keys())

    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


def main():
    user_input = input("Enter a string: ")
    word_counts = count_word_occurrences(user_input)
    print("Word occurrences:")
    print_word_occurrences(word_counts)


if __name__ == "__main__":
    main()
