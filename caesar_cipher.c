/*
Problem URL: https://cs50.harvard.edu/x/2021/psets/2/caesar/
Problem Statement: Implement a program that encrypts messages using Caesar’s cipher, per the below.

e.g.    $ ./caesar 13
        plaintext:  HELLO
        ciphertext: URYYB
e.g.    $ ./caesar 1
        plaintext:  HELLO
        ciphertext: IFMMP
e.g.    $ ./caesar 13
        plaintext:  be sure to drink your Ovaltine
        ciphertext: or fher gb qevax lbhe Binygvar

e.g.    $ ./caesar HELLO
        Usage: ./caesar key
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

char input_string[100];
char ch;
int i=0;
void print_usage();
bool is_number();

int main(int argc, char * argv[]){
    printf("%s\n", argv[1]);
    if (argc != 2){
        print_usage();
    }
    else if (! is_number(argv[1])){
        print_usage();
    }
    else{
       printf("plaintext:  ");
       gets(input_string);
       printf("ciphertext: ");
       for(i=0; i < strlen(input_string); i++ ){
            if(65 <= input_string[i] &&  input_string[i] <= 90){
               printf("%c", ((atoi(argv[1]) + input_string[i] - 65 ) % 26) + 65); // uppercase characters starts from 65 in ASCII table
            }
            else if(97 <= input_string[i] &&  input_string[i] <= 122){
               printf("%c", ((atoi(argv[1]) + input_string[i] - 97) % 26) + 97); // lowercase character starts from 97 in ASCII table
            }
            else{
                printf("%c", input_string[i]);
            }
       }
    }
}
void print_usage(){
    printf("Usage: caesar_cipher <key>\n\n       e.g. caesar_cipher 3");
}

bool is_number(char number[]){
    for(int j=0; j < strlen(number); j++){
         if (!isdigit(number[j]))
            return false;
    }
    return true;
}
