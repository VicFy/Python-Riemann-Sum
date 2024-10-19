# Riemann-Sum-Python
This project features a Python algorithm designed to calculate the area under the curve for four specific equations using Riemann sums. The approach offers three modes of estimation: left, midpoint, and right Riemann sums. Each method breaks the interval into small rectangles to approximate the integral, providing different levels of accuracy. These estimations are applied to functions like linear, quadratic, cubic, and exponential decay, showcasing a variety of mathematical behaviors.

When working with crescent and decrescent functions, the choice of the rectangle’s upper point (left or right) significantly impacts the result. This decision affects the sign of the relative error and alternates between overestimation and underestimation. It's essential to pay close attention to this detail when analyzing the results, as it can change how the error is interpreted.

In addition, the algorithm calculates the relative error between the numerical approximations and their known analytical solutions, offering insights into the accuracy of each method. For better visualization, Matplotlib is used to create graphical representations of the Riemann sums, plotting the rectangles under the curves to highlight the areas and errors. To grasp this concept more clearly, check out the gif below!

![Riemanngif](https://github.com/user-attachments/assets/93cffbf7-f014-4310-944d-0175612132ba)
