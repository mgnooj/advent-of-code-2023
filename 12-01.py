file = "day1.txt"
with open(file) as f:
    text = f.read()
input = [x for x in text.split('\n') if x != ""]

def part1():
    valid_digits = [str(x) for x in range(0, 10)]
    calibration_values = []
    for string in input:
        digits = [y for y in filter(lambda x: x in valid_digits, string)]
        calibration_value = int(digits[0] + digits[-1])
        calibration_values.append(calibration_value)
    return sum(calibration_values)

def part2():
    valid_digits = [str(x) for x in range(0, 10)]
    digit_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lookup_table = {digit_strings[i] : valid_digits[i] for i in range(len(valid_digits))}
    calibration_values = []
    for string in input:
        most_sig_digit = {}
        least_sig_digit = {}
        for digit in digit_strings:
            first_appearance = string.find(digit)
            last_appearance = string.rfind(digit)
            if first_appearance != -1 and (most_sig_digit == {} or most_sig_digit.get("idx") > first_appearance):
                most_sig_digit = {"num": lookup_table.get(digit), "idx": first_appearance}
            if last_appearance != -1 and (least_sig_digit == {} or least_sig_digit.get("idx") < last_appearance):
                least_sig_digit = {"num": lookup_table.get(digit), "idx": last_appearance}
        digits = [{"num": y, "idx": idx} for idx, y in [(index, char) for index, char in enumerate(string) if char in valid_digits]]
        if most_sig_digit == {} or most_sig_digit.get("idx") > digits[0].get("idx"):
            most_sig_digit = digits[0]
        if least_sig_digit == {} or least_sig_digit.get("idx") < digits[-1].get("idx"):
            least_sig_digit = digits[-1]
        calibration_value = int(most_sig_digit.get("num") + least_sig_digit.get("num"))
        calibration_values.append(calibration_value)
    return sum(calibration_values)