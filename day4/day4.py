import operator

from parse import *


def read_input(name_of_input_file):
    file_input = open(name_of_input_file, "r")
    return file_input


def build_timetable(file_input):
    timetable = []
    for line in file_input:
        timetable.append(line)
    timetable.sort()
    return timetable


def get_current_id(entry):
    result = parse("{}#{id} begins shift", entry)
    return int(result.named['id'])


def get_minutes(entry):
    result = parse("{}:{minute}]{}", entry)
    return int(result.named['minute'])


def get_minutes_distribution():
    minutes = dict()
    for minute in range(0, 60):
        minutes[minute] = 0
    return minutes


def get_key_with_max_value(dictionary):
    return max(dictionary.items(), key=operator.itemgetter(1))[0]


def get_max_value(dictionary):
    return max(dictionary.items(), key=operator.itemgetter(1))[1]


def first_strategy(amount_sleep, minutes_asleep):
    max_sleeping_id = get_key_with_max_value(amount_sleep)
    max_sleeping_id_sleeping_minutes = minutes_asleep[max_sleeping_id]
    max_sleeping_minute = get_key_with_max_value(max_sleeping_id_sleeping_minutes)
    print("Part 1:")
    print(max_sleeping_id * max_sleeping_minute)


def second_strategy(minutes_asleep):
    max_sleeping_minute_times = 0
    max_sleeping_id = 0
    max_sleeping_minute = 0
    for guard_id in minutes_asleep.keys():
        for minute in minutes_asleep[guard_id].keys():
            if minutes_asleep[guard_id][minute] > max_sleeping_minute_times:
                max_sleeping_minute_times = minutes_asleep[guard_id][minute]
                max_sleeping_id = guard_id
                max_sleeping_minute = minute
    print("Part 1:")
    print(max_sleeping_id * max_sleeping_minute)


def find_most_asleep_guard(file):
    timetable = build_timetable(file)
    amount_sleep = dict()
    current_id = 0
    start_sleeping = 0
    minutes_asleep = dict()
    for entry in timetable:
        if "begins shift" in entry:
            current_id = get_current_id(entry)
            if current_id not in amount_sleep.keys():
                amount_sleep[current_id] = 0
                minutes_asleep[current_id] = get_minutes_distribution()
        if "falls asleep" in entry:
            start_sleeping = get_minutes(entry)
        if "wakes up" in entry:
            end_sleeping = get_minutes(entry)
            amount_sleep[current_id] += (end_sleeping - start_sleeping)
            for minute in range(start_sleeping, end_sleeping):
                minutes_asleep[current_id][minute] += 1

    first_strategy(amount_sleep, minutes_asleep)
    second_strategy(minutes_asleep)


find_most_asleep_guard(read_input("input.txt"))
