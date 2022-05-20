clear
close
clc

b=.5;
x = -2:0.1:2;
y1 = 1-b.*x;
y2 = exp(-x);

plot(x,y1,'b')
hold on
plot(x,y2,'r')
xlabel('u','FontSize',14)
title(sprintf('Fixed Points for b = %f',b),'FontSize',14)
legend('1-bu','exp(-u)','location','northeast')
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
xlim([-2,2])
ylim([-1,3])
