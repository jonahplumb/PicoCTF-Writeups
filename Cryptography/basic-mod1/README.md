# basic-mod1

## Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message [here](./message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Hints
Do you know what mod 37 means?

mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## How To

After reading the description you can see that we are given a message to us in a list of numbers.
We need to take the modulus of each number and map it the specified alphabet given to us. This can be done in various ways, I decided to write a [script](./Basic-Mod1-Script.py)
This script reads in our message file, takes each number and mods it by 37 and then proceeds to map it to our given alphabet.
The alphabet is mapped using values 26-35 being subtracted by 26 to restore them to normal decimal value, ascii characters are mapped by adding 65 and our underscore is mapped directly to 36.
This script does not print out the flag wrapped in the proper picoCTF{} flag format

## Flag
picoCTF{R0UND_N_R0UND_79C18FB3}
