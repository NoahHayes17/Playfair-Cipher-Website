GRID_SIZE = 5

#without 'j'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def build_matrix(key):
    # remove duplicates while maintaining order
    key = ''.join(sorted(set(key), key=key.index)) 
    
    matrix = []
    for char in key + ''.join(alphabet):
        if char not in matrix and char != 'j': 
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def encrypt_message(message, matrix):
    message = prepare_message(message)
    encrypted = ""
    i = 0
    while i < len(message):
        if i == len(message) - 1:
            pair = message[i] + 'x' 
        else:
            pair = message[i] + message[i + 1]
        
        if pair[0] == pair[1]:
            pair = pair[0] + 'x' 
        
        encrypted += encrypt_pair(pair[0], pair[1], matrix)
        i += 2
    return encrypted.upper()

def prepare_message(message):
    message = ''.join([c.lower() for c in message if c.isalpha()]).replace('j', 'i')
    if len(message) % 2 != 0:
        message += 'x'
    return message


def encrypt_pair(a, b, matrix):
    row_a, col_a = find_position(a, matrix)
    row_b, col_b = find_position(b, matrix)

    if row_a is None or row_b is None:
        raise ValueError(f"Letters '{a}' or '{b}' not found in the matrix.")
    
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]


def find_position(letter, matrix):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return None  # this should never happen if alphabet is complete
