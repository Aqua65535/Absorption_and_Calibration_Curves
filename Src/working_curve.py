import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import gc

# 字体配置
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def run_working_curve(substance: str, concentrations_str: str, absorbances_str: str, Ax: float) -> str:
    """
    执行工作曲线绘制和未知样品浓度计算
    参数:
        substance: 物质名称
        concentrations_str: 空格分隔的浓度字符串（第一项应为0）
        absorbances_str: 空格分隔的吸光度字符串（第一项应为0）
        Ax: 未知样品的吸光度
    返回:
        状态信息字符串（包含拟合结果）
    """
    try:
        # 解析数据
        concentration_list = list(map(float, concentrations_str.split()))
        absorbance_list = list(map(float, absorbances_str.split()))
        concentrations = np.array(concentration_list)
        absorbances = np.array(absorbance_list)

        # 检查数据长度
        if len(concentrations) != len(absorbances):
            return "错误：浓度数据和吸光度数据数量不匹配喵！"

        # 检查第一项是否为0（仅提醒，不强制）
        if concentrations[0] != 0:
            print("提示：浓度第一项不是0，建议将空白样浓度设为0喵！")
        if absorbances[0] != 0:
            print("提示：吸光度第一项不是0，建议将空白样吸光度设为0喵！")

        # 过原点拟合：只使用非零浓度点
        non_zero_indices = concentrations > 0
        concentrations_non_zero = concentrations[non_zero_indices]
        absorbance_non_zero = absorbances[non_zero_indices]

        if len(concentrations_non_zero) == 0:
            return "错误：没有有效的非零浓度数据点！"

        # 计算斜率
        slope = np.sum(concentrations_non_zero * absorbance_non_zero) / np.sum(concentrations_non_zero ** 2)

        # 生成拟合直线
        fit_line = slope * concentrations

        # 计算 R²
        correlation_matrix = np.corrcoef(absorbances, fit_line)
        r_squared = correlation_matrix[0, 1] ** 2

        # 计算未知样品浓度
        cx = Ax / slope

        # 创建图形
        plt.figure(figsize=(8, 6))

        # 绘制数据点和拟合直线
        plt.plot(concentrations, absorbances, 'ro', markersize=8, label='标准样品数据')
        plt.plot(concentrations, fit_line, 'b-', linewidth=2,
                 label=fr'拟合曲线: $A = {slope:.4f} \cdot c$' + '\n' + fr'($R^2 = {r_squared:.4f}$)')

        # 绘制未知样品点
        plt.axhline(y=Ax, color='purple', linestyle='--', alpha=0.7)
        plt.axvline(x=cx, color='purple', linestyle='--', alpha=0.7)
        plt.plot(cx, Ax, 's', color='purple', markersize=10,
                 label=f'未知样: A={Ax:.3f}\nc={cx:.4f}')

        # 标注数据点
        for i in range(len(concentrations)):
            plt.annotate(f'({concentrations[i]:.3f}, {absorbances[i]:.3f})',
                         (concentrations[i], absorbances[i]),
                         textcoords="offset points",
                         xytext=(5, 5),
                         ha='left', fontsize=8)

        # 设置坐标轴
        plt.xlabel(f'{substance} 的浓度(mg/mL)', fontsize=12)
        plt.ylabel(r'吸光度 $A$', fontsize=12)

        # 坐标范围
        plt.xlim(-0.001 * max(concentrations), max(concentrations) * 1.1)
        plt.ylim(-0.02, max(absorbances) * 1.1)

        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.figtext(0.5, 0.01, f'图2 - {substance} 的工作曲线', ha='center', fontsize=10)

        # 保存图片
        plt.savefig(f'{substance}_working_curve.png', dpi=150, bbox_inches='tight')

        # 构建结果字符串
        result = (f"拟合成功！\n"
                  f"拟合方程: A = {slope:.4f} * c\n"
                  f"线性相关系数 R² = {r_squared:.6f}\n"
                  f"未知样品浓度: {cx:.4f} mg/mL\n"
                  f"图片已保存为 {substance}_working_curve.png，在与当前程序文件相同的目录")

        plt.show()
        gc.collect()
        return result

    except Exception as e:
        return f"错误：{str(e)}"