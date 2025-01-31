"""7.Python program that accepts a sequence of comma-separated words as input and 
returns the words sorted in alphabetical order."""
def sort_words(string):
    return ','.join(sorted(string.split(',')))
    
print(sort_words('banana,apple,grape,orange'))

""" 6.Python program that takes two digits, M and N, as inputs and generates a two-dimensional array. The value at 
the i-th row and j-th column of the array should be i*j."""
def create_matrix(M, N):
    return [[i * j for j in range(N)] for i in range(M)]

create_matrix(4,3)


# 5.Calculate Q Values from D 
import math
def calculate_q_values(d_values):
    C = 50
    H = 30
    value = []
    items = [float(x) for x in d_values.split(',')]
    for D in items:
        Q = round(math.sqrt((2 * C * D) / H))
        value.append(str(Q))
    return ','.join(value)

calculate_q_values('5,50,500')


""" 8.Python program that takes a 
sequence of lines as input and returns each line capitalized."""
def capitalize_lines(lines):
    return [line.upper() for line in lines]
    
my_line = ['My Love', 'Sports are fun!', 'Games can be played with two 2 players']
print(capitalize_lines(my_line))


"""9.Python program that accepts a sequence of whitespace-separated words as input and returns 
them sorted alphabetically with duplicates removed."""
def unique_sorted_words(string):
    return ' '.join(sorted(string.split(' ')))
    
print(unique_sorted_words('dog apple banana cherry kiwi'))


""" 10.Python program that accepts
 a sequence of comma-separated 4-digit binary numbers as 
 input and checks if they are divisible by 5. 
 The valid numbers should be returned in a comma-separated sequence."""
def binary_divisible_by_5(binaries):
    return ‘,’.join([b for b in binaries.split(‘,’) if int(b, 2) % 5 == 0])
    
binaries = ‘1101,1010,1111,1001’
print(binary_divisible_by_5(binaries))
