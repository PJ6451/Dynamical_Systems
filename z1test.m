% Z1TEST  Gottwald-Melbourne 0-1 test for chaos
% 
% Z1TEST(X) is the result of the 0-1 test applied to the vector X.
% Result is near to 0 for non-chaotic data and near 1 for chaotic data.
% see  http://arxiv.org/pdf/0906.1418v1.  Paul Matthews, July 2009.
function kmedian=z1test
x = zeros(1,5000);
c = -1.9;
x(1) = 0.2;
for i=2:5000
    x(i) = x(i-1)^2+c;
end

s=size(x);

if s(2)==1 
    x=x'; 
end

N=length(x); 
j=1:N;
t=1:round(N/10);
M=zeros(1,round(N/10));
c=pi/5+rand(1,100)*3*pi/5; % 100 random c values in [pi/5,4pi/5]

for its=1:100
   p=cumsum(x.*cos(j*c(its)));
   q=cumsum(x.*sin(j*c(its)));
%    plot(p,q);xlabel('p');ylabel('q');
   for n=1:round(N/10)
      M(n)=mean( (p(n+1:N)-p(1:N-n)).^2 + (q(n+1:N)-q(1:N-n)).^2 )- ...
           mean(x)^2*(1-cos(n*c(its)))/(1-cos(c(its)));
   end
   kcorr(its)=corr(t',M');
end

% useful diagnostic plots
 plot(c,kcorr,'*');xlabel('c');ylabel('k'); 
%  plot(t,M);xlabel('t');ylabel('D')

% Two crude attempts to check for oversampling:
if (max(x)-min(x) )/mean(abs(diff(x))) > 10 || ...
       median(kcorr(c<mean(c))) - median(kcorr(c>mean(c))) > 0.5
   disp('Warning: data is probably oversampled.')
   disp('Use coarser sampling or reduce the maximum value of c.')
end

kmedian=median(kcorr);