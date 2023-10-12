%{
#include <stdio.h>
#include <math.h>

void yyerror(const char* s);
%}

%token NUM

%%

input: /* empty */
    | input line
    ;

line:
    expr '\n'     {
        printf("Result: %d\n", $1);
        printf("Reached the printf\n"); // Debugging statement
        fflush(stdout); // Flush the output
        printf("Output flushed\n"); // Debugging statement
    }
    ;

expr:
    NUM           { $$ = $1; }
    | expr '+' NUM { $$ = $1 + $3; }
    | expr '-' NUM { $$ = $1 - $3; }
    | expr '*' NUM { $$ = $1 * $3; }
    | expr '/' NUM { $$ = $1 / $3; }
    | expr '^' NUM { $$ = (int)pow($1, $3); }
    | '(' expr ')'  { $$ = $2; }
    ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "Parser error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}