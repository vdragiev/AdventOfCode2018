def get_ids_from_file(file_input):
    ids = []
    for line in file_input:
        ids.append(line.strip())
    return ids


def differ_one_character(id, compared_id):
    difference_counter = 0
    for index in range(len(id)):
        if id[index] != compared_id[index]:
            difference_counter += 1
            if difference_counter > 1:
                return False
    return difference_counter == 1


def common_letters_id(id, compared_id):
    resulting_common_id = ""
    for index in range(len(id)):
        if id[index] == compared_id[index]:
            resulting_common_id += id[index]
    return resulting_common_id


def find_common_id(input_file_name):
    file_input = open(input_file_name, "r")
    collection_of_ids = get_ids_from_file(file_input)
    for id in collection_of_ids:
        for compared_id in collection_of_ids:
            if differ_one_character(id, compared_id):
                return common_letters_id(id, compared_id)


print(find_common_id("input.txt"))
