# `sde` - solving nonlinear stochastic differential equation

Here we have implemented solution of nonlinear SDE:

<p align="center">
![d x = \left(\eta - \frac{\lambda}{2} \right) x^{2 \eta - 1} d t + x^\eta d W](./eqs/sde.png)
</p>

In this context "solution" is understood as obtaining single sample
trajectory of desired length and discretization time step.

The numerical solution is obtained by solving Bessel process SDE:

<p align="center">
![d y = \frac{\lambda - \eta}{2 \left( \eta - 1 \right)} \cdot \frac{d t}{y} + d W](./eqs/bessel.png)
</p>

and applying nonlinear transformation:

<p align="center">
![x = \left[ \left( \eta - 1 \right) y \right]^\frac{1}{1-\eta}](./eqs/transform.png)
</p>

to obtain the solutions of the nonlinear SDE above.

Bessel process is solved using Euler-Maruyama method with variable time step.