clear
clc

Niterates   = 700;
Nlambda     = 1000;
Ntransients = 500;

%  ---------  Initial Conditions  ---------
lambda_min = -2.4;
lambda_max = 1.2;
xmin       = -5.0;
xmax       = 5.0;
t          = zeros(Niterates,Nlambda);
v          = zeros(Niterates,Nlambda);

for k=1:Nlambda
  lambda = lambda_min + (lambda_max-lambda_min)*(k-1)/(Nlambda-1);

  %  ---------  Transients  ---------
  x0 = 0.1237;
  for i=1:Ntransients
    x1 = x0^2 - lambda;
    x0 = x1;
  end
  
  %  ---------  Iterate  ---------
  for j=1:Niterates
    x1     = x0^2 - lambda;
    x0     = x1;
    t(j,k) = lambda;
    v(j,k) = x1;
  end
end

plot(t,v,'k.','Markersize',4);
xlabel('{\lambda}');
ylabel('{x_n}');
set(gca,'FontSize',12);
grid on;
axis equal