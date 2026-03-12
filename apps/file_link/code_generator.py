from random import choice

symbols = "abcdefghijklmnopqrstuvwxyz"
symbols += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols += "0123456789"

def generate() -> str:
    code = ""
    for symbol in range(5):
        code += choice(symbols)

    return code
