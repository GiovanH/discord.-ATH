# discord.ATH
Syntax Reference

```
/*
    This program creates creates a queue from user-inputted values.
    The user may add a number to the end of the queue using [1] and view the queue using [2]. [3] terminates the program.
*/

PROCREATE LOOP 1;
PROCREATE QUEUE NULL;

~ATH(LOOP) {
    print ("Select action:\n");
    print ("[1] Add an item to queue\n");
    print ("[2] View queue\n");
    print ("[3] Exit\n");
    input CHOICE "";
    
    DEBATE (CHOICE == 3) {
            LOOP.DIE();
    } UNLESS (CHOICE == 2) {
            PROCREATE BLAH 0;
            PROCREATE STACK NULL;
            REPLICATE TEMP QUEUE;
            ~ATH(BLAH) {
                    BIFURCATE TEMP[HEAD, TEMP];
                    DEBATE (TEMP) {
                            print ("~s\n", HEAD);
                            AGGREGATE [STACK, HEAD]STACK;
                    } UNLESS {
                            BLAH.DIE();
                    }
            }
            print ("Stack print done.\n");
            PROCREATE OOF 0;
            ~ATH(OOF) {
                    BIFURCATE STACK[STACK, TAIL];
                    print ("I went oof.\n");
                    DEBATE (STACK) {
                            print ("~s\n", TAIL);
                    } UNLESS {
                            OOF.DIE();
                    }
            }
            print ("Queue print done.\n");
    } UNLESS (CHOICE == 1){
            input ITEM "Input string to add: ";
            AGGREGATE [ITEM, QUEUE]QUEUE;
    } UNLESS {
            print ("Invalid input.");
    }
}
THIS.DIE();
// Program end.
```



________________


Language specification
* This will make use of python’s re library, basically the interpreter works on REGEX
* This is not supposed to be very user-friendly, remember! It should be relatively frustrating to use! We’re calling this an esoteric language for a reason!
* In/Out statements are lowercase. Everything else is upper. [[Talks here](https://pastebin.com/au2MLgkV)]
* Variable names follow normal python convention for varnames (any case type, basically)
* Enforced double/single-quotes for strings. Byte-arrays might not actually work?
* Follow C-style comments, canon ~ATH uses C-style comments
* How will it handle importing ~ATH files? Can it import python files also?
   * Import item from file - Is what it looks like, so using python packages wouldn't be hard?
   * We can use python's C libs to import stuff using strings
* import “filename” looks for module or file, must specify ~ATH extension if ~ATH file.
* How will ~ATH imports work?
   * Deal with imports later, get variables and loops working first
* ~ATH will work its variables similarly to LISP (but not exactly): 
   * A variable consists of its symbol and up to two values.
      * Assigning a number/string to a symbol name will always store it in the LEFT value.
      * Assigning a function to a symbol name will always store it in the RIGHT value.
      * An symbol may be assigned as a value to either side, using syntax I haven’t figured out yet.
   * BIFURCATE-ing a symbol will allow one to create new symbol pointers to its parts individually, following the same rules as above.
   * AGGREGATE-ing two values/symbols together will use the third symbol specified and assign its LEFT and RIGHT parts to the two given objects, unless the arrangement will violate the above rules.
   * REPLICATE-ing a symbol will create a new living symbol to point to its two values. One may clone a symbol onto itself to “revive” it.
   * Only symbols can actually die, the values they’re attached to may be reused as many times as needed.
   * One is allowed to assign, BIFURCATE, and AGGREGATE dead symbols onto living symbols and vice-versa.


* An ~ATH loop will iterate through its contents until the symbol it references dies. 
   * One is only allowed to put symbols in the conditional of an ~ATH loop.
   * Killing the control symbol will end the loop immediately like a break statement.
   * The script itself is wrapped in an implicit ~ATH loop controlled by the global symbol THIS. Killing THIS will end the script immediately, and failing to kill THIS at the end of the script will cause it to loop over. [Talks here]
   * One may use the EXECUTE function on a symbol and attach it to a ~ATH loop’s end, which means that the function will be iterated through until a symbol with the same name as the symbol in the ~ATH conditional dies in the function body. Under this syntax, the ~ATH loop body must remain empty aside from other ~ATH loops.
* On Conditional Statements:
   * Putting an expression inside will test if the resulting symbol is alive or not.
   * Value comparison operators: ==, ~=, <, >, <=, >= they compare the LEFT values of symbols, and return a living or dead symbol depending on the truth value.
   * Symbol comparison operators: !=!, ?=!, !=?, ~=!, !=~, ~=~ (compare living state of both symbol parts of both, compare living state of right, compare living state of left, compare both; invert left, compare both; invert right, compare both; invert all)
   * Note that symbol comparison operators will assume that the relevant value side is a symbol type, and will throw an exception if one or both variables being compared don’t have symbols.
* obj.DIE(); is a deconstructor also, good idea? How will it work tho?
* Implicitly asynchronous, explicitly concurrent? (lowest priority)
   * Honestly this might work quite well. Using asyncio’s event loop as a ~ATH loop
   * Asyncio suxxxx but ok
* What happens when we bifurcate the THIS script, two instances looping in the same asyncio loop?
* What about errors/exceptions?
   * All caught errors/exceptions will be logged, but the user will only be given a random insult from our friendly neighborhood Karkat Exception Thrower
* How do user-defined functions work?
   * Function declaration uses the keyword FABRICATE
   * Run function using EXECUTE(FUNC, ARG1, … , ARGN)
   * Pass by value or pass by reference?
   * Return values using the keyword DIVULGATE
________________
# Documentation

## Symbols:


Symbols are the basic units in ~ATH. They represent individual living pointers to a pair of values. The pair of values it refers to follow a simple set of rules: 


By convention the paired values are referred to as the `left` and `right` values of the symbol; the left value may only contain either an `integer`, `float`, `character`, `string`, or `complex` number while the right value may only contain functions.


A single exception is that either of a symbol’s values may instead be other symbols themselves.

## Basic Statements:

Input Statement - Syntax: `input NAME[ PROMPT];`

(Should probably use a different symbol to denote optional parameters, since we use [] for AGGREGATE and BIFURCATE)


Takes a string input from the input buffer. This will automatically convert numbers in appropriate formats into integers and floats before saving the value to the left of NAME.


PROMPT may either be a string or a symbol with a left value that isn’t empty or a symbol. It will display the value as a string before requesting input from the user. Adding a prompt argument is optional, and if not included will cause it to request input without printing a string.


Print Statement - Syntax: `print(STR[, ARG1, ARG2, …]);`


Outputs a string to the console. The first argument is the string to be outputted and must either be a bare string or a symbol containing a string. If the string contains format substrings, it may be supplied an additional number of arguments equal to the number of format substrings.


Format substrings:
`~s` - output value as string
`~d` - output value as integer
`~[x.y]f ` - output value as float with x significant digits and y decimal places. Specifying x and y are optional.


To output tilde ~ symbols directly, escape them with backslash as such: \~


~ATH supports the following special characters in print statements:

```
\a Bell Character
\b Backspace Character
\f Line Feed Character
\r Carriage Return Character
\n Newline Character
\t Horizontal Tab Character
\v Vertical Tab Character
```


Bifurcate Statement - Syntax: `BIFURCATE PARENT[LEFT, RIGHT];`


Splits PARENT into its left and right values and assign two new symbols LEFT and RIGHT to the respective values.


If a value from PARENT is a symbol, it will be directly assigned to the name and no new symbol will be created for it.


If a value from PARENT is not initialized, a new empty dead symbol will be created and assigned to the name.


Aggregate Statement - Syntax: `AGGREGATE [LEFT, RIGHT]NAME;`


Merges LEFT and RIGHT into a new symbol assigned to NAME. 


Implementation Note:
In order to avoid circular referencing when aggregating a symbol to itself, AGGREGATE instead assigns copies of LEFT and RIGHT to the values of the symbol bound to NAME and rebuilds all pointer relationships.
