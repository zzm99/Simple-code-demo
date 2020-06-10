# -*- coding:utf-8 -*-
import torch.nn as nn
import torch
import matplotlib.pyplot as plt
import imageio

torch.manual_seed(0)
num_samples = 100

x_train = torch.linspace(0, 1, num_samples)
y_train = 0.1 * x_train + 0.2 + torch.randn(num_samples)*0.03

w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD([w,b], lr=0.01)

images = []
num_epochs = 4000
for epoch in range(num_epochs):
    y_pred = w * x_train + b
    loss = criterion(y_pred, y_train)
    optimizer.zero_grad()
    loss.backward()
    if epoch % 100 == 99:
        plt.figure()
        plt.ylim(torch.min(y_train).item(), torch.max(y_train).item())
        plt.scatter(x_train.tolist(), y_train.tolist(), marker='.')
        plt.plot(x_train.tolist(), y_pred.tolist(), color='r', linewidth=2)
        plt.title('Epoch [{}/{}], Loss: {:.6f}, \n Weight: {:.6f}, Bias: {:.6f}'
                  .format(epoch+1, num_epochs, loss.item(), w.item(), b.item()))
        plt.savefig('a.png')
        plt.close()
        images.append(imageio.imread('a.png'))
    optimizer.step()
    
imageio.mimsave('gen.gif', images, duration=0.5)
