def find_result_frequency():
    file_input = open("input.txt", "r")
    current_frequency = 0
    for line in file_input:
        current_frequency = current_frequency + int(line)
    return current_frequency


def find_twice_matched_frequency():
    file_input = open("input.txt", "r")
    current_frequency = 0
    frequency_set = {current_frequency}

    while True:
        for line in file_input:
            current_frequency = current_frequency + int(line)
            if current_frequency in frequency_set:
                print(current_frequency, "matched twice")
                return current_frequency
            else:
                frequency_set.add(current_frequency)
        file_input.seek(0)


find_twice_matched_frequency()
