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

# sneeki snek 2 oh no what did i do
Author: ZeroDayTea  
Description: did snek steal your pasta because this is some spaghetti (I don't understand a shjt :))  
[sneekisnek2.txt](https://2021.killerqueenctf.org/Public/sneekisnek2.txt)

-----------------------------------------------------------------------
It's the same as sneeki 1, just a little longer. Result:
```python
a =[1739411,1762811,1794011,1039911,1061211,1718321,1773911,1006611,1516111,1739411,1582801,1506121,1783901,1783901,1773911,1582801,1006611,1561711,1039911,1582801,1773911,1561711,1582801,1773911,1006611,1516111,1516111,1739411,1728311,1539421]
b = ''
for i in a:
	c = str(i)[::-1]
	c = c[:-1]
	c = int(c)
	c = c^5
	c = c-55555
	c = c//555
	b = b+chr(c)
print(b)
```
flag: `kqctf{snek_waas_not_so_sneeki}`
	
