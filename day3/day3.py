from numpy import *
from parse import *

EMPTY_INCH = 0
TAKEN_INCH = 1
OVERLAPPED_INCH = 2


def read_file(input_file):
    file = open(input_file, "r")
    return file


def get_fabric_matrix(file):
    fabric_piece = empty([1000, 1000])
    for line in file:
        result = parse("#{id} @ {left},{top}: {width}x{height}", line)
        left = int(result.named['left'])
        top = int(result.named['top'])
        width = int(result.named['width'])
        height = int(result.named['height'])

        for x in range(top, top + height):
            for y in range(left, left + width):
                if fabric_piece[x][y] == EMPTY_INCH:
                    fabric_piece[x][y] = TAKEN_INCH
                elif fabric_piece[x][y] == TAKEN_INCH:
                    fabric_piece[x][y] = OVERLAPPED_INCH

    return fabric_piece


def count_overlapping_inches(file):
    fabric_piece = get_fabric_matrix(file)
    return count_nonzero(fabric_piece == OVERLAPPED_INCH)


def find_not_overlapping_claim(file):
    fabric_piece = get_fabric_matrix(file)
    file.seek(0)
    for line in file:
        result = parse("#{id} @ {left},{top}: {width}x{height}", line)
        left = int(result.named['left'])
        top = int(result.named['top'])
        width = int(result.named['width'])
        height = int(result.named['height'])
        claim_id = int(result.named['id'])

        is_overlapped = False

        for x in range(top, top + height):
            for y in range(left, left + width):
                if fabric_piece[x][y] == OVERLAPPED_INCH:
                    is_overlapped = True

        if not is_overlapped:
            return claim_id


print(find_not_overlapping_claim(read_file("input.txt")))
