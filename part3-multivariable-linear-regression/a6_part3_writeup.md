# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

0.86. My model is much more accurate because it is closer to 1 the the previous two r^2 values.

2. Is your model accurate? Why or why not?

I would say the model is accurate, although not a perfect correlation, it is still very close to 1.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

$9099.98 and $2240.25

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

This is happening because we didn't set a limit to the cars value so it uses the same formula which keeps on decreasing the value until the value is eventually negative.