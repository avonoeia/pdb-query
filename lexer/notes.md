# yywrap() function in Flex

In flex, yywrap() is a function that the lexical analyzer (yylex()) calls when it reaches the end of an input file or input stream. Its primary purpose is to manage multiple input sources or terminate the scanning process.

You may use the %option noyywrap direction in the definitions section to tell your program that the end of the input has been reached and no further action needs to be taken.

Alternatively, you can also define the your own custom yywrap function after the second % sign. This function should return 1 to indicate that the no more input is available. However, if you want to continue scanning, for example if you want to read from multiple files, you can return 0 which indicates that the function has set up a new input which is usually done by calling the yyin variable to point to a new input file.

If you don't provide a yywrap() or specify the noyywrap option, you have to either link with the flex library (-lfl), which provides a default yywrap() that always returns 1 or you have to use the --noyywrap flag in your command.