function[u]=onedheat(u0)
N=12;
Tend=10;
x=linspace(-0.1,1.1,13);
t=linspace(0,1,11);
%time and space differences%
dt=0.1;
dx=0.1;
mu=dt/(dx).^2;
[X,T]=meshgrid(x,t);
I=eye(N+2);
l=ones(N+1,1);
l=ones(N+1,1);
U=-mu*diag(l,1);
L=-mu*diag(l,-1);
A=(1+2*mu).*I+U+L;
%u(:,1)=zeros(14,1)%;
u(:,1)=[0,0,0,0,0,1,1,1,1,1,0,0,0,0];
u(:,2)=A\u(:,1);
for i=1:N+1
    u(:,i+1)=A\u(:,i);
end
figure
pcolor(u)
colorbar
shading interp;
axis equal tight;







