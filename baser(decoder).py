def make_binary(text_input):
    """
    Removes "=" padding from encoded text, and creats a binary
    for each encoded character in "0b~" format.
    """
    if "=" in text_input:
        text_input = "".join(text_input.split("="))
    return [bin(ord(x)) for x in text_input]

def back_to6(binary_list):
    """
    Reverses the adding/subtracting process in encoder code.
    Resulting binaries are devoid of "0b" characters, but 
    they are not len(6)
    """
    six_bit = []
    for binary in binary_list:
        if int(binary,2) == 43:
            six_bit.append(bin(int(binary,2) + 19))
        elif int(binary,2) == 47:
            six_bit.append(bin(int(binary,2) + 16))
        elif int(binary,2) <= 57:
            six_bit.append(bin(int(binary,2) + 4))
        elif int(binary,2) <= 90:
            six_bit.append(bin(int(binary,2) - 65))
        elif int(binary,2) <= 122:
            six_bit.append(bin(int(binary,2) - 71))
    return [x[2:] for x in six_bit]

def make_six(transformed_bits):
    """
    Takes a binary and adds zero's "0" to its left end 
    untill the length of every binary is six.
    Opposite to what encoder code does in the same stage does.
    """
    for index, binary in enumerate(transformed_bits):
        if len(binary) != 6:
            transformed_bits[index] = ("0" * (6 - len(binary))) + binary
    #debug
    return "".join(transformed_bits)

def segment_to_byte(binary_input):
    """
    Starting from the leftmost bit in the string, this function 
    creates 8-bit segments (bytes)  to be used for creating
    ascii characters.

    6 bits from original binary + 2 bits from the next 6-bit segment 
    that was the output of make_six function.
    """
    segmented = []
    start = 0
    end = 8
    while start < len(binary_input):
        segmented.append(binary_input[start:end])
        start = end
        end += 8
    return segmented

def to_ascii(segmented_input):
    """
    A list comprehension that:
    1. Converts each created byte from segment_to_byte to integer
    2. Converts each integer into an ascii character 
    3. if the last remaining binary is not a byte, it doesn't
        decode it to ascii character. It will be discarded.
    """
    return "".join([chr(int(x,2)) for x in segmented_input if len(x) == 8])

def base64_decoder(input_text):
    """
    The final main function that executes every function
    in code in order.
    """
    detransform = back_to6(make_binary(input_text))
    complete_6bits = make_six(detransform)
    byte_form = segment_to_byte(complete_6bits)
    return to_ascii(byte_form)
