# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    shape = ""

    for i in range(1, n + 1):

        if i == 1 or i == n:

            shape += n * '*' + '\n'

        else:

            shape += '*' + ' ' * (n - 2) + '*' + '\n'

    return(shape.strip())

# print(hollow_square(2))

# 1
# 12
# 123
# 1234
def number_pattern(n):

    pattern = ""

    for i in range(1, n + 1):

        for j in range(1, i + 1):

            pattern += str(j)
            
        pattern += '\n'

    return pattern.strip()

# print(number_pattern(4))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):

    sum = 0

    for i in range(1, n + 1):
        
        sum += int(i)

    return sum

# print(sum_of_natural_numbers(5))

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    
    pyramid = ""
    
    for i in range(1, n + 1):

        spaces = ' ' * (n - i)
        stars = '*' * (1 + 2 * (i - 1))

        pyramid += spaces + stars + '\n'

    return pyramid.rstrip()

# print(centered_star_pyramid(4))