# GenericFileRead

Assuming a data file with values delimited in some way, this simple Python snippet allows anyone to be able to read the data from the file into a list.

### Implementation

The implementation is very simple, just a lot of maps and reduces and all of that fun functional programming jazz. Not much to explain really. Look at the code!

### Usage

To use it, all you need to do is import the *read.py* file, and call the readDataFromFile function.

Function signature is as follows:

```list<type_T> readDataFromFile(<string> filename, <string> delimiter, <function> conversion_func)```

Regarding the arguments. ```filename``` and ```delimiter``` are relatively straightforward. ```conversion_func``` is the function passed in in order to parse the data contents the proper way. For instance, if the data consisted of integers, ```conversion_func``` would be ```int```.   
