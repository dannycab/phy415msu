---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Course Design

For most of you, 4415 is an elective course that you are taking to learn more about how we use mathematical techniques in physics. As such, this course is designed under several different principles than a standard course. Below, I provide those principles and their rationale.

* 415 should help you learn the central tenets of modeling physical systems
  * The sheer volume of mathematical and computational physics knowledge out there is immense and impossible for any one person to learn. However, the central elements of making models, how to learn about specific techniques, and how to debug your approaches are things we can learn and employ broadly as well as to specific problems.
* 415 should be a celebration of your knowledge
	* For most of you, this course is part of your senior level coursework. What you have achieved in the last three to four years should be celebrated and enjoyed. This course will provide ample opportunities for you to share what things you know and what things you are learning with me and with each other.
* 415 should give you opportunities to engage in professional practice
	* As you start towards your professional career, it's important to learn what professional scientists do. You have probably already begun this work in advanced lab and research projects that you have worked on. We will continue developing your professional skills in this course through the use of course projects.
* 415 will illustrate that we can learn from each other
	* Even though I've been learning physics for almost 20 years, I don't know everything. I am excited to learn from you and I hope that you are excited to learn from me and each other.

## Optional purchases:

The core readings and work for this course will be this jupyterbook. I will find resources online, make my own, and provide as much organized free material as possible. If you want to have a textbook that helps you organize your readings, please obtain copies of:

1.  Mary Boas, [*Mathematical Methods in the Physical Sciences*](https://www.amazon.com/Mathematical-Methods-Physical-Sciences-Mary/dp/04711982) (Wiley; 2005). This book is the definitive text on mathematical approaches, written by Dr. Boas originally in 1966! Any 3rd edition will be useful and I will put the section numbers from Boas in the online readings.
2. Mark Newman, [*Computational Physics*](https://www.amazon.com/Computational-Physics-Mark-Newman/dp/1480145513) (CreateSpace Independent Publishing Platform; 2012). This book is a great introduction to a variety of computational physics techniques, written by UMich professor Mark Newman for a computational physics course. I will put section numbers from Newman in the online readings.

### Additional sources

In addition, I will draw from the following books. I have copies of them if you want or need scans of sections. But they can found online in Google Books and other places as well. no need to purchase unless you want a copy for your personal library.

#### Mechanics

* Edwin Taylor, Mechanics
* Jerry Marion and Stephen Thornton, Classical Dynamics of Particles and Systems
* Charles Kittel, Walter D. Knight, Malvin A. Ruderman, A. Carl Helholtz, and Burton J. Moyer, Mechanics
 
#### Electromagnetism

* Edward Purcell, Electricity and Magnetism
* David J. Grriffths, Introduction to Electromagnetism

#### Quantum Mechanics

* David McIntyre, Quantum Mechanics
* David J. Griffiths, Introduction to Quantum Mechanics

#### Waves and Thermal Physics

* Frank S. Crawford, Waves
* Charles Kittel, Thermal Physics
* Ashley Carter, Classical and Statistical Thermodynamics
* Daniel Schroeder, Thermal Physics

#### Additional Physics Topics

* Steven H. Strogatz, Nonlinear Dynamics and Chaos
* B Lautrup, Physics of Continuous Matter
* Frank L. Pedrotti and Leno S. Pedrotti, Introduction to Optics

#### Mathematics

* Susan M. Lea, Mathematics for Physicists
* William E. Boyce and Richard C. DiPrima, Elementary Differential Equations
* James Brown and Ruel Churchill, Complex Variables and Applications
* Jerrold Marsden and Anthony Tromba, Vector Calculus
* Sheldon Ross, A First Course in Probability

#### Presenting (Visual) Information

* Edward Tufte, The Visual Display of Quantitative information
* Albert Cairo, The Truthful Art
* Stephen E. Toulmin, The Uses of Argument

# Course Activities

## "Readings"

"Reading" is an essential part of 415! Reading the notes before class is very important. I use "reading" in quotes, because in our class this idea goes beyond just reading text and includes understanding figures and watching videos. These should help inform the basis of your understating that we will draw on in class to clarify your understanding and to help you make sense of the material. I will assume you have done the required readings in advance! It will make a huge difference if you spend the time and effort to carefully read and follow the resources posted. The
[calendar](./calendar.html) has the details on readings that will be updated.

## Class Meetings

**Classroom Etiquette:** Please silence your electronic devices when entering the classroom. I don't mind you using them (in fact, see below, we will use them). But, sometimes, they can very distracting to your neighbors, so use your judgement. I appreciate that you might have questions or comments about things in class. If you and your neighbors are confused, just raise your hand and ask. If you are confused, you are likely not the only one and it's better to chat about it, then move on. Questions in lecture are always good, and are strongly encouraged!

**Computing Devices:** Please bring some sort of computing device to class everyday. You might be researching information online, reviewing work you have done, or actively building models of systems together. This device can be a computer, a tablet, or a phone. You can also partner up with folks because we will use them in groups.

**In-Class Activities:** We will also use a variety of in-class activities and worksheets that help you construct an understanding of a particular topic or concept. These will not be collected or graded, but we will discuss the solutions in class.

## Homework

There will be a homework due every Friday by 5pm. Late homework can't be accepted once solutions are posted - but, your lowest score will be dropped. Homework is exceedingly important for developing an understanding of the course material, not to mention building skills in complex physical and mathematical problem solving. They will require considerable time and personal effort this term! *Your lowest homework grade will be dropped.*

There are four kinds of homework problems in this class:

**Standard Homework Problems**: These are regular back-of-the-book type homework problems that involve derivations, calculations, figures, and graphs. If you took 481, there will be fewer of these in 482. Each question will be coarsely graded for "completion":

* 10 pts. complete
* 8 pts. right idea, but incomplete
* 4 pts. relatively incomplete
* 0 pts. not turned in

**Computational Homework Problems:** There will be *some use of computation in this course* on homework problems. I will encourage and support the use of Python (through [Jupyter notebooks](http://jupyter.org/)). You do not need any computational experience for this course as you will learn some fundamentals early on and keep using them throughout the course. You are welcome to use any environment of your choosing (e.g., Octave/MATLAB, Mathematica, C++), but I will only provide support for Python. Python is in use across the sciences, but it is becoming much used in physics, so learning it will serve you well in your future work. I suggest downloading the [Anaconda distribution of Python](https://www.continuum.io/) as it comes with all the packages you will need to get up and running with Jupyter notebooks. These will be graded on the same 10-8-4-0 scale as standard homework problems. Here are [instructions for installing Jupyter Notebooks](http://jupyter.readthedocs.io/en/latest/install.html).

**Project Homework Problems**: These are homework problems to support your working towards completing your individual and paired projects (see below). *Projects are difficult to complete, so having some regular check-ins on how those projects are going, setting milestones to complete, and producing a semi-complete piece of a project are all important aspects of research!* These homework problems are meant to help you make that progress each week. They count twice as much as normal homework problems, but follow a similar grading scale:

* 20 pts. complete
* 16 pts. right idea, but incomplete
* 8 pts. relatively incomplete
* 0 pts. not turned in

You will be given detailed feedback on these project homework problems as you are working on bigger projects throughout this class. You should read and be responsive to this feedback as it will help you develop a strong project.

**Self-reflection Homework Problems**: These are homework problems that ask you to evaluate your progress on your projects and how you and your partner are working together. *Evaluating how well you understand something and what you need to do to move forward is a hard thing to learn. So is working on a team (or with a partner).* These homework problems are meant to help you do both and get feedback from me on how things are going. These problems are graded out of 10 points like regular homework problems on the same 10-8-4-0 scale. You will also be given detailed feedback on these homework problems.


*I strongly encourage collaboration*, an essential skill in science and engineering (and highly valued by employers!) Social interactions are critical to scientists' success -- most good ideas grow out of discussions with colleagues, and essentially all physicists work as part of a group. Find partners and work on homework together. However, it is also important that you OWN the material. I strongly suggest you start homework by yourself (and that means really making an extended effort on every problem). Then work with a group, and finally, finish up on your own -- write up your own work, in your own way. There will also be time for peer discussion during classes -- as you work together, try to help your partners get over confusions, listen to them, ask each other questions, critique, teach each other. You will learn a lot this way! For all assignments, the work you turn in must in the end be your own: in your own words, reflecting your own understanding. (If, at any time, for any reason, you feel disadvantaged or isolated, contact me and I can discretely try to help arrange study groups.)

### Help Session

Help sessions/office hours are to facilitate your learning. We encourage attendance - plan on working in small groups, our role will be as learning coaches. The sessions are homework-centric, but we will not be explicitly telling anyone how to do the homework (how would that help you learn?) I strongly encourage you to start all problems on your own. If you come to help sessions "cold", the value of homework to you will be greatly reduced.
