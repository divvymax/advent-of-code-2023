def determine_calibration_value(s: str) -> int:
    ints = [c for c in s if c in "0123456789"]
    return int(ints[0] + ints[-1])


TEST_DOCUMENTS = {"1abc2": 12, "pqr3stu8vwx": 38, "a1b2c3d4e5f": 15, "treb7uchet": 77}

TEST_CALIBRATIONS = {k: determine_calibration_value(k) for k in TEST_DOCUMENTS.keys()}

assert all(v == TEST_CALIBRATIONS[k] for k, v in TEST_DOCUMENTS.items())
assert sum(TEST_CALIBRATIONS.values()) == 142

day01_input = open("day01.txt", "r").readlines()

print(sum(determine_calibration_value(l) for l in day01_input))

word_to_number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def convert_words_to_numbers(s: str) -> str:
    for i in range(len(s)):
        if s[i] in "0123456789":
            break
        found = False
        for k in word_to_number_map.keys():
            l = len(k)
            if s[i:i+l] == k:
                s = s[:i] + str(word_to_number_map[k]) + s[i+l:]
                found = True
                break
        if found:
            break

    for i in reversed(range(len(s))):
        if s[i] in "0123456789":
            break
        found = False
        for k in word_to_number_map.keys():
            l = len(k)
            if s[i:i+l] == k:
                s = s[:i] + str(word_to_number_map[k]) + s[i+l:]
                found = True
                break
        if found:
            break

    return s


TEST_DOCUMENTS = {
    "two1nine": 29,
    "eightwothree": 83,
    "abcone2threexyz": 13,
    "xtwone3four": 24,
    "4nineeightseven2": 42,
    "zoneight234": 14,
    "7pqrstsixteen": 76,
}

TEST_CALIBRATIONS = {
    k: determine_calibration_value(convert_words_to_numbers(k))
    for k in TEST_DOCUMENTS.keys()
}

assert all(v == TEST_CALIBRATIONS[k] for k, v in TEST_DOCUMENTS.items())
assert sum(TEST_CALIBRATIONS.values()) == 281

print(sum(determine_calibration_value(convert_words_to_numbers(l)) for l in day01_input))