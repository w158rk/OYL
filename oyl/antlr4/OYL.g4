grammar OYL;

CATEGORY: 'category';
SEMICOLON: ';' ;
WS : [ \u000C\t\r\n] -> skip ;
DATE: [0-9][0-9][0-9][0-9] '-' [0-9][0-9] '-' [0-9][0-9];
IN: 'IN';
OUT: 'OUT';
INTEGER: [0-9]+;
ID : (~ [ \n\u000D\t0-9-;])(~ [ \n\u000D\t;])*;

records: (category | record)*;
category: CATEGORY name code attrname* SEMICOLON;
record: date? (IN|OUT) name number unit attrvalue* (SEMICOLON note)? SEMICOLON;
name: ID;
code: ID;
attrname: ID;

date: DATE;
number: INTEGER;
unit: ID;
note: ID;
attrvalue: ID | INTEGER | DATE;