# library
# standard library
import os

# third-party library
import torchvision
from pylab import *

# Mnist digits dataset
# if not(os.path.exists('./data/')) or not os.listdir('./MINIST/'):
#     # not mnist dir or mnist is empyt dir
#     DOWNLOAD_MNIST = True

trainset = torchvision.datasets.MNIST(
    root='./data/',
    train=True,  # this is training data
    transform=torchvision.transforms.ToTensor(),  # Converts a PIL.Image or numpy.ndarray to
    # torch.FloatTensor of shape (C x H x W) and normalize in the range [0.0, 1.0]
    # download=DOWNLOAD_MNIST,
)

print(trainset.data.size())                 # (60000, 28, 28)
print(trainset.targets.size())

plt.figure(1)
for i in range(0, 10):
    for j in range(0,6000):
        if trainset.targets[j]==i:break
    plt.subplot(2, 5, i + 1)
    plt.imshow(trainset.data[j].numpy(), cmap='gray')
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('手写%i' % trainset.targets[j])

plt.figure(2)
i=0
for j in range(0,6000):
    if trainset.targets[j]==7:
        i+=1
        plt.subplot(2, 5, i)
        plt.imshow(trainset.data[j].numpy(), cmap='gray')
    if i==10:break

plt.show()
