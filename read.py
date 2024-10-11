GEN_LEN = 8
GENERATOR_VALUE = int('10110010', 2)


def cyclic_r_partial(data:int, mask:int):
    mask_l = len(bin(mask)) - 3
    data_l = len(bin(data)) - 2
    while (data_l - mask_l - 1) >= 0:
        shifted_mask = mask << (data_l - mask_l - 1)
        data = data ^ shifted_mask
        data_l = len(bin(data)) - 2
    return data


with open('test.txt', 'rb') as F:
    byte_string = 0
    
    data = F.read()
    for byte in data:
        byte_string = byte_string << 8
        byte_string = byte_string | byte
        byte_string = cyclic_r_partial(byte_string, GENERATOR_VALUE)
    
    byte_string << GEN_LEN - 1
    byte_string = cyclic_r_partial(byte_string, GENERATOR_VALUE)

print(bin(byte_string))