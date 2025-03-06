import matplotlib.pyplot as plt
import matplotlib.cm as cm


# 生成一些示例数据（参数量 params，准确率 Accuracy）
models = [
    "Event Histogram (Min)", "Event Histogram (Full)",
    "Voxel Grid (Min)", "Voxel Grid (Full)",
    "AET (Min)", "AET (Full)",
    "SCFR (Ours, Min)", "SCFR (Ours, Full)"
]

params = [0.06, 21.33, 0.08, 21.36, 0.08, 21.36, 0.25, 21.53]  # 参数量 (单位：Million)

accuracy = [48.46, 73.16, 68.70, 78.50, 27.13, 83.14, 78.50, 85.44]  # 准确率 (%)


# 设置颜色和点的大小
num_models = len(models)
cmap = cm.get_cmap('tab10')
colors = [cmap(i/10) for i in range(num_models)]

# 创建图表
plt.figure(figsize=(10, 6))
plt.scatter(params, accuracy, c=colors, s=150, edgecolors="black", alpha=0.8)

# 使用对数尺度表示x轴
plt.xscale('log')

# 调整文本标签位置，考虑对数尺度
for i, model in enumerate(models):
    # 在对数尺度下计算适当的文本位置
    text_x = params[i] * 1.2  # 在对数尺度上向右偏移20%
    plt.text(text_x, accuracy[i] - 0.5, model, fontsize=12, fontweight="bold")

# 轴标签和标题
plt.xlabel("Tunable Params (M, log scale)", fontsize=14)  # 更新标签说明对数尺度
plt.ylabel("N-Caltech 101 Top-1 Accuracy (%)", fontsize=14)
plt.title("Model Performance Comparison", fontsize=16, fontweight="bold")

# 美化网格和边界
plt.grid(True, linestyle="--", alpha=0.5)
# 不再显式设置x轴范围，让matplotlib自动处理对数尺度的范围
plt.ylim(min(accuracy) - 2, max(accuracy) + 2)  # 设置y轴范围

# 添加箭头和标注
plt.annotate("Better Models", xy=(1, 80), xytext=(2, 77),
             arrowprops=dict(arrowstyle="->", color="brown", lw=2), fontsize=12, color="brown")

# 显示图像
plt.show()