# crypto/blecc

Author: AdnanSlef  
Blecc! What are all these numbers? This doesn't look like RSA... [blecc.txt](https://static.redpwn.net/uploads/abe77ecef06f1e3362c7584aedf2a14aa51ec0da169f66d4328b14e1f8f5eb94/blecc.txt)
__________________________________________________________________________
Mặc dù ban đầu hơi lú nhưng mà sau khi nhìn đi nhìn lại tớ đã xuống dòng đúng cách :V :
   
    p = 17459102747413984477
    a = 2
    b = 3
    G = (15579091807671783999, 4313814846862507155)
    Q = (8859996588597792495, 2628834476186361781)
    d = ???
    Can you help me find `d`?
    Decode it as a string and wrap in flag format.
    
Chứ thực ra ban đầu tớ xuống dòng như này: :)

    p = 17459102747413984477
    a = 2b = 3G = (15579091807671783999, 4313814846862507155)Q = (8859996588597792495, 2628834476186361781)d = ???
    Can you help me find `d`?
    Decode it as a string and wrap in flag format.
    
Rồi vào vấn đề chính:
Sau một hồi search google các kiểu thì tớ biết được đây là Elliptic Curve, dùng mã hóa ECC (vì có ecc giống với file đính kèm nên mới thêm chắc chắn 🤭 ). 

    
    p = 17459102747413984477
    a = 2
    b = 3
    G = (15579091807671783999, 4313814846862507155)
    Q = (8859996588597792495, 2628834476186361781)
    E__ = EllipticCurve(Zmod(p),[a,b])
    print(discrete_log(E__(Q[0],Q[1]),E__.gens()[0],E__.order(),operation='+'))
