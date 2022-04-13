# original script cleaned up a bit following the CTF and implemented some aspects of the following work
# https://github.com/CavemanJay/PicoCTF/blob/master/2022/cryptography/basic_mod1/get_flag.py

# Read in file of numbers
file = open("message.txt", "r").read().split(" ")
message = [int(f) for f in file if f != '']

# Method used for mapping
def decrypt_message(value):
    result = value % 37
    if (result == 36): # Under score
        return "_"
    elif result in range(0,26): # Alphabet
        return chr(result + 65)
    elif result in range(26,36): # Decimals
        return str(result - 26)
    else:
        return None

flagList = [decrypt_message(m) for m in message]
flag = ''.join(flagList)
print(flag)
