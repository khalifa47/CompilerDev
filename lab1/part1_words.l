%%
[\t]+ {}
[a-zA-Z]+ {printf("%s\n", yytext);}
. {}
\n {}
%%

int main() {
    yylex();

    return 0;
}