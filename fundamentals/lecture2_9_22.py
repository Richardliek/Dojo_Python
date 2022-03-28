def greater_than_second(numbers):
    if len(numbers) < 2:
        return False

    second_value = numbers[1]
    output = []

    for number in numbers:
        if number > second_value:
            output.append(number)

        return output

greater_than_second([2,3,4,32,4])