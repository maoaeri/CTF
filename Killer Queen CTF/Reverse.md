# sneeki snek  
Author: ZeroDayTea  
Description: ssssssssssssssssssssssssssssssssssssss  
[sneekisnek.txt](https://2021.killerqueenctf.org/Public/sneekisnek.txt)  

--------------------------------------------------------------------------------
The given file is python bytecode, so our mission is dissasemble it. I read this article: [Understanding Python Bytecode](https://towardsdatascience.com/understanding-python-bytecode-e7edaae8734d) and this python docs [dis — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html). This is the result:

```python
f = ''
a = 'rwhxi}eomr\\^`Y'
z = 'f]XdThbQd^TYL&\x13g'
a = a+ z
for i,b in enumerate(a):
	c = ord(b)
	c = c-7
	c = c + i
	c = chr(c)
	f = f+c
print(f)    
``` 
 
flag: `kqctf{dont_be_mean_to_snek_:(}`
