# Cyphper

## Description:

Background story: this code was once used on a REAL site to encrypt REAL data. Thankfully, this code is no longer being used and has not for a  long time.

A long time ago, one of the sites I was building  needed to store some some potentially sensitive data. I did not know how to use any proper encryption techniques, so I wrote my own symmetric cipher.

The encrypted content in output.bin is a well-known, olde English quote in lowercase ASCII alphabetic characters. No punctuation; just letters and spaces.

The flag is key to understanding this message.

### Attached files

- `cypher.php`:

  ```php
  <?php
  
  function secure_crypt($str, $key) {
    if (!$key) {
      return $str;
    }
  
    if (strlen($key) < 8) {
      exit("key error");
    }
  
    $n = strlen($key) < 32 ? strlen($key) : 32;
  
    for ($i = 0; $i < strlen($str); $i++) {
      $str[$i] = chr(ord($str[$i]) ^ (ord($key[$i % $n]) & 0x1F));
    }
  
    return $str;
  }
  ```
- `output.bin`:
    ```
    sf'gh;k}.zqf/xc>{j5fvnc.wp2mxq/lrltqdtj/y|{fgi~>mff2p`ub{q2p~4{ub)jlc${a4mgijil9{}w>|{gpda9qzk=f{ujzh$`h4qg{~my|``a>ix|jv||0{}=sf'qlpa/ofsa/mkpaff>n7}{b2vv4{oh|eihh$n`p>pv,cni`f{ph7kpg2mxqb
    ```


  

## Hint:

The first 6 characters of the flag are `gigem{`.

## Difficulty/Points: 

`100 points`

## Flag:

`gigem{dont~roll~your~own~crypto}`


# Solution
We tried to decode the first characters of the plaintext using the known part of the key (`gigem{`) ad the cypher itself, slightly modified to avoid the key lenght error:
```php
<?php
function secure_crypt($str, $key) {

  $n = strlen($key);

  for ($i = 0; $i < strlen($str); $i++) {
    $str[$i] = chr(ord($str[$i]) ^ (ord($key[$i % $n]) & 0x1F));
  }

  return $str;
}
$myfile = fopen("output.bin", "r");
$cyphertext = fread($myfile,filesize("output.bin"));
fclose($myfile);

$key = "gigem{";
echo(secure_crypt($cyphertext, $plaintext));
?>
```

The output is:
```
to be lt)|}(qd;vq2oqkn5py5huj(euiyjc}m*tg|o`ls%joa7}{rk|t?ky=|po2medz)`f=jbdqne>~pl9u|b}f0vf&arrows#io1|||wj|q{gh9lugm{y=`z4tc*jkyf*b}th(hfdwhac3u0t|g?mq=|jegb`om)ugy9u{7dgnek`wa0n}|5dto
```
Non we know the first 6 character of the plaintext: `to be `. The description says that the plaintext is a famous old english quote, so we hypothesized that the text may be the Hamlet's monologue:
>To be, or not to be, that is the question\
 Whether 'tis nobler in the mind to suffer\
 ...

We tryed to use the first sentence of the monologue as the key, the output is:
```
gi'em;do.t~r/ll>yo5r~ow.~c2ypt/}gigem{d;v|ycgfl>cir2dou`~q&x {|q)~df5nd'ynfd}c9yxw1n{ipa-~zi8fo}knh-sh yb{ox|otin0}w|hs|s"{s2gf3~lrd/{nru/dxdicf/{2nok=xb;{mm|j{hf+z`d1pt)czaar{y{7xb2|mtq
```
The first part of the output resembles a flag, but there are some uncorrectly decrypted character. This behaviour is caused by the presence of the `& 0x1F` operation in the encryption function, which prevents the 3 most significant bits of the text's characters to be encrypted. This is not a big deal when we want to encrypt/decrypt a text but it's a problem when we want to obtain the key from the cypertext and the plaintext. To avoid this problem, it's possible to use a modified version of the chyper that forcibly assign `011` to the 3 most significant bits of the key:
```php
<?php
  function secure_crypt_mod($str, $key) {

    $n = strlen($key);

    for ($i = 0; $i < strlen($str); $i++) {
      $str[$i] = chr((ord($str[$i]) ^ ord($key[$i % $n])) | 0b01100000);
    }

    return $str;
  }

  $myfile = fopen("output.bin", "r");
  $cyphertext = fread($myfile,filesize("output.bin"));
  fclose($myfile);

  $plaintext = "to be or not to be that is the question";

  echo(secure_crypt_mod($cyphertext, $plaintext));
?>
```
The output is:
```
gigem{dont~roll~your~own~crypto}gigem{d{v|ycgfl~cirrdou`~qfx`{|qi~dfundgynfd}cyyxwqn{ipam~zixfo}knhmsh`yb{ox|otinp}w|hs|sb{srgfs~lrdo{nruodxdicfo{rnok}xb{{mm|j{hfkz`dqpticzaar{y{wxbr|mtq
```
