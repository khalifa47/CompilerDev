%{
#include <string.h>
int is_email = 0;
int vowel_count = 0;
%}

%%
[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]{2,4} {
    is_email = 1;
    char *email = yytext;
    for (int i = 0; email[i] != '\0'; i++) {
        if (strchr("aeiouAEIOU", email[i]) != NULL) {
            vowel_count++;
        }
    }
}
[aeiouAEIOU] { vowel_count++; }
\n {
    if (is_email) {
        printf("The input is an email address.\n");
    } else {
        printf("The input is not an email address.\n");
    }
    return 0;
}
%%

int yywrap() {}

int main() {
    yylex();
    printf("Number of Vowels: %d\n", vowel_count);
    return 0;
}