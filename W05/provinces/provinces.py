def main():
    province_list = read_list("provinces.txt")

    print(province_list)


def read_list(filename):
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list;


if __name__ == "__main__":
    main()
