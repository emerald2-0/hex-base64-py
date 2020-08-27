import codecs
import time

def hex_to_base64():
	hexa_input = input("Enter the hex code here: ")
	time.sleep(0.4)
	print("Converting to base64...")
	time.sleep(0.4)
	b64_result = codecs.encode(codecs.decode(hexa_input, 'hex'), 'base64').decode()
	print("Conversion complete...")
	
	return b64_result

print("Cyphers supported: ")
time.sleep(0.4)
print("1. Hexa to Base64 ")
print("2. Ceaser Cypher ")
cypher_method = int(input("Select the a cypher method: "))

if cypher_method == 1:
	print("Refering to hexa conversion...")
	time.sleep(0.4)
	hex_to_base64()

if cypher_method != 1:
	print("No other method supported for now..")
