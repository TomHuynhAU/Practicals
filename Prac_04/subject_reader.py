FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details."""
    for subject in data:
        code, lecturer, num_students = subject
        print(f"{code} is taught by {lecturer} and has {num_students} students")


if __name__ == '__main__':
    main()
