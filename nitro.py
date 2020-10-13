import random
import os




def Nitro():
    code = ''.join(random.choices(randomness + randomnum, k=16))
    return f'https://discord.gift/{code}'

randomness = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz'

randomnum = '123456789'

numbers = input("Enter amount of codes to generate or press enter to generate indefinitely: ")

nitro_file = open("nitro.txt", 'a')

try:
	for i in range(int(numbers)):
		print(nitro_file.write(f"[NITRO GEN #{i}] " + Nitro() + "\n"))


except:
	os.system('cls')
	print("Generating nitro codes, ctrl + c to stop.")
	while True:
		nitro_file.write(Nitro() + "\n")
