#!/usr/bin/env python
# coding: utf-8

# # 18 Oct 2022 - Introduction to Waves
# 
# As we have built up an analysis of 1D SHOs that started to show complex motion. That is, as we added more and more oscillators, more "kinds" of motion became possible. We saw that in the increasing number and complexity of the normal modes. But what happens at the limit of infinitely many, small oscillators - like a continuously flexible object - a rope or string, for example. 
# 
# Here, enters a new model. One that has existed for a long time and was used widely in the 19th century to develop one of our most complete theories of physics to date: [Classical Electrodynamics](https://en.wikipedia.org/wiki/Maxwell%27s_equations). We will begin our work with a reminder of these equations and their uses, and then derive the wave equation from them, and characterize solutions to it.

# ## Reminders of Maxwell's Equations
# 
# My E&M professor in undergrad, Richard Hazeltine, told us that every physicist should be able to recite Maxwell's equations in their sleep. I don't know what Richard was doing in his sleep, but I tend to actually sleep not recite equations. But in any event, here they are in differential and integral form for a vacuum:
# 
# ### Differential Form (Vacuum)
# 
# #### Gauss's Law
# 
# $$\nabla \cdot \mathbf{E} = \dfrac{\rho}{\varepsilon_0}$$
# 
# #### Faraday's Law
# 
# $$\nabla \times \mathbf{E} = -\dfrac{d\mathbf{B}}{dt}$$
# 
# #### No Specific Name ("Gauss's Law for Magnetism"; No Magnetic Monopoles)
# 
# $$\nabla \cdot \mathbf{B}  = 0$$
# 
# #### Ampere's Law (with the Maxwell Correction)
# 
# $$\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \varepsilon_0 \mu_0 \dfrac{d\mathbf{E}}{dt}$$
# 
# ### Integral Form (Vacuum)
# 
# #### Gauss's Law
# 
# $$\iint \mathbf{E} \cdot d\mathbf{A} = \iiint \dfrac{\rho}{\varepsilon_0} dV$$
# 
# #### Faraday's Law
# 
# $$\oint \mathbf{E} \cdot d\mathbf{l} = -\iint \dfrac{d\mathbf{B}}{dt} \cdot d\mathbf{A}$$
# 
# #### No Specific Name ("Gauss's Law for Magnetism"; No Magnetic Monopoles)
# 
# $$\iint \mathbf{B} \cdot d\mathbf{A} = 0$$
# 
# #### Ampere's Law (with the Maxwell Correction)
# 
# $$\oint \mathbf{B}\cdot d\mathbf{l} = \iint \left(\mu_0 \mathbf{J}  + \varepsilon_0 \mu_0 \dfrac{d\mathbf{E}}{dt}\right) \cdot d\mathbf{A}$$

# ## Static/Steady Situations
# 
# Consider two situations that you have likely seen in the past. 
# 
# 1. The charges are static, glued to the outside surface of a solid tube (radius, $R$) that is very long ($L>>R$). Using Gauss's Law, find the electric field inside and outside the tube if a total amount $Q$ is glued uniformly around that tube.
# 2. Change the tube to a metal, that has a total charge $Q$ distributed throughout it's volume. The charges move steadily along the tube with a drift speed $v_d$ such that they produce a steady current density: $\mathbf{J}(\mathbf{r},t) = \mathbf{J}(\mathbf{r})$. Using Ampere's Law, find the magnetic field inside and outside the tube. _Recall the definition of a volume current density as the charge that passes a slice of the tube per unit time per unit area._

# ## What happens if there's no sources?
# 
# $$\nabla \cdot \mathbf{E} = 0$$
# 
# $$\nabla \times \mathbf{E} = -\dfrac{d\mathbf{B}}{dt}$$
# 
# $$\nabla \cdot \mathbf{B}  = 0$$
# 
# $$\nabla \times \mathbf{B} =  \varepsilon_0 \mu_0 \dfrac{d\mathbf{E}}{dt}$$

# 
