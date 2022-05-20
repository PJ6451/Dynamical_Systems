clear
clc
tic
Niterates = 50;
NGridSize = 200;

a = linspace(-2.4, 1.2, NGridSize);
b = linspace(-1.5, 1.5, NGridSize);
B = [];
W = [];
for j = 1:NGridSize
    for k = 1:NGridSize
        z0 = 0 + 0*1i;
        for m = 1:Niterates
            z1 = z0^2+(a(j)+b(k)*1i);
            z0 = z1;
            x = real(z0);
            y = imag(z0);
            mag = sqrt(x^2 + y^2);
            if mag <= 4
            else
                break
            end
        end
        if mag <= 4
            B = [B; a(j),b(k)];
        elseif mod(m,2) == 0
            B = [B; a(j),b(k)];
        else
            W = [W; a(j),b(k)];
        end
    end
end

% scatter(W(:,1),W(:,2),'w','filled')
% hold on
scatter(B(:,1),B(:,2),'k','filled')
hold on
scatter(W(:,1),W(:,2),'w','filled')
toc
