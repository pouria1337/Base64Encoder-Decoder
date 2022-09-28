def convert_tobin(input_string):
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
    #debug
    incomplete_binary = 0
    if len(new_bin[-1]) != 6:
        zero_to_add = 6 - len(new_bin[-1])
        incomplete_binary = new_bin[-1]
        new_bin.pop()
        new_bin.append(incomplete_binary + ("0"*zero_to_add))
    #debig
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

def base64_encode(input_text):
    binary_string = convert_tobin(input_text)
    padding_to_add = padding(input_text)
    numbers = [int(x, 2) for x in convert_to6(binary_string)]
    #debug
    final_chars = []
    for i in numbers:
        if i <= 25:
            final_chars.append(chr(i + 65))
        elif i <= 51:
            final_chars.append(chr(i + 71))
        elif i <= 61:
            final_chars.append(chr(i - 4))
        elif i == 62:
            final_chars.append(chr(i - 19))
        elif i == 63:
            final_chars.append(chr(i - 16))
    if padding_to_add:
        return "".join(final_chars) + padding_to_add
    else:
        return "".join(final_chars)

def main():
    user_input = input("Enter text to encode: ")
    print(base64_encode(user_input))

main()