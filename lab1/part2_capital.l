
%{
int count = 0;
%}

%%
[aeiouAEIOU] {count++;}
[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,4} {printf("%s is an email address\n", yytext);} 
.    {printf("%s is not an email address\n", yytext);} 
\n    {return 0;}
%%

/*** Code Section prints the number of
capital letter present in the given input***/
int yywrap(){}
int main(){

yylex();
printf("\nNumber of Vowels =%d", count);
 
return 0;
}