clear all; 
clc;
x=0:0.001:2;
Y1 = s(x);
plot(x,Y1), grid on,  hold on;
Y2 = c(x);
plot(x,Y2), grid on,  hold on;
%x0=-0.6;%нач.приближение
x1=fzero(@f,1);
plot(x1,s(x1),'or');