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