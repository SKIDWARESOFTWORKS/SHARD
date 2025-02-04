# ❄ SHARD ❄ || Documentation

SHARD can be used for almost anything you need! It is a programming language that's sole purpose is to make cybersecurity and hacking a priority in coding, and to make it easy at that!

# THE BASICS
## PRINTING
Printing things are easy! Just use the ``echoln()``. Here are some different ways you can use it:

```
echoln() - Prints a blank line that can be used to seperate text.

echoln('text here') - Prints text.

echoln(variable) - Prints a variable.

echoln(v'The variable is equal to: {variable}') - Joins text and a variable into one string.

echoln('\nHi there!') - Creates a line break and prints the text.

echoln('Hi', variable) - Prints two or more components. When using the comma, it automatically makes a space.

echoln('Hi ' + variable) - Prints two or more components. You must manually add a space if you have a string.
```

You can either use "" for strings or '', it doesn't matter.

## WRITING COMMENTS
To write a comment, just add '//' before whatever you're commenting out.

## BASICS OVERVIEW
Here is an example that looks at everything we've learned about ``the basics``:
```rust
let name = 'John' // <--- You will learn this in the next section
echoln(v'Hello {name}!, "\nYour name *is* " + name, 'right?')
```

Output:
```
Hello John!
Your name *is* John right?
```


# VARIABLES

## DEFINING VARIABLES
To define a variable with an number or integer, you can do ``let {variable} = 10``
To define a variable with a string, you can do either ``let {variable} = 'string'`` OR ``let {variable} = "string"``.

Unlike rust, there is no ``i32``, ``u32``, ``f32``, or anything of the sort - it will detect what type of variable it is automatically!

It is important to note that to DEFINE a variable, you must do ``let {variable} = {value}``, however this will not let you change the value unless you define it again.

To make it so that you don't have to redefine it to change the value, simply define it as a mutable variable by doing ``let mut {variable} = {value}"``!
Then, if you want to change the value, all you do is ``{variable} = {value}``, like in python!

## PRINTING VARIABLES
To print a variable in SHARD, do ``echoln(variable)``. If you want to print it in a string, do ``echoln(v'The variable equals {variable}.)``

## VARIABLES INSIDE OF FUNCTIONS
By default, variables are mutable if they are arguments in a function. (This will not be covered in the overview, due to the fact that
this section comes before functions. However, it *is* covered in the *Functions Overview*.)

## VARIABLE OVERVIEW
Here is an example that looks at everything we've learned about ``variables``:
```rust
let name = "John"
// Cant be changed; only redefined
let mut age = 25
// Can be changed AND redefined

echoln(name)
echoln(age)
echoln()
echoln(v"Your name is {name}.")
echoln(v"You are {age} years old.")

age = 26
// We can change the age because it is mutable, however if we were to
// change the name variable without redefining it, it would present us
// with an error.

echoln(v"You just aged 1 year and are now {age} years old!")
```

Output:
```
John
25
Your name is John.
You are 25 years old.
You just aged 1 year and are now 26 years old!
```


# FUNCTIONS
## DEFINING FUNCTIONS
To define a function, simply do:
```lua
function main() {
   <Put whatever code you need here>
}
```
Just write whatever code you're executing in there!

Additionally, you can also write arguments within the functions like this.
```lua
function main(numberone, numbertwo) {
   output = numberone + numbertwo
   echoln(v"{numberone} + {numbertwo} = {output}")
}
```
It is important to note that functions must be called in order to be executed, with the exception of the main() function, that will run automatically if it exists. Any other function must be called to be executed.

## CALLING FUNCTIONS
To call a function, just type the functions name in this format: ``function_name()``.
It is important to note that if your function has arguments, it wont execute correctly if the arguments are not filled out.
For example, if the function is adding 2 numbers, it needs the 1st argument for the first number, and the 2nd argument for the second number. However, if one or more are not specified, the function will error.

*This code will error:*
```lua
function addnumbers(num, num2) {
   output = num + num2
   echoln(v"{num} + {num2} = {output}
}

addnumbers()

```

*This code wil run as it is supposed to:*
```lua
function addnumbers(num, num2) {
   output = num + num2
   echoln(v"{num} + {num2} = {output}
}

addnumbers(32, 40)
```

## FUNCTIONS OVERVIEW
Here is an example that looks at everything we've learned about ``functions``:
```lua
function makemoney(money, account) {
   account = account + money
   echoln(f'Your account now holds ${money}!')
   echoln()
}

makemoney(30, 20)
```

Output:
```js
Your account now holds $50!
```

# CONDITIONALS
``` 
if X == 5 {
   logln("X is 5")
} else {
   logln("X is not 5")
}
```

# LOOPS
**For Loop:**
```
for i in 0..5 {
   logln(i)
}
```

**While Loop:**
```
temp counter = 0
while counter < 5 {
   logln(counter)
   counter += 1
}
```

# IMPORTS
``` 
import network
import cryptography
```

# ERROR HANDLING
**Try-Catch:**
```
func divide(a, b) {
   try {
      temp result = a / b
      return result
   } catch (error) {
      logln("Error: {error}")
   }
}
```

# MODULE CREATION
```
// my_module.shrd
func my_func() {
   logln("This is my function.")
}
```

# DATA TYPES
**Primitive Types:**
- String
- Integer
- Boolean
- Float

**Collections:**
- Arrays
- HashMaps (similar to JavaScript objects)

Let me know if you'd like to add or adjust anything!
