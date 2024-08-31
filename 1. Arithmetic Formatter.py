def arithmetic_arranger(problems, show_answers=False):
    # check the lengths of parameter
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = []
    numbers = []

    for problem in problems:
        array = problem.split()
        operators.append(array[1])
        numbers.append(array[0])
        numbers.append(array[2])

    # check for invalid operators
    for operator in operators:
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    # check for non-digits and operand length
    for number in numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(number) > 4:
            return "Error: Numbers cannot be more than four digits."

    answers = []
    top_row = ''
    bottom_row = ''
    answer_row = ''
    dashes = ''

    for i in range(0, len(numbers), 2):
        num1 = int(numbers[i])
        num2 = int(numbers[i+1])
        operator = operators[i // 2]
        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        answers.append(result)

        # formatting row
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        top_row += numbers[i].rjust(space_width)
        bottom_row += operator + numbers[i+1].rjust(space_width - 1)
        dashes += '-' * space_width

        # spacing between problems
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4

    # formatting answer row
    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]), len(numbers[2 * i + 1])) + 2
        answer_row += str(answers[i]).rjust(space_width)

        # spacing between answer
        if i != len(answers) - 1:
            answer_row += ' ' * 4

    # final arrangement and return
    if show_answers:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, answer_row))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))

    return arranged_problems

print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')