(cover)


#title:
A Statistical Distance Derived From The Kolmogorov-Smirnov Test:
   specification, reference measures (benchmarks) and example uses


#authors:
Renato Fabbri, Fernando Gularte de León
renato.fabbri@gmail.com, fernandogularte@gmail.com
(ICMC/USP, Parque Tecnológico Industrial del Cerro)

#ENMC2017
(XX Encontro Nacional de Modelagem Computacional)
19/Out/2017


















=========================
(slide 1)

*Introduction*

c' is a statistical distance
derived from the Kolmogorov-Smirnov test.

d(x, y) >= 0
d(x, y) = 0  <=> x = y
d(x, y) = d(y, x)
d(x, y) <= d(x, z) + d(z, y)

c' is true or generalized.



=========================
(slide 2)

*Methods*

* D > c(a) . [ ( n + n') / (n . n') ]^0.5

* c' = D . [ n . n' / (n + n') ]^0.5

a    & 0.1  & 0.05 & 0.025 & 0.01 & 0.005 & 0.001
c(a) & 1.22 & 1.36 & 1.48  & 1.63 & 1.73  & 1.95 

=========================
(slide 3)

*Methods*

Benchmark tables of c' for the cases:

* When the null hypothesis is true

* When it is false

* c' values for real samples

* Automated by scripts and render
documentation

  	







=========================
(slide 4)

*Results*

* Tables for n=n'=1000,

* Emphasis for a.n when the null hypothesis is true

* Measures of c' when it is false

* c' for samples derived from texts, sound,
music, OS statistics




=========================
(slide 5)

*Results*

* Python scripts that render the tables

* Latex files that make the into a PDF

* Thorough description of the tables obtained

(See the tables in the article)




==========================
(slide 6)

*Conclusions*

* Useful and robust statistic (?)

* Reasonable collection of benchmark tables (?)

* Better organize scripts

* Account for the 2an rejections for power-law

* Compare c' to other statistical distances

* Better formalize when c' is a generalized
or true metric

* Reference values of c' for true null hypothesis

* Account for differences in the KS test
for discrete and continuous variables

* Make benchmark tables without using histograms

thanks: FAPESP, ICMC/USP, ENMC2017
