function cobweb(a,x0,len)
    plotpop(a,len);
    NIter = 100;
    y     = zeros(NIter,1);
    for i = 1:NIter
        y(i) = rpop(a,x0);
        if i == 1
            plotcob1(x0,y(i,1))
        else
            plotcob(x0,y(i,1))
        end
%         if i > 10
%             if ismember(x0,y)
%                 break
%             end
%         end
        x0 = y(i,1);
    end
%     disp(i)
end

function y = rpop(a,x)
    %y = a.*x;
    y = abs(x-1);
%     y = (a.*x-x.^3)./2;
end

function plotpop(a,len)
    x = len;
    y = rpop(a,x);
    plot(x,y,'b')
    hold on;
    ax = gca;
    ax.XAxisLocation = 'origin';
    ax.YAxisLocation = 'origin';
    plot(x,x,'k')
end

function plotcob1(x,y)
    line([x,x],[0,y],'Color','red','LineStyle','--');
    hold on;
    line([x,y],[y,y],'Color','red','LineStyle','--');
end

function plotcob(x,y)
    line([x,x],[x,y],'Color','red','LineStyle','--');
    hold on;
    line([x,y],[y,y],'Color','red','LineStyle','--');
end