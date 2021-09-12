from hashlib import md5

original = '7f4986da7d7b52fa81f98278e6ec9dcb'

for i in range(0,50):
    for k in range(0,12):
        for l in range(0,31):
            year = 1970 + i
            month = 1 + k
            day = 1 + l
            bday = str(year) + ('' if month >=10 else '0') + str(month) + ('' if day >=10 else '0') + str(day)
            pwd = 'Aaron' + bday 
            result = md5(pwd.encode()).hexdigest()
            if result == original: 
                print(pwd)
                break
