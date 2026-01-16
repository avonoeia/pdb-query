enum yytokentype {
    CONFIG = 1000, QUERY, FIND, WHERE, AND, OR, 
    EQUALS, LESS, GREATER, LPAREN, RPAREN, 
    NUMBER, STRING, IDENTIFIER
};
union { char *str; } yylval;