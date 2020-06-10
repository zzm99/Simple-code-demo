% 以下为一次插值建模的代码 全部代码可见于报告pdf
y = [1783.7151; 1895.0712; 1996.7213];
t = [0 0 1; 1 1 1; 4 2 1];
z = pinv(t)*y

y = -4.9*3^2 + 116.2*3 + 1783.7

t = 0:0.01:3;
y = -4.9*t.^2 + 116.2*t + 1783.7;
plot(t,y)

y = [886.1973; 967.1026; 1525.1511];
t = [0 0 1; 1 1 1; 4 2 1];
z = pinv(t)*y

y = 238.5716*3^2 -157.6663*3 + 886.1973

t = 0:0.01:3;
y = 238.5716*t.^2 -157.6663*t + 886.1973;
plot(t,y)

t = 0:0.01:3;
x = -4.9*t.^2 + 116.2*t + 1783.7;
y = 238.5716*t.^2 -157.6663*t + 886.1973;
plot(x,y)
