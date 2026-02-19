"""import matplotlib.pyplot as plt
import numpy as np
import gc

from vtkmodules.util.colors import purple

# 字体配置
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


# 工作曲线需要的数据（这个是老数据，让我注释掉了，不用管）
concentrations = np.array([0.000, 0.008, 0.016, 0.024, 0.032, 0.040])  # c / mol·L⁻¹
absorbance_std = np.array([0.000, 0.031, 0.061, 0.195, 0.391, 0.408])  # A


# 工作曲线需要的数据
concentrations = np.array([0.000, 0.008, 0.016, 0.024, 0.032, 0.040])  # c / mol·L⁻¹
absorbance_std = np.array([0.000, 0.040, 0.089, 0.110, 0.172, 0.201])  # A
Ax = 0.064

# 使用 numpy 进行过原点的一元线性拟合
# 只使用非零浓度点进行拟合（排除原点）
non_zero_indices = concentrations > 0
concentrations_non_zero = concentrations[non_zero_indices]
absorbance_non_zero = absorbance_std[non_zero_indices]

# 过原点拟合：A = k*c，计算斜率k
slope = np.sum(concentrations_non_zero * absorbance_non_zero) / np.sum(concentrations_non_zero**2)

# 生成拟合直线上的点（包括原点）
fit_line = slope * concentrations

# 计算 R²（使用所有数据点）
correlation_matrix = np.corrcoef(absorbance_std, fit_line)
r_squared = correlation_matrix[0,1] ** 2

# 计算未知样品浓度
cx = Ax / slope

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制数据点和拟合直线
plt.plot(concentrations, absorbance_std, 'ro', markersize=8, label='数据')
plt.plot(concentrations, fit_line, 'b-', linewidth=2,
         label = fr'拟合曲线: $A = {slope:.3f}c$' + '\n' + fr'($R = {r_squared:.4f}$)')

# 绘制未知样品点
plt.axhline(y=Ax, color=purple, linestyle='--', alpha=0.7)
plt.axvline(x=cx, color=purple, linestyle='--', alpha=0.7)
plt.plot(cx, Ax, 's', color=purple, markersize=10,
        label=f'未知样: A={Ax:.3f}\nc={cx:.4f} mol/L')

# 给每个标准数据点标注坐标值
for i in range(len(concentrations)):
    plt.annotate(f'({concentrations[i]:.3f}, {absorbance_std[i]:.3f})',
                (concentrations[i], absorbance_std[i]),
                textcoords="offset points",
                xytext=(5,5),  # 标注文字距离点的偏移量
                ha='left', fontsize=8)

# 设置坐标轴
plt.xlabel(r'$\mathrm{[Cu(NH_3)_4]^{2+}}$ 的浓度 (mol$\cdot$L$^{-1}$)', fontsize=8)
plt.ylabel(r'吸光度 $A$', fontsize=8)

# 刻度和范围
plt.xlim(-0.001, max(concentrations)*1.1)
plt.ylim(-0.02, max(absorbance_std)*1.1)

# 网格和图例
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 美化布局
plt.tight_layout()

#标题在下面
plt.figtext(0.5,0.01,r'图2 - $\mathrm{Cu^{2+}}$ 的工作曲线',ha='center', fontsize=10)

#保存图片
plt.savefig('working_curve.png', dpi=72, bbox_inches='tight')

# 打印拟合参数
print(f"拟合方程: A = {slope:.4f}c")
print(f"线性相关系数 R² = {r_squared:.6f}")

#显示图片
plt.show()

gc.collect()

"""


import matplotlib.pyplot as plt
import numpy as np
import gc
from time import sleep

# 字体配置
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def process_data():
    while True:
        try:
            # 按空格分隔输入
            concentration_list = list(map(float, input("输入浓度数据（第一项必须为0），空格分隔：").split()))
            absorbance_list = list(map(float, input("输入吸光度数据（第一项必须为0），空格分隔：").split()))
            Ax = float(input("输入未知样品的吸光度："))

            concentrations = np.array(concentration_list)
            absorbance_std = np.array(absorbance_list)
            break

        except ValueError:
            print("输入格式错误，请重新输入~~")
            continue

        except Exception as e:
            print(f"发生错误：{e}！你测出了bug！请汇报给lfw同学！")
            continue

    """拟合↓"""
    # 使用 numpy 进行过原点的一元线性拟合
    # 只使用非零浓度点进行拟合（排除原点）
    non_zero_indices = concentrations > 0
    concentrations_non_zero = concentrations[non_zero_indices]
    absorbance_non_zero = absorbance_std[non_zero_indices]

    # 过原点拟合：A = k*c，计算斜率k
    slope = np.sum(concentrations_non_zero * absorbance_non_zero) / np.sum(concentrations_non_zero ** 2)

    # 生成拟合直线上的点（包括原点）
    fit_line = slope * concentrations

    # 计算 R²（使用所有数据点）
    correlation_matrix = np.corrcoef(absorbance_std, fit_line)
    r_squared = correlation_matrix[0, 1] ** 2
    """拟合↑"""

    # 计算未知样品浓度
    cx = Ax / slope

    # 创建图形
    plt.figure(figsize=(8, 6))

    # 绘制数据点和拟合直线
    plt.plot(concentrations, absorbance_std, 'ro', markersize=8, label='数据')
    plt.plot(concentrations, fit_line, 'b-', linewidth=2,
             label=fr'拟合曲线: $A = {slope:.3f}c$' + '\n' + fr'($R = {r_squared:.4f}$)')

    # 绘制未知样品点
    plt.axhline(y=Ax, color='purple', linestyle='--', alpha=0.7)
    plt.axvline(x=cx, color='purple', linestyle='--', alpha=0.7)
    plt.plot(cx, Ax, 's', color='purple', markersize=10,
             label=f'未知样: A={Ax:.3f}\nc={cx:.4f} mol/L')

    # 给每个标准数据点标注坐标值
    for i in range(len(concentrations)):
        plt.annotate(f'({concentrations[i]:.3f}, {absorbance_std[i]:.3f})',
                     (concentrations[i], absorbance_std[i]),
                     textcoords="offset points",
                     xytext=(5, 5),  # 标注文字距离点的偏移量
                     ha='left', fontsize=8)

    # 设置坐标轴
    plt.xlabel(r'$\mathrm{[Cu(NH_3)_4]^{2+}}$ 的浓度 (mol$\cdot$L$^{-1}$)', fontsize=8)
    plt.ylabel(r'吸光度 $A$', fontsize=8)

    # 刻度和范围
    plt.xlim(-0.001, max(concentrations) * 1.1)
    plt.ylim(-0.02, max(absorbance_std) * 1.1)

    # 网格和图例
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 美化布局
    plt.tight_layout()

    # 标题在下面
    plt.figtext(0.5, 0.01, r'图2 - $\mathrm{Cu^{2+}}$ 的工作曲线', ha='center', fontsize=10)

    # 保存图片
    plt.savefig('working_curve.png', dpi=150, bbox_inches='tight')

    # 打印拟合参数
    print(f"拟合方程: A = {slope:.4f}c")
    print(f"线性相关系数 R² = {r_squared:.6f}")
    print(f"未知样品浓度: {cx:.4f} mol/L")

    # 显示图片
    for _ in range(3):
        plt.show()

    gc.collect()


def main():
    print("你好，我是lfw！")
    sleep(0.8)
    print("欢迎使用lfw同学用python开发的化学实验数据处理工具之————工作曲线图像绘制~")
    sleep(1.5)
    print("因为这是临时做的程序，所以不太健壮，输入离谱内容或不匹配的数据个数会崩。")
    sleep(1.5)
    print(
        "说明：输入完成所有数据后，程序会弹出图像窗口。你可以调节该窗口的大小。\n我给这个程序加了自动保存图表的功能，但是可能有字体显示的问题。所以建议直接给窗口截图。")
    sleep(4)
    print("将窗口关闭后，程序会继续运行。")
    sleep(1)
    print("不说别的了，代码能跑就行！！")
    sleep(2)
    while True:
        print("=======================================================================")
        process_data()
        print("如果图像上什么都没有，可能是输入的数据不合理。")
        print("图片已保存。文件名：working_curve.png")
        input("输入任意内容，即可重新运行程序。")


if __name__ == "__main__":
    main()
