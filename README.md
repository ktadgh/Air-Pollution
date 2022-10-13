We have the differential equation:
$$
\frac{\delta}{\delta t} U = D\frac{\delta ^{2}}{\delta x^{2}}-v \frac{\delta}{\delta x}.
$$
We can use the first and second order central difference for $x$, which gives us: 
$$
\frac{\delta}{\delta t} U = D\frac{U_{m-1} - 2U_{m}+U_{m+1}}{(\Delta x)^{2}}- v \frac{U_{m+1} - U_{m-1}}{2 \Delta x}
$$
And using forward Euler for time gives:
$$
\frac{U_{m}^{n+1} - U_m^n}{\Delta t} = D\frac{U_{m-1} - 2U_{m}+U_{m+1}}{(\Delta x)^{2}}- v \frac{U_{m+1} - U_{m-1}}{2 \Delta x}
$$
Now we let
$$
\begin{align}
C = \frac{D \Delta t}{ (\Delta x)^2}\\
B = \frac{ v \Delta t }{ 2 \Delta x },
\end{align}
$$
which gives us:
$$
U_{m}^{n+1} = U_{m}^{n} + C(U_{m-1}^{n} - 2U_{m}^{n} + U_{m+1}^{n}) - B(U_{m+1}^{n} - U_{m-1}^{n}).
$$

Which we can write as
$$
U_{m}^{n+1} = (1 - 2C)U_{m}^{n} + (C+B)U_{m-1}^{n} + (C- B)U_{m+1}^n
$$
Which gives us the steps to take in our numerical solution.