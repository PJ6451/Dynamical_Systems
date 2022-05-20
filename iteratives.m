function A = iteratives(a,k,range)
    x   = range(1):0.0001:range(2); 
    mid = 0;
    xn  = zeros(size(x,2),k);
    for i=1:k
        if i == 1
            xn(:,i) = rpop(a,x);
        else
            xn(:,i) = rpop(a,xn(:,i-1));
        end
    end
    iter = cell(size(xn,1),k);
    for i=1:k
        for j=1:size(xn,1)
            if xn(j,i) > mid
                iter{j,i} = 'R';
            else
                iter{j,i} = 'L';
            end
        end
    end
    iter2 = cell(size(xn,1),1);
    for j=1:size(iter,1)
        for i=1:k
            iter2{j,1} = strcat(iter2{j,1},iter{j,i});
        end
    end
    xn = num2cell(xn);
    A = [xn,iter2];
    T = cell2table(A,'VariableNames',{'FirstIter' 'SecondIter' 'ThirdIter' 'Iteratives'});
    filename = 'C:\Users\16617\OneDrive\Documents\MATLAB\Chaos Scripts\iterates.xlsx';
    writetable(T,filename,'Sheet',1,'Range','A1')
end



function y = rpop(a,x)
    y = a-x.^2;
end