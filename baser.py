def convert_tobin(input_string):
    #input_string = "".join(input_string.split())
    binary_list = [bin(ord(x)) for x in input_string]
    corrected = []
    for binary in binary_list:
        corrected.append(("0" * (8 - len(binary[2:]))) + binary[2:])
    return "".join(corrected)

def convert_to6(bin_string):
    start = 0
    end = 6
    new_bin = []
    while start < len(bin_string):
        new_bin.append(bin_string[start:end])
        start = end
        end += 6
    #print(new_bin)
    incomplete_binary = 0
    if len(new_bin[-1]) != 6:
        zero_to_add = 6 - len(new_bin[-1])
        incomplete_binary = new_bin[-1]
        new_bin.pop()
        new_bin.append(incomplete_binary + ("0"*zero_to_add))
    #print(new_bin)
    return new_bin

def padding(thisinput):
    counter = 0
    initial_length = len(thisinput)
    if initial_length % 3 == 0:
        return 0
    while initial_length % 3 != 0:
        initial_length += 1
        counter += 1
    return "=" * counter

def to_base64(input_text):
    binary_string = convert_tobin(input_text)
    padding_to_add = padding(input_text)
    numbers = [int(x, 2) for x in convert_to6(binary_string)]
    #print(numbers)
    final_chars = []
    for i in numbers:
        if i <= 25:
            final_chars.append(chr(i + 65))
        if i > 25 and i <= 51:
            final_chars.append(chr(i + 71))
        if i > 51 and i <= 61:
            final_chars.append(chr(i - 4))
        if i == 62:
            final_chars.append(chr(i - 19))
        if i == 63:
            final_chars.append(chr(i - 16))
    if padding_to_add:
        return "".join(final_chars) + padding_to_add
    else:
        return "".join(final_chars)
