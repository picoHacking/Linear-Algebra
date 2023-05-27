# Linear Algebra Application: Cubic Splines
Convert random points into a continuous, piecewise curve using linear algebra.

This program uses numpy arrays to create a system of linear equations based on a specified number of randomly located points in the x-y plane. The solution is a vector whose entries are the coefficients of cubic polynomials. These polynomials are graphed over each interval to form a smooth curve. The 1st and 2nd derivatives of the cubic polynomials are equal at the intersections of adjacent curves. This ensures that the final curve is continuous, and there are enough linear equations to solve the system.


![Figure_1](https://github.com/picoHacking/Linear-Algebra/assets/50973789/f1698777-c712-4489-9d09-f1a30f748b38)

Figure 1: a sample output with each piecewise curve in a different color. The program will actually output the curve in orange over the straight lines through each coordinate (gray).
