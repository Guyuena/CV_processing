from tkinter import Image

import torch
from matplotlib import transforms, pyplot as plt


def multibox_prior(data, sizes, ratios):
    in_height, in_width = data.shape[-2:]
    device = data.device
    num_sizes, num_ratios = len(sizes), len(ratios)
    boxes_per_pixel = num_sizes + num_ratios - 1  # 每个像素的anchor数量

    size_tensor = torch.tensor(sizes, device=device)
    ratio_tensor = torch.tensor(ratios, device=device)

    offset_h, offset_w = 0.5, 0.5
    # 归一化
    steps_h = 1.0 / in_height
    steps_w = 1.0 / in_width

    # 计算中心偏移
    center_h = (torch.arange(in_height, device=device) + offset_h) * steps_h
    center_w = (torch.arange(in_width, device=device) + offset_w) * steps_w
    shift_y, shift_x = torch.meshgrid(center_h, center_w)
    shift_y, shift_x = shift_y.reshape(-1), shift_x.reshape(-1)

    # 由于一个像素对应boxes_per_pixel个anchor，交叉重复boxes_per_pixel次
    out_grid = torch.stack([shift_x, shift_y, shift_x, shift_y], dim=1).repeat_interleave(boxes_per_pixel, dim=0)

    # 计算在一个像素处，anchor左上、右下坐标相对于像素中心的偏移
    # 下面在计算w时，为了处理矩形的情况,需要* in_height / in_width
    w = torch.cat(
        (size_tensor * torch.sqrt(ratio_tensor[0]), sizes[0] * torch.sqrt(ratio_tensor[1:]))) * in_height / in_width
    h = torch.cat((size_tensor / torch.sqrt(ratio_tensor[0]), sizes[0] / torch.sqrt(ratio_tensor[1:])))

    anchor_manipulations = torch.stack((-w, -h, w, h)).T.repeat(in_height * in_width, 1) / 2

    output = out_grid + anchor_manipulations
    return output.unsqueeze(0)
img_get = Image.open("3.jpg")  # 读取图片
plt.imshow(img_get , cmap=plt.cm.binary)
# plt.show()
print(img_get)
trans = transforms.Compose([  # 将所有的transform操作合并在一起执行
transforms.Compose([transforms.ToTensor()])
])
img = img_get.convert("RGB")
img =trans(img)
img = torch.unsqueeze(img, dim=0)
print(img.shape)
h, w = img.shape[-2:]
print(h, w)
# 构建与图像大小一直的锚框模板
X = torch.rand(size=(1, 3, h, w))

print("X.shape",X.shape)
print("X",X)
# 生成锚框 每个坐标生成5个框
Y = multibox_prior(X, sizes=[0.75, 0.5, 0.25], ratios=[1, 2, 0.5])
print("Y",Y)
print(Y.shape)
