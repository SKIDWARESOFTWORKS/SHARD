# ❄ SHARD ❄ || Documentation

SHARD can be used for almost anything you need. With a familiar syntax. Below are examples.

# VARIABLES
(let) ```temp X = "5"```<br>
(const) ```perm X = "100"```

# FUNCTION ASSIGNMENT
```
func greet(name) {
   logln("Hello, " + name)
}
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
