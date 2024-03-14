import math
import tkinter as tk
"""
Berger code calculator for a predemtermined size (error detecting code)

"""

length = 4 # size of the messages

# compute the codewords of size length
message = []
def get_code_of_size_length(code=""):
    if len(code) == length:
        message.append(code)
        return
    get_code_of_size_length(code + "0")
    get_code_of_size_length(code + "1")
get_code_of_size_length("")

# length of the checkbit
checkbit_length = math.ceil(math.log(length) / math.log(2))

def berger_code_calculator(code):
    # number of ones 
    one_count = code.count('1')
    checkbits = bin(one_count)[2:]
    checkbits = checkbits.zfill(length)
    return code + checkbits
# print(berger_code("0110100101"))

def check_error(code) -> bool:
    # n - k <= 2 ** k - 1
    n = len(code)
    for k in range(n//2):
        if n - k <= 2 ** k - 1:
            return True
    return False

# print(message)
for m in message:
    final_message = berger_code_calculator(m)
    print(m, final_message, check_error(final_message))
    # print("For %s code send message: %s" % (m, final_message))