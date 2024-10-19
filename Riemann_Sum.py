# Tasks:
# Provide the calculated and approximated area using Riemann sums of the functions y = x, y = x + x^2, y = x + x^2 + x^3, and y = e^-x, limited by the interval [0, 1].
# Plot the graphs using left Riemann approximation.
# How many delta_x are needed for the numerical and analytical solutions to converge? And what is the Relative error?

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def quadra(x): # Quadratic function.
    return x+x**2 

def cub(x): # Cubic function.
     return x+x**2+x**3

n = 10 # Number of intervals.

p = 2 # Number of decimal places.

lim_sup = 1 # Upper limit of integration.
lim_inf = 0 # Lower limit of integration.

delta_x = 1/n # x interval.

x_a = np.linspace(lim_inf, lim_sup, n+1) # Array with the x domain.

f_lin = np.zeros(n+1) # Array with the image of x in the linear function.
f_lin = x_a

f_quad = np.zeros(n+1) # Array with the image of x in the quadratic function.
f_quad = x_a + x_a**2

f_cub = np.zeros(n+1) # Array with the image of x in the cubic function.
f_cub = x_a + x_a**2 + x_a**3

f_exp = np.zeros(n+1) # Array with the image of x in the exponential function.
f_exp = np.exp(-x_a)

f_sum = np.zeros((4, 3)) # Null 4x3 matrix to store the summation of the functions for the left, mid, and right Riemann sums, respectively.

#--------------------------------------------

# Loops that calculate the summation and store it in the corresponding function row.

for i in range(0, n): # Left Riemann sum
    f_sum[0,0] += f_lin[i]*delta_x
    f_sum[1,0] += f_quad[i]*delta_x
    f_sum[2,0] += f_cub[i]*delta_x
    f_sum[3,0] += f_exp[i]*delta_x

for i in range (1, n+1): # Midpoint Riemann sum
    f_sum[0,1] += ((x_a[i]+x_a[i-1])/2)*delta_x
    f_sum[1,1] += quadra((x_a[i]+x_a[i-1])/2)*delta_x
    f_sum[2,1] += cub((x_a[i]+x_a[i-1])/2)*delta_x
    f_sum[3,1] += np.exp(-(x_a[i]+x_a[i-1])/2)*delta_x

for i in range(1, n+1): # Right Riemann sum
    f_sum[0,2] += f_lin[i]*delta_x
    f_sum[1,2] += f_quad[i]*delta_x
    f_sum[2,2] += f_cub[i]*delta_x
    f_sum[3,2] += f_exp[i]*delta_x
    
f_sum = np.round(f_sum, p)
#--------------------------------------------- 

# Analytical solutions of the integrals of the functions in the interval [0, 1].
analy = [1/2, 0.833, 1.083, 0.632]

e_r = np.zeros((4, 3))  # 4x3 matrix to store the relative errors.

for j in range(3): # Calculates the Relative error of each function for each estimation method.
    e_r[:, j] = np.round(((f_sum[:, j] - analy) / analy)*100, p)

#--------------------------------------------- 

# Graphs of the functions using left Riemann sum approximations.

fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12)) = plt.subplots(3, 4, figsize=(18, 8))

ax1.set_title('y = x')
for i in range(1,n):
    ax1.add_patch(Rectangle((x_a[i],0),1/n,f_lin[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax1.plot(x_a, f_lin)

ax2.set_title('y = x + x$^{2}$')
for i in range(1,n):
    ax2.add_patch(Rectangle((x_a[i],0),1/n,f_quad[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax2.plot(x_a, f_quad)

ax3.set_title('y = x + x$^{2}$ + x$^{3}$')
for i in range(1,n):
    ax3.add_patch(Rectangle((x_a[i],0),1/n,f_cub[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax3.plot(x_a, f_cub)

ax4.set_title('y = e$^{-x}$')
for i in range(1,n+1):
    ax4.add_patch(Rectangle((x_a[i]-1/n,0),1/n,f_exp[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax4.plot(x_a, f_exp)

for i in range(1, n):
    ax5.add_patch(Rectangle(((x_a[i]+x_a[i-1])/2, 0), 1/n, f_lin[i], linewidth=2, ec='#87cefa', fc='none'))
ax5.plot(x_a, f_lin)

for i in range(1,n):
    ax6.add_patch(Rectangle(((x_a[i]+x_a[i-1])/2, 0),1/n,f_quad[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax6.plot(x_a, f_quad)

for i in range(1,n):
    ax7.add_patch(Rectangle(((x_a[i]+x_a[i-1])/2, 0),1/n,f_cub[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax7.plot(x_a, f_cub)

for i in range(1,n):
    ax8.add_patch(Rectangle(((x_a[i]+x_a[i-1])/2, 0),1/n,f_exp[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax8.plot(x_a, f_exp)

for i in range(1,n+1):
    ax9.add_patch(Rectangle((x_a[i-1],0),1/n,f_lin[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax9.plot(x_a, f_lin)

for i in range(1,n+1):
    ax10.add_patch(Rectangle((x_a[i-1],0),1/n,f_quad[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax10.plot(x_a, f_quad)

for i in range(1,n+1):
    ax11.add_patch(Rectangle((x_a[i-1],0),1/n,f_cub[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax11.plot(x_a, f_cub)

for i in range(0,n):
    ax12.add_patch(Rectangle((x_a[i+1]-1/n,0),1/n,f_exp[i], linewidth = 2, ec = '#87cefa', fc  = 'none')) 
ax12.plot(x_a, f_exp)

plt.figtext(0.1025, 0.85, 'Relative error = {}%'.format(e_r[0,0]), ha='center')
plt.figtext(0.35, 0.85, 'Relative error = {}%'.format(e_r[1,0]), ha='center')
plt.figtext(0.60, 0.85, 'Relative error = {}%'.format(e_r[2,0]), ha='center')
plt.figtext(0.93, 0.85, 'Relative error = {}%'.format(e_r[3,0]), ha='center')

plt.figtext(0.1025, 0.55, 'Relative error = {}%'.format(e_r[0,1]), ha='center')
plt.figtext(0.35, 0.55, 'Relative error = {}%'.format(e_r[1,1]), ha='center')
plt.figtext(0.60, 0.55, 'Relative error = {}%'.format(e_r[2,1]), ha='center')
plt.figtext(0.93, 0.55, 'Relative error = {}%'.format(e_r[3,1]), ha='center')

plt.figtext(0.1025, 0.225, 'Relative error = {}%'.format(e_r[0,2]), ha='center')
plt.figtext(0.35, 0.225, 'Relative error = {}%'.format(e_r[1,2]), ha='center')
plt.figtext(0.60, 0.225, 'Relative error = {}%'.format(e_r[2,2]), ha='center')
plt.figtext(0.93, 0.225, 'Relative error = {}%'.format(e_r[3,2]), ha='center')

plt.figtext(0.1025, 0.88, 'Area = {}'.format(f_sum[0,0]), ha='center')
plt.figtext(0.35, 0.88, 'Area = {}'.format(f_sum[1,0]), ha='center')
plt.figtext(0.60, 0.88, 'Area = {}'.format(f_sum[2,0]), ha='center')
plt.figtext(0.93, 0.88, 'Area = {}'.format(f_sum[3,0]), ha='center')

plt.figtext(0.1025, 0.58, 'Area = {}'.format(f_sum[0,1]), ha='center')
plt.figtext(0.35, 0.58, 'Area = {}'.format(f_sum[1,1]), ha='center')
plt.figtext(0.60, 0.58, 'Area = {}'.format(f_sum[2,1]), ha='center')
plt.figtext(0.93, 0.58, 'Area = {}'.format(f_sum[3,1]), ha='center')

plt.figtext(0.1025, 0.255, 'Area = {}'.format(f_sum[0,2]), ha='center')
plt.figtext(0.35, 0.255, 'Area = {}'.format(f_sum[1,2]), ha='center')
plt.figtext(0.60, 0.255, 'Area = {}'.format(f_sum[2,2]), ha='center')
plt.figtext(0.93, 0.255, 'Area = {}'.format(f_sum[3,2]), ha='center')

plt.tight_layout()
plt.show()