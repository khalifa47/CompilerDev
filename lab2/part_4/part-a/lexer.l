%{
#include "y.tab.h"
%}

%%
[0-9]+                  { yylval = atoi(yytext); return NUM; }
[-+*/^()\\n]            { return yytext[0]; }
[ \t]                   ; // Ignore whitespace
.                       { printf("Unexpected character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}