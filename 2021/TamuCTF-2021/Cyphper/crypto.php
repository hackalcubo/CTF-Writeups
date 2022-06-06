<?php
function secure_crypt($str, $key) {

  $n = strlen($key);

  for ($i = 0; $i < strlen($str); $i++) {
    $str[$i] = chr(ord($str[$i]) ^ (ord($key[$i % $n]) & 0x1F));
  }

  return $str;
}

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

$key = "gigem{";
echo(secure_crypt($cyphertext, $key));
echo("\n");
$plaintext = "to be or not to be that is the question";
echo(secure_crypt($cyphertext, $plaintext));
echo("\n");
echo(secure_crypt_mod($cyphertext, $plaintext));
?>