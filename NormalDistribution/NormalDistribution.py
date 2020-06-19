import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 200)
f = np.exp((-(x**2))/2)

fig, ax = plt.subplots()

ax.plot(x, f, c='black', linewidth=2)


# Vertical lines in the plot
ax.plot([0,0], [0,1], c='black', alpha=.5)
ax.plot([1,1], [0,np.exp((-(1**2))/2)], c='black', alpha=.5)
ax.plot([-1,-1], [0,np.exp((-(1**2))/2)], c='black', alpha=.5)
ax.plot([2,2], [0,np.exp((-(2**2))/2)], c='black', alpha=.5)
ax.plot([-2,-2], [0,np.exp((-(2**2))/2)], c='black', alpha=.5)

# Lines below the plot
ax.plot([0,0], [-.25, -.3], c='black')
ax.plot([.25335,.25335], [-.25, -.3], c='black')
ax.plot([.5244,.5244], [-.25, -.3], c='black')
ax.plot([.84162,.84162], [-.25, -.3], c='black')
ax.plot([1.28155,1.28155], [-.25, -.3], c='black')
ax.plot([2.32634,2.32634], [-.25, -.3], c='black')
ax.plot([-.25335,-.25335], [-.25, -.3], c='black')
ax.plot([-.5244,-.5244], [-.25, -.3], c='black')
ax.plot([-.84162,-.84162], [-.25, -.3], c='black')
ax.plot([-1.28155,-1.28155], [-.25, -.3], c='black')
ax.plot([-2.32634,-2.32634], [-.25, -.3], c='black')

# x-axis
ax.plot([-4,4], [0,0], c='black')

# Deviation text
ax.text(-2.9, .75, r'$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} $', size=15)
ax.text(0, -.075, '$\mu$', ha='center')
ax.text(1, -.075, '$\mu + \sigma$', ha='center')
ax.text(-1, -.075, '$\mu - \sigma$', ha='center')
ax.text(2, -.075, '$\mu + 2\sigma$', ha='center')
ax.text(-2, -.075, '$\mu - 2\sigma$', ha='center')
ax.text(.5, .125, '$34.13\%$', ha='center')
ax.text(-.5, .125, '$34.13\%$', ha='center')
ax.text(1.5, .125, '$13.59\%$', ha='center')
ax.text(-1.5, .125, '$13.59\%$', ha='center')

#Percentiles text
ax.text(-2.32634, -.375, '$1$', ha='center')
ax.text(-1.28155, -.375, '$10$', ha='center')
ax.text(-.84162, -.375, '$20$', ha='center')
ax.text(-.5244, -.375, '$30$', ha='center')
ax.text(-.25335, -.375, '$40$', ha='center')
ax.text(0, -.375, '$50$', ha='center')
ax.text(2.32634, -.375, '$99$', ha='center')
ax.text(1.28155, -.375, '$90$', ha='center')
ax.text(.84162, -.375, '$80$', ha='center')
ax.text(.5244, -.375, '$70$', ha='center')
ax.text(.25335, -.375, '$60$', ha='center')

ax.set_aspect(2)
ax.set_xlim(-3, 3)
ax.set_ylim(-.5, 1.5)
plt.axis('off')

plt.show()
