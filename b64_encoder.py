import codecs

hexa_input = input("Copy the hex code here: ")
b64_result = codecs.encode(codecs.decode(hexa_input, 'hex'), 'base64').decode()

print(b64_result)