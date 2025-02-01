# ❄ SHARD ❄ || Documentation

SHARD can be used for almost anything you need and has an 

# COMMENTS

## WRITING COMMENTS
To write a comment, just add '//' before whatever you're commenting out.

## COMMENTS OVERVIEW
Here is an example that looks at everything we've learned about ``comments``:
```rust
// This is how you comment something out!
```


# VARIABLES

## DEFINING VARIABLES
To define a variable with an number or integer, you can do ``let {variable} = 10``
To define a variable with a string, you can do either ``let {variable} = 'string'`` OR ``let {variable} = "string"``.

Unlike rust, there is no ``i32``, ``u32``, ``f32``, or anything of the sort - it will detect what type of variable it is automatically!

It is important to note that to DEFINE variable, you must do ``let {variable} = {value}``, however this will not let you change the value unless
you define it again.

To make it so that you don't have to redefine it to change the value, simply define it as a mutable variable by doing ``let mut {variable} = {value}"``!
Then, if you want to change the value, all you do is ``{variable} = {value}``, like in python!

## PRINTING VARIABLES
To print a variable in SHARD, do ``echoln(variable)``. If you want to print it in a string, do ``echoln(v'The variable equals {variable})``

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


# FUNCTION ASSIGNMENT


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
