import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import numpy as np
from spikingjelly.datasets.dvs128_gesture import DVS128Gesture
from spikingjelly.datasets.cifar10_dvs import CIFAR10DVS

root_dir = '/data1/tyk/datasets/DVSGesture'
dataset_dir = '/data1/tyk/datasets/CIFAR10DVS'


# CIFAR[0]
# train_set = DVS128Gesture(root_dir, train=True, data_type='event')
dataset_trainval = CIFAR10DVS(root=dataset_dir)

events, label = dataset_trainval[0]

# events, label = train_set[500]

x = events['x'].reshape(events['x'].shape[0],1)
y = events['y'].reshape(events['x'].shape[0],1)
p = events['p'].reshape(events['x'].shape[0],1)
t = events['t'].reshape(events['x'].shape[0],1)

data = np.concatenate([t,x,p,y],axis=1)

# 提取数据
x = data[0:5000, 0]
y = data[0:5000, 1]
z = data[0:5000, 3]
colors = ['green' if i == 1 else 'blue' for i in data[0:5000, 2]]
print(x)
print(y)
print(z)
# 绘制三维散点图
fig = plt.figure(figsize=(15, 15),dpi=300)
ax = fig.add_subplot(111, projection='3d')

# 设置散点的大小和颜色
scatter = ax.scatter(x, y, z, c=colors, s=1)

# ax.set_xlim(0, 128)
# ax.set_ylim(0, 128)
# ax.set_zlim(0, 1300000)
ax.set_box_aspect([10, 2, 2])

ax.view_init(elev=8, azim=86)

y_tick = np.linspace(0,40,3)
plt.yticks(y_tick)
plt.gca().invert_xaxis()

plt.rcParams['axes.facecolor'] = 'white'
fig.patch.set_facecolor('white')
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))


# 设置坐标轴标签
ax.set_xlabel('t',fontsize = 16)
ax.set_ylabel('x',fontsize = 16)
ax.set_zlabel('y',fontsize = 16)
# plt.xlabel('t',fontsize = 20)
# plt.ylabel('x',fontsize = 20)
# plt.clabel('y',fontsize = 20)


# plt.show()
plt.savefig('/home/tyk/EventAug/EventAug/Plot/scatter_plot.png',dpi=300)

