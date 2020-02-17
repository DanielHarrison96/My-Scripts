%function[Z]=conditionsgrid(N)%
%condtionsgrid%
x=0.01:0.01:2; %length 50%
y=0.01:0.001:1; %length 100%
[X,Y] = meshgrid(x,y);
G=ones(1,200);
Z=(G./(2.*X)).*(X-sqrt((1-X-Y).^2+4.*Y)).*(1+X+Y-sqrt((1-X-Y).^2+4.*Y));% c=C , d=Y%
A=Z<0.4;
image(A,'CDataMapping','scaled')
colorbar


