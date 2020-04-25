import base64


def hex2base(input_hex):
    barr = bytearray.fromhex(input_hex)
    return base64.b64encode(barr).decode()


def fixed_xor(x, y):
    xarr = bytearray.fromhex(x)
    yarr = bytearray.fromhex(y)
    result = bytes(a ^ b for (a, b) in zip(xarr, yarr))
    return result.hex()

def single_byte_xor():
    pass


def challenge_1():
    hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert hex2base(hex_input) == base_output


def challenge_2():
    x = "1c0111001f010100061a024b53535009181c"
    y = "686974207468652062756c6c277320657965"
    xor_output = "746865206b696420646f6e277420706c6179"
    assert fixed_xor(x, y) == xor_output

def challenge_3():
    pass


challenge_2()
