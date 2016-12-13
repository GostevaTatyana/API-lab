clear; clc;
[x,y]=meshgrid(-1:0.01:1);
z=f(x,y,25);
z1=f(x,y,7);
mesh(x,y,z), hold on, title('График');
mesh(x,y,z1);