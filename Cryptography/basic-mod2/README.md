# basic-mod2

## Description
A new modular challenge!
Download the message [here](./message.txt).
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Hints
Do you know what the modular inverse is?

The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z

It's recommended to use a tool to find the modular inverses

## How To
Almost the exact same as [basic-mod1](../basic-mod1/README.md), we approach this challenge the same, we need take each number mod by 41, then use a tool to find the modular inverse.
I used the `pow` tool built into python. Some links to learn more about the tool and modular inverse: [Stack Overflow](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python), [DelftStack](https://www.delftstack.com/howto/python/mod-inverse-python/), [Python.org](https://bugs.python.org/issue36027).
I used my script from the previous challenge and added the extra step of finding the modular inverse. [Script](./Basic-Mod2-Script.py)

## Flag
picoCTF{1NV3R53LY_H4RD_C680BDC1}
