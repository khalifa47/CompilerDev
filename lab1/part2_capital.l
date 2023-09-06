
%{
int count = 0;
%}


%%
[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,4} {printf("%s is an email address\n", yytext);}
[aeiouAEIOU] {count++;}
.     {printf("%s is not an email address\n", yytext);}
\n    {return 0;}
%%

 
/*** Code Section prints the number of
capital letter present in the given input***/
int yywrap(){}
int main(){
 
// Explanation:
// yywrap() - wraps the above rule section
/* yyin - takes the file pointer
          which contains the input*/
/* yylex() - this is the main flex function
          which runs the Rule Section*/
// yytext is the text in the buffer
 
// Uncomment the lines below
// to take input from file
// FILE *fp;
// char filename[50];
// printf("Enter the filename: \n");
// scanf("%s",filename);
// fp = fopen(filename,"r");
// yyin = fp;
 
yylex();
printf("\nNumber of Captial letters "
      "in the given input - %d\n", count);
 
return 0;
}