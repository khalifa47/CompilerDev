%%
[\t]+ {}
[a-zA-Z]+ {printf("%s\n", yytext);}
. {}
\n {}
%%

int yywrap(){}
int main() {
    yylex();
    
    return 0;
}