import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 启用 Seaborn 论文风格
sns.set_context("paper")
sns.set_style("whitegrid")

# 数据
models = [
    "Event Histogram (Min)", "Event Histogram (Full)",
    "Voxel Grid (Min)", "Voxel Grid (Full)",
    "AET (Min)", "AET (Full)",
    "SAPE (Ours, Min)", "SAPE (Ours, Full)", "EST (Min)", "EST (Full)"
]
params = np.array([0.06, 21.33, 0.08, 21.36, 0.08, 21.36, 0.11, 21.39, 0.11, 21.28])  # 参数量 (M)
accuracy = np.array([48.46, 73.16, 68.70, 78.50, 74.70, 83.14, 80.50, 85.44, 73.93, 81.70])  # 准确率 (%)

# 颜色方案（使用 magma 颜色渐变）
colors = sns.color_palette("magma_r", len(models))

# 创建图表
plt.figure(figsize=(8, 5))

# 绘制散点图
plt.scatter(params, accuracy, c=colors, marker="o", s=200, edgecolors='black', alpha=0.85)

# 手动调整文本标签的偏移量
offsets = [
    (15, 8), (-20, -8),  # Event Histogram (Min/Full)
    (15, 5), (-20, -5),  # Voxel Grid (Min/Full)
    (15, 10), (-20, 0),  # AET (Min/Full)
    (20, 7), (-25, 0),  # SAPE (Ours, Min/Full)
    (15, 0), (-22, -6)  # EST (Min/Full)
]

# 在数据点旁边添加模型名称，避免重叠
for i, model in enumerate(models):
    ha = "left" if "Min" in model else "right"  # Min 在右，Full 在左
    va = "bottom" if i % 2 == 0 else "top"  # 交替调整垂直对齐
    offset_x, offset_y = offsets[i]  # 获取对应的偏移值

    plt.annotate(model, (params[i], accuracy[i]), fontsize=10, fontweight="bold",
                 xytext=(offset_x, offset_y), textcoords="offset points",
                 ha=ha, va=va, fontname="Arial")

# 对数刻度（log scale）
plt.xscale("log")
plt.xlabel("Tunable Parameters (M, log scale)", fontsize=14, fontname="Arial")
plt.ylabel("N-Caltech 101 Top-1 Accuracy (%)", fontsize=14, fontname="Arial")
plt.title("Representation Performance Comparison", fontsize=16, fontweight="bold", fontname="Arial")

# 美化网格和边界
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlim(min(params) / 2, max(params) * 2)
plt.ylim(min(accuracy) - 5, max(accuracy) + 5)

# 添加方向指示箭头
plt.annotate("Better Models", xy=(1.0, 40), xytext=(10, 30),
             arrowprops=dict(arrowstyle="->", color="brown", lw=2),
             fontsize=12, color="brown", fontweight="bold", fontname="Arial")

# 保存高清图片
plt.tight_layout()
plt.savefig("./fig/scatter_plot_manual_adjusted.png", dpi=300, bbox_inches="tight")

# 显示图像
plt.show()
