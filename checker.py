from icecream import ic
def str_bin(phrase:str):
    for char in phrase:
        if char == phrase[0]:
            output = ord(char)
        else:
            output = output << 8
            output = output | ord(char)
    return output

def cyclic_redundancy(data:int, mask:int):
    mask_l = len(bin(mask)) - 3
    data = data << mask_l 
    data_og = data 
    data_l = len(bin(data)) - 2
    while (data_l - mask_l - 1) >= 0:
        shifted_mask = mask << (data_l - mask_l - 1)
        data = data ^ shifted_mask
        data_l = len(bin(data)) - 2
    return data_og | data

key_bits = int(input("Phrase: "), 2)


gen_bits = int(input("enter binary generator: "), 2)

print(bin(cyclic_redundancy(key_bits, gen_bits)))