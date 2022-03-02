# `pyNSDE` - solving nonlinear stochastic differential equation

Here we have implemented solution of nonlinear SDE:

<div align="center">
  <img alt="d x = \left(\eta - \frac{\lambda}{2} \right) x^{2 \eta - 1} d t + x^\eta d W" src="./eqs/sde.png"/>
</div>

In this context "solution" is understood as obtaining single sample
trajectory of desired length and discretization time step.

The numerical solution is obtained by solving Bessel process SDE:

<div align="center">
  <img alt="d y = \frac{\lambda - \eta}{2 \left( \eta - 1 \right)} \cdot \frac{d t}{y} + d W" src="./eqs/bessel.png"/>
</div>

and applying nonlinear transformation:

<div align="center">
  <img alt="x = \left[ \left( \eta - 1 \right) y \right]^\frac{1}{1-\eta}" src="./eqs/transform.png"/>
</div>

to obtain the solutions of the nonlinear SDE above.

Bessel process is solved using Euler-Maruyama method with variable time step.
