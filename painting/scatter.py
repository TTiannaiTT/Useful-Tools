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
    "SCFR (Ours, Min)", "SCFR (Ours, Full)"
]
params = np.array([0.06, 21.33, 0.08, 21.36, 0.08, 21.36, 0.25, 21.53])  # 参数量 (M)
accuracy = np.array([48.46, 73.16, 68.70, 78.50, 27.13, 83.14, 78.50, 85.44])  # 准确率 (%)

# 颜色方案（使用 Viridis 颜色渐变）
colors = sns.color_palette("magma_r", len(models))

# 创建图表
plt.figure(figsize=(8, 5))

# 绘制散点图（统一 Marker）
plt.scatter(params, accuracy, c=colors, marker="o", s=200, edgecolors='black', alpha=0.85)

# 在数据点旁边添加模型名称，自动调整文本位置
for i, model in enumerate(models):
    ha = "right" if params[i] > 5 else "left"  # 避免超出边界
    offset_x = -15 if ha == "right" else 10  # 左侧文字偏右，右侧文字偏左
    offset_y = 5  # 避免重叠
    plt.annotate(model, (params[i], accuracy[i]), fontsize=10, fontweight="bold",
                 xytext=(offset_x, offset_y), textcoords="offset points", ha=ha, va="center", fontname="Arial")

# 对数刻度（log scale）避免数据挤在一起
plt.xscale("log")
plt.xlabel("Tunable Parameters (M, log scale)", fontsize=14, fontname="Arial")
plt.ylabel("N-Caltech 101 Top-1 Accuracy (%)", fontsize=14, fontname="Arial")
plt.title("Model Performance Comparison", fontsize=16, fontweight="bold", fontname="Arial")

# 美化网格和边界
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlim(min(params) / 2, max(params) * 2)
plt.ylim(min(accuracy) - 5, max(accuracy) + 5)

# 右下角添加 "Min" 和 "Full" 的解释
plt.text(0.07, min(accuracy) - 8,
         "Min: Backbone frozen\nFull: Fine-tuning entire model",
         fontsize=10, fontname="Arial", color="black",
         ha="left", va="top", bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.3"))

# 右下角添加箭头（指向左上角）
plt.annotate("Better Models", xy=(0.15, 50), xytext=(0.5, 40),
             arrowprops=dict(arrowstyle="->", color="brown", lw=2),
             fontsize=12, color="brown", fontweight="bold", fontname="Arial")

# 保存高清图片
plt.tight_layout()
plt.savefig("scatter_plot.png", dpi=300, bbox_inches="tight")

# 显示图像
plt.show()
