import matplotlib.pyplot as plt
import numpy as np
import gc

# 字体配置
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 定义两组数据
data_sets = {
    "旧数据": {
        "concentrations": np.array([0.000, 0.008, 0.016, 0.024, 0.032, 0.040]),
        "absorbance_std": np.array([0.000, 0.031, 0.061, 0.195, 0.391, 0.408]),
        "Ax": 0.421,
        "color": "orange"
    },
    "新数据": {
        "concentrations": np.array([0.000, 0.008, 0.016, 0.024, 0.032, 0.040]),
        "absorbance_std": np.array([0.000, 0.040, 0.089, 0.110, 0.172, 0.201]),
        "Ax": 0.064,
        "color": "purple"
    }
}

# 创建两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# 循环处理两组数据
for idx, (data_name, data) in enumerate(data_sets.items()):
    if idx == 0:
        ax = ax1
    else:
        ax = ax2

    concentrations = data["concentrations"]
    absorbance_std = data["absorbance_std"]
    Ax = data["Ax"]
    color = data["color"]

    """拟合"""
    # 使用非零浓度点进行过原点拟合
    non_zero_indices = concentrations > 0
    concentrations_non_zero = concentrations[non_zero_indices]
    absorbance_non_zero = absorbance_std[non_zero_indices]

    # 过原点拟合：A = k*c
    slope = np.sum(concentrations_non_zero * absorbance_non_zero) / np.sum(concentrations_non_zero ** 2)
    fit_line = slope * concentrations

    # 计算 R²
    correlation_matrix = np.corrcoef(absorbance_std, fit_line)
    r_squared = correlation_matrix[0, 1] ** 2
    """拟合"""

    # 计算未知样品浓度
    cx = Ax / slope

    # 绘制数据点和拟合直线
    ax.plot(concentrations, absorbance_std, 'ro', markersize=8, label='标准数据点')
    ax.plot(concentrations, fit_line, 'b-', linewidth=2,
            label=fr'拟合: $A = {slope:.3f}c$' + '\n' + fr'($R^2 = {r_squared:.4f}$)')

    # 绘制未知样品点
    ax.axhline(y=Ax, color=color, linestyle='--', alpha=0.7)
    ax.axvline(x=cx, color=color, linestyle='--', alpha=0.7)
    ax.plot(cx, Ax, 's', color=color, markersize=10,
            label=f'未知样: A={Ax:.3f}\nc={cx:.4f} mol/L')

    # 给每个标准数据点标注坐标值
    for i in range(len(concentrations)):
        ax.annotate(f'({concentrations[i]:.3f}, {absorbance_std[i]:.3f})',
                    (concentrations[i], absorbance_std[i]),
                    textcoords="offset points",
                    xytext=(5, 5),
                    ha='left', fontsize=8)

    # 设置坐标轴
    ax.set_xlabel(r'$\mathrm{[Cu(NH_3)_4]^{2+}}$ 的浓度 (mol$\cdot$L$^{-1}$)', fontsize=12)
    ax.set_ylabel(r'吸光度 $A$', fontsize=12)

    # 刻度和范围
    ax.set_xlim(-0.001, max(concentrations) * 1.1)
    ax.set_ylim(-0.02, max(max(absorbance_std), Ax) * 1.1)

    # 网格和图例
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend(loc='upper left')

    # 设置子图标题
    ax.set_title(f'{data_name}工作曲线', fontsize=14, fontweight='bold')

    # 打印结果
    print(f"{data_name}结果:")
    print(f"  拟合方程: A = {slope:.4f}c")
    print(f"  线性相关系数 R² = {r_squared:.6f}")
    print(f"  未知样浓度: {cx:.6f} mol/L")
    print()

# 整体标题
plt.suptitle(r'图2 - $\mathrm{Cu^{2+}}$ 的工作曲线对比', fontsize=16, y=0.04)

# 美化布局
plt.tight_layout()

# 保存图片
plt.savefig('working_curve_comparison.png', dpi=72, bbox_inches='tight')

# 显示图片
plt.show()

gc.collect()

#本人已经累死了。这旧仪器咋回事啊啊，数据太离谱了。。早点换掉吧！！