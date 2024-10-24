# Based on J.M.E. Baudot's August 21, 1888 Patent No. 388,244
# Use '+' = 0, '-' = 1 since 'If the cipher and key are the same the result is +.' for this
# Rather than '+' = 1 and using xnor logic, since all input and output is either ASCII or +/- encoded

# From the patent, unsure of the 4 after 'Z', though the last '-----' is space. Substituting symbols
# Also using ASCII so 'e' represents the 'E' with an accent
ascii_to_baudot_map = {'A': '+----', 'B': '--++-', 'C': '+-++-', 'D': '++++-', 'E': '-+---', 'e': '++---',
                       'F': '-+++-', 'G': '-+-+-', 'H': '++-+-', 'I': '-++--', 'J': '+--+-', 'K': '+--++',
                       'L': '++-++', 'M': '-+-++', 'N': '-++++', 'O': '+++--', 'P': '+++++', 'Q': '+-+++',
                       'R': '--+++', 'S': '--+-+', 'T': '+-+-+', 'U': '+-+--', 'V': '+++-+', 'W': '-++-+',
                       'X': '-+--+', 'Y': '--+--', 'Z': '++--+', '~': '+---+', '*': '---++', '|': '---+-',
                       '_': '----+', ' ': '-----'}

baudot_to_ascii_map = {v: k for k, v in ascii_to_baudot_map.items()}

test_input_baudot = ['+-+-+', '+++++', '++++-', '--+-+', '-++--', '--+--', '-+---', '+-++-', '+++++', '+++--',
                     '++---', '---+-', '+++--', '---+-', '++-++', '--+++', '+++++', '-++--', '+++--', '+-+++',
                     '++++-', '-+-++', '-++--', '++-+-', '++---', '+-++-', '+----', '-+--+', '+---+', '+---+',
                     '+++-+', '-++-+', '--++-', '-----', '++-++', '--+++', '--+-+', '--+--', '--+++', '---++',
                     '--++-', '--+--', '--++-', '+-++-', '--++-', '+++--', '++---', '++--+', '-+++-', '+-+--',
                     '++--+', '-----', '--++-']
# The original challence listed the key as "CUBAN MISSLE CRISIS" but it seems the spaces were erroneous and
# the misspelling of "MISSILE" was unintentional or intentionally misleading.
#test_key_ascii = "CUBAN MISSLE CRISIS"
test_key_ascii = "CUBANMISSILECRISIS"

def baudot_to_bin(baudot):
    binary_code = []
    for b in baudot:
        num = 0
        for symbol in b:
            num = num << 1
            if symbol == '-':
                num = num | 0b1
        binary_code.append(num)
    return binary_code

def bin_to_baudot(binary_code):
    baudot = []
    for num in binary_code:
        word = ''
        for i in range(5):
            if (num & 0b10000) == 0:
                word = word + '+'
            else:
                word = word + '-'
            num = num << 1
        baudot.append(word)
    return baudot

def baudot_to_ascii(baudot):
    ascii_out = ''
    for symbol in baudot:
        if symbol in baudot_to_ascii_map.keys():
            ascii_out = ascii_out + baudot_to_ascii_map[symbol]
        else:
            ascii_out = ascii_out + '?'
    return ascii_out

def ascii_to_baudot(ascii_in):
    baudot = []
    for c in ascii_in:
        if c in ascii_to_baudot_map.keys():
            baudot.append(ascii_to_baudot_map[c])
        else:
            baudot.append('?????')
    return baudot

def print_bin(binary_array):
    for num in binary_array:
        print(format(num, '05b'))

def xor_crypt(text, key):
    cryptex = []
    i = 0
    for sym in text:
        cryptex.append(sym ^ key[i])
        i = (i + 1) % len(key)
    return cryptex

#b = baudot_to_bin(test_input_baudot)
#print_bin(b)

#b = bin_to_baudot(b)
#print(b)

#a = baudot_to_ascii(b)
#print(a)

test_key_baudot = ascii_to_baudot(test_key_ascii)
#print(test_key_baudot)

test_key = baudot_to_bin(test_key_baudot)
test_input = baudot_to_bin(test_input_baudot)

result = xor_crypt(test_input, test_key)
result_baudot = bin_to_baudot(result)
result_ascii = baudot_to_ascii(result_baudot)

print(result_ascii)

