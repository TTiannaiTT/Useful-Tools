import matplotlib.pyplot as plt
import numpy as np

# 生成一些示例数据（参数量 MACs，准确率 Accuracy）
models = ["Model A", "Model B", "Model C", "Model D", "Model E"]
macs = [1.0, 2.5, 4.0, 6.0, 8.5]  # 参数量 (单位：Billion)
accuracy = [72, 75, 78, 80, 81]  # Top-1 准确率 (%)

# 设置颜色和点的大小
colors = ["red", "blue", "green", "orange", "purple"]

# 创建图表
plt.figure(figsize=(10, 6))
plt.scatter(macs, accuracy, c=colors, s=150, edgecolors="black", alpha=0.8)

# 添加文本标签
for i, model in enumerate(models):
    plt.text(macs[i] + 0.2, accuracy[i] - 0.5, model, fontsize=12, fontweight="bold")

# 轴标签和标题
plt.xlabel("MACs (Billion)", fontsize=14)
plt.ylabel("ImageNet Top-1 Accuracy (%)", fontsize=14)
plt.title("Model Performance Comparison", fontsize=16, fontweight="bold")

# 美化网格和边界
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlim(0, max(macs) + 2)  # 设置 x 轴范围
plt.ylim(min(accuracy) - 2, max(accuracy) + 2)  # 设置 y 轴范围

# 添加箭头和标注
plt.annotate("Better Models", xy=(6, 80), xytext=(7, 77),
             arrowprops=dict(arrowstyle="->", color="brown", lw=2), fontsize=12, color="brown")

# 显示图像
plt.show()
