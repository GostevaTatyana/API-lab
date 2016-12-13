function S = f(x,y,a)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
S=atan(sqrt(abs((x-sin(y))./(x+sin(y))+(x+sin(y))/(x-sin(y)))))+a.*exp((x-sin(y)).*(x+sin(y)));

end

