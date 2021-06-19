import telnetlib


HOST = 'extended-fibonacci-sequence.hsc.tf'
PORT = 1337
tn = telnetlib.Telnet()
tn.open(HOST,PORT)

def fib(n):
    F = [0,1]
    S = [0,1]
    sum =0
    for i in range(2,n+1):
    	F.append(F[i-1]+F[i-2])
    for i in range(2,n+1):
    	S.append(int(str(S[i-1])+str(F[i])))
    for i in range(0,n+1):
    	sum += S[i]
    return(sum%(10**11))

data = tn.expect([b'\n[0-9]+\n'],3)[2].decode('UTF-8').split('\n')[1]
print(data)
tn.write((bytes(str(fib(int(data)))+'\n','UTF-8')))
while True:
    tuple2 = tn.expect([b'[0-9]+'],3)[2]
    data2 = tuple2.decode('UTF-8').split(' ')[1]
    if tuple2[0]==-1:
        print(tuple2)
        break
    tn.write((bytes(str(fib(int(data2)))+'\n','UTF-8')))
    print(data2)

