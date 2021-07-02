# New Caesar

Category: Cryptography  
Points: 60  
Author: MADSTACKS  
Description: We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{})  
`mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj`  [new_caesar.py](https://mercury.picoctf.net/static/b82dc751249b75b2509315c59f8200c7/new_caesar.py)  

__________________________________________________________________________

Tải file new_caesar.py về xem có gì không nào.

    LOWERCASE_OFFSET = ord("a")
    ALPHABET = string.ascii_lowercase[:16]
    
Đầu tiên khởi tạo chữ cái làm chuẩn là a.
Đặt `ALPHABET='abcdefghijklmnop'`.

    def b16_encode(plain):
  	  enc = ""
	    for c in plain:
		    binary = "{0:08b}".format(ord(c))
		    enc += ALPHABET[int(binary[:4], 2)]
		    enc += ALPHABET[int(binary[4:], 2)]
	    return enc
   
Cái này là bước encode đầu tiên: Lấy từng chữ cái trong `plain`, chuyển thành dạng nhị phân 8 bit. Sau đó tách 4 bit đầu viết về dạng thập phân, lấy chữ cái trong string ALPHABET
có chỉ số tương ứng, tương tự với 4 bit sau.

    def shift(c, k):
	    t1 = ord(c) - LOWERCASE_OFFSET
	    t2 = ord(k) - LOWERCASE_OFFSET
	    return ALPHABET[(t1 + t2) % len(ALPHABET)]
      
Hàm shift ...  

Để ý có `assert all([k in ALPHABET for k in key])` và `assert len(key) == 1` có nghĩa là key phải là một chữ cái và nó phải nằm trong ALPHABET, nếu không sẽ raise error.

    
ĐM code đây:
    
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


Ra kết quả: 

    EUµUU?µÇ?EÇ?E??ÇI??I????????????EEE?Ç?É
    ÜëÆëì▌ÆOcUO"Ü"_OY« Y-« _§- __r_-UÜUcO-U
    íüxüy·xéºìé1í1°éî¼±î_¼±°,_±°°¿°_ìíêºé_ë
    ♫EèúEyúE_EAúÿIAÿIIAAÉIAAAAAIy_ûEúIü
    ☼▲ù▲▼Uù♂Ü♫♂U☼UO♂ _O D_OOUDOOOÑOD♫☼♀Ü♂D
    ►/
    / ê
    ∟í▼∟ì►ìa∟◄ïä◄áïäaëáäaaâaá▼►↔í∟á▲
    !0←01û←-_ -y!yô-"do"òdoôüòoôôóôò !._-ò/
    ♥♠♣♣♦♣♥12?☼>♥0♣>3☺♠3♥☺♠♣
    CR=RS↔=O►BO▼C▼▬OD↕↨D¶↕↨▬▲¶↨▬▬§▬¶BC@►O¶A
    TcNcd.NP!SP T 'PU#(U%#('/%(''&'%STQ!P%R
    et_tu?_a2da1e18af49f649806988786deb2a6c
    v?`??@`rCurBvBIrwEJwGEJIAGJIIHIGuvsCrGt
    ??q??Qq?T??S?SZ??V[?XV[ZRX[ZZYZX???T?X?
    ?§?§"b??e??d?dk??gl?iglkcilkkjki???e?i?
    c,?,1s?¥v"¥ucu|¥ªx}ªzx}|tz}||{|z"c▌v¥z§
    ºÉ☼ÉE?☼¶?1¶?º??¶»??»????????????1º·?¶?,
   
Có mỗi cái `et_tu?_a2da1e18af49f649806988786deb2a6c` là có vẻ đúng, và nó đúng thật :v

#### Flag = picoCTF{et_tu?_a2da1e18af49f649806988786deb2a6c}
