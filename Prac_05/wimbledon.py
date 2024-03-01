"""
Wimbledon Champions
"""


def read_csv_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            line = line.strip().split(",")
            data.append(line)
    return data


def get_champions(data):
    champions_count = {}
    for row in data:
        champion = row[2]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
    return champions_count


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    sorted_countries = sorted(countries)
    return ", ".join(sorted_countries)


def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_csv_file(filename)

    champions_count = get_champions(wimbledon_data)
    print("Wimbledon Champions:")
    for champion, count in champions_count.items():
        print(f"{champion} {count}")

    countries = get_countries(wimbledon_data)
    print("\nThese countries have won Wimbledon:")
    print(countries)


if __name__ == "__main__":
    main()
