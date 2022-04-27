# original script cleaned up a bit following the CTF and implemented some aspects of the following work
# https://github.com/CavemanJay/PicoCTF/blob/master/2022/cryptography/basic_mod1/get_flag.py

# Reading in file
file = open("message.txt", "r").read().split(" ")
contents = [int(f) for f in file if f != '']


contents = [x % 41 for x in contents] # Moding each number by 41
message = [pow(int(i),-1,41) for i in contents] # Finding modular inverse for each number
# print(content_list)


def decrypt_message(val):
        if val == 37: # Under score
                return "_"
        elif val in range(1,27): # Alphabet
                return chr(val+64)
        elif val in range(27,37): # Decimals
                return str(val - 27)
        else:
                return None


result = [decrypt_message(m) for m in message]
flag = ''.join(result)
print(flag)

