# rectangle-draw

## About
A simple yet fun program that draws a rectangle of specified width and height via input from the user. The goal is to:
1. Prompt the user of the width and print and error mesage and exit if the value is less than 2.
2. Prompt the user of the height and print and error mesage and exit if the value is less than 2.
3. If user enters acceptable values then call function to draw rectangle and pass in the user values as parameters.
4. It's fair to assume here that the user will enter integers so there is no error checking for input types.

## Usage
`python3 rectangle-draw.py`

### Sample Output
```
❯ python3 rectangle-draw.py
Enter width of rectangle: 54
Enter legnth of rectangle: 9
+ ---------------------------------------------------- +
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
+ ---------------------------------------------------- +
❯
❯ python3 rectangle-draw.py
Enter width of rectangle: 1
error: width ( 1 ) must be > 1
❯
❯ python3 rectangle-draw.py
Enter width of rectangle: 2
Enter legnth of rectangle: 1
error: height ( 1 ) must be > 1
❯
❯ python3 rectangle-draw.py
Enter width of rectangle: 2
Enter legnth of rectangle: 2
+  +
+  +

```

## Contributors
Ryan Fisher


