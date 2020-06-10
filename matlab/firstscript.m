for i=1:10
    x = linspace(0,10,101);
    plot(x,sin(x+i));
    %print(gcf,'-deps',strcat('plot',num2str(i),'.ps'));
end

