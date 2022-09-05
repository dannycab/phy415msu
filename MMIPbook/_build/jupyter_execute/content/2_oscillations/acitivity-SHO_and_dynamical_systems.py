#!/usr/bin/env python
# coding: utf-8

# # Outline
# 
# - Introduce SHO model and ansatz
#     - Activity (Familiar Idea): 
#         - Show the ansatz works
#         - Solve two particular cases (and compare)
#         - What do you know about this solution and implications?
#             - Where does that knowledge come from?
#             - Can you make visualizations of that knowledge?
#     - Activity (New Idea)
#         - Introduce phase space (family of solutions)
#             - Example: constant force; drag in 1d
#             - Focus on technical aspects and interpretation
#             - Give chance to play (adjust parameters)
#         - Do harmonic oscillator yourself
#             - Build map
#             - Explain
#             - Play
#             - Extend (add drag?)

# We have seen for the canonical one-dimensional harmonic oscillator is described by the following **2nd order linear** differential equation:
# 
# $$m\ddot{s} = -k{s}$$
# 
# where $s$ represents the distance from the oscillators equilibrium position. It's important to note that this model for a linear restoring force gives rise to at **second order** differential equation. As you will see, there would be no ability for cycles or recurrent behavior without two dimensions (the two dimensions here are the position, $s$, and velocity of the oscillator, $\dot{s}$). It is also important that the differential equation is **linear**.
# 
# ## Linearity of differential equations
# 
# This is something that is easy to confuse because we use the term **linear** in different ways at different times. In many cases this prompts us to think of a line, so that we might think the only linear differential equations are ones where the variable of interest (in this case the position of the oscillator) appears only *linearly* in the equation. So you might think:
# 
# ```admonition
# Nth order differential equations of the form:
# $$\dfrac{d^n x}{dt^n} == c\;x$$
# are the only ones that are linear. Note for the harmonic oscillator $n=2$.
# ```
