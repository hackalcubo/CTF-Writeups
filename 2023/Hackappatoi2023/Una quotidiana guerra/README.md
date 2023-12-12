# Una quotidiana guerra
## DESCRIPTION: 
`Max Pezzali has stolen the holy code containing the secret song, and replaced everything with his lyrics!!!
Can you recreate the code for me? And please, don’t listen to the secret song :(`

[una_quotidiana_guerra.c](Attachments/una_quotidiana_guerra.c)

### Author: 
`@retro4hack`

## FLAG:
`HCTF{3nj0y_https://youtu.be/DYeklxeUpFo}`

## Solution
After downloading the [file](Attachments/una_quotidiana_guerra.c), we can see that the file is somewhat encrypted.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define tu 
#define dimmi 
#define come 
#define mai 
#define kilometri 
#define melodia 
#define sus 
#define inutile 
#define inutilestimai 
#define qui 
#define seduto 
#define notti 
#define alla 
#define sento 
#define sogno 
#define pregando 
#define non 
#define scrivere 
#define ma 
#define casa 
#define vedere 
#define dove 
#define vai 

notti quotidiana inutile inutilestimai alla "abcdefghijklmnopqrstuvwxyz.:_-=/{}ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  sus
notti guerra inutile inutilestimai alla "HDVIC8tq8}Es/{-}JOPJAHHJQ.=Y5rAHJWEtRgSc" sus  
tu stanza come notti finiscono mai qui
sogno come tu i alla 0 sus i non pregando come quotidiana mai sus i scrivere mai qui
ma come finiscono casa quotidiana inutile i inutilestimai mai qui
melodia i sus
seduto seduto
melodia 0 sus seduto 
sento bambino come mai qui
sogno come tu i alla 0 sus i non pregando come guerra mai sus i scrivere mai qui
guerra inutile i inutilestimai alla quotidiana inutile come stanza come guerra inutile i inutilestimai mai vedere pregando come quotidiana mai dove i mai  vai pregando come quotidiana mai inutilestimai sus seduto
kilometri come "%s\n", guerra mai sus seduto
tu dimmi come mai qui
kilometri come "Kilometri di kilometri di kilometri di kilometri\n" mai sus
bambino come mai sus
melodia 0 sus seduto
```

Following the syntax of C, we began to create a mapping of the words with their equivalents in C and arrived at the following mapping.

```json
mapping = {
	"tu" : "int", 
	"dimmi" : "main", 
	"come" : "(", 
	"mai" : ")", 
	"kilometri" : "printf", 
	"melodia" : "return", 
	"sus" : ";", 
	"inutile" : "[", 
	"inutilestimai" : "]", 
	"qui" : "{", 
	"seduto" : "}", 
	"notti" : "char", 
	"alla" : "=", 
	"sento" : "void", 
	"sogno" : "for", 
	"pregando" : "strlen", 
	"non" : "<", 
	"scrivere" : "++", 
	"ma" : "if", 
	"casa" : "==", 
	"vedere" : "+", 
	"dove" : "-", 
	"vai" : "%"
}
```

So, the [recreated program](Attachments/una_quotidiana_guerra_ricreated.c) is the following, which after being compiled gives us the flag.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char quotidiana [ ] = "abcdefghijklmnopqrstuvwxyz.:_-=/{}ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  ;
char guerra [ ] = "HDVIC8tq8}Es/{-}JOPJAHHJQ.=Y5rAHJWEtRgSc" ;  

int stanza ( char finiscono ) {
	for ( int i = 0 ; i < strlen ( quotidiana ) ; i ++ ) {
		if ( finiscono == quotidiana [ i ] ) {
			return i ;
		} 
	}
	return 0 ; 
}
 
void bambino ( ) {
	for ( int i = 0 ; i < strlen ( guerra ) ; i ++ ) {
		guerra [ i ] = quotidiana [ ( ( stanza ( guerra [ i ] ) + strlen ( quotidiana ) ) - i ) % strlen ( quotidiana ) ] ; 
	}
	printf ( "%s\n", guerra ) ; 
}

int main ( ) {
	printf ( "Kilometri di kilometri di kilometri di kilometri\n" ) ;
	bambino ( ) ;
	return 0 ; 
}
```