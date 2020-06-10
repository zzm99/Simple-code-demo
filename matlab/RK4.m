function [t, y] = RK4(f, tspan, y0, h)

a = tspan(1); b = tspan(2); n = (b-a)/h;
t = (a+h : h : b);
k1 = feval(f, a, y0);
k2 = feval(f, a+h/2, y0+k1/2*h);
k3 = feval(f, a+h/2, y0+k2/2*h);
k4 = feval(f, a+h, y0+k3*h);
y(1) = y0 + (k1/6 + k2/3 + k3/3 + k4/6)*h;
for i = 1 : n-1
    k1 = feval(f, t(i), y(i));
    k2 = feval(f, t(i)+h/2, y(i)+k1/2*h);
    k3 = feval(f, t(i)+h/2, y(i)+k2/2*h);
    k4 = feval(f, t(i)+h, y(i)+k3*h);
    y(i+1) = y(i) + (k1/6+k2/3+k3/3+k4/6)*h;
end
t = [a t]; y = [y0 y];
disp('   step        t               y')
k = 1:length(t); out = [k; t; y];
fprintf('%5d   %15.10f   %15.10f\n', out)


    
