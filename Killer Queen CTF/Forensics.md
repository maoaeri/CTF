# Obligatory Shark
Author: sampinkerton  
Description: remember to wrap the flag  
[challenge.pcapng](https://2021.killerqueenctf.org/Public/challenge.pcapng)

----------------------------------------
So I searched online about PCAPNG files, and this is what I got:  
![image](https://user-images.githubusercontent.com/71202086/139532773-6c4d8694-2a05-4914-8aa3-22be3eb3ad27.png)  
Before this challenge, I've known nothing about PCAPNG files, so I just opened it in Wireshark to see what I can find. 
![image](https://user-images.githubusercontent.com/71202086/139532923-8009831a-ce53-4549-a907-988c80e2ec6d.png)  
Everything seemed too complicated for me to understand, and I had to searched for "how to analyze pcapng file". Luckily, I found this article: [PCAP analysis basics with Wireshark [updated 2021]](https://resources.infosecinstitute.com/topic/pcap-analysis-basics-with-wireshark/). I followed the instruction in the article and found this: ![image](https://user-images.githubusercontent.com/71202086/139533049-fe7f1920-5bb5-431c-848a-63a08e413816.png)  
There seemed to be no page where I can login with this account, so I thought the flag is in the password. Hmmm... But it's not hex, so maybe something else. I searched Google again :) and I'm (luckily again) found out that it's md5 hash. So the flag is: `kqctf{dancingqueen}`

