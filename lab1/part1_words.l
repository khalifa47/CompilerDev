%%
[\t]+ {}
[a-zA-Z]+ {printf("%s\n", yytext);}
. {}
\n {}
%%