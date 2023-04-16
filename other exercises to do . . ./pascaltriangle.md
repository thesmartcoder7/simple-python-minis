# Pascal Triangle Generator
### Create a script to generate the binomial coefficients for (x+y)^n

The Pascal triangle is a table of numbers representing the coefficients of the mathematical expression: **(x+y)^n**. Here are some examples:

- (x+y)^1 = x + y; the coefficients are **1,1**
- (x+y)^2 = x^2 + 2xy + y^2; the coefficients are **1, 2, 1**
- (x+y)^3 = x^3 + 3(x^2)y + 3x(y^2) + y^3; the coefficients are **1, 3, 3, 1**

Therefore, now that you have understood where the pascal triangle is applied, here is how to output the bionamial coefficients for (x+y)^n:

![Pascal Triangle](https://www.w3resource.com/w3r_images/pascal-traingle.png)

Now, go ahead and right a script that generates the the nth row of the Pascal Triangle sucg that:
- if **n=1**, then the output is [1,1]
- if **n=2**, then the output is [1,2,1]
- if **n=3**, then the output is [1,3,3,1], and so on and so forth.

Once your script is working well, trying n as 100. Did you get the right response? Is your code slow or is the execution fast enough. Make sure your code is both accurate and fast!
Note that there are mathematical ways to solve for the Pascal Triangle. Feel free to research them. However, the logic from the image above should be just enough to create a script that works pretty well to generate your nth row of a Pascal triangle.
