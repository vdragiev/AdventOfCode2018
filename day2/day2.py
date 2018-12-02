def find_checksum_candidate_boxes(name_of_input_file):
    file_input = open(name_of_input_file, "r")
    id_two_letters = 0
    id_three_letters = 0

    for line in file_input:
        line_dictionary = dict()
        for letter in line:
            if letter not in line_dictionary:
                line_dictionary[letter] = 1
            else:
                line_dictionary[letter] = line_dictionary[letter] + 1

        if 2 in line_dictionary.values():
            id_two_letters = id_two_letters + 1

        if 3 in line_dictionary.values():
            id_three_letters = id_three_letters + 1

    return id_two_letters * id_three_letters


print(find_checksum_candidate_boxes("input.txt"))



