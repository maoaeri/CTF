import string

ciphertext = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
ALPHABET = string.ascii_lowercase[:16]
LOWERCASE_OFFSET = ord("a")

def b16_decode(cipher):
	dec = ''
	for c in range(0,len(cipher),2):
		binary1 = "{0:04b}".format(ALPHABET.index(cipher[c]))
		binary2 = "{0:04b}".format(ALPHABET.index(cipher[c+1]))
		dec += chr(int(binary1+binary2,2))
	return dec

def unshift(c,k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t2 + t1) % len(ALPHABET)]

for key in ALPHABET:
	dec = ""
	for c in ciphertext:
		dec += unshift(c,key)
	flag = b16_decode(dec)
	print(flag)
