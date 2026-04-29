import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import gc

# 字体配置
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def run_absorption_curve(substance: str, wavelengths_str: str, absorbances_str: str) -> str:
    """
    执行吸收曲线绘制
    参数:
        substance: 物质名称
        wavelengths_str: 空格分隔的波长字符串
        absorbances_str: 空格分隔的吸光度字符串
    返回:
        状态信息字符串
    """
    try:
        # 解析数据
        wavelength_list = list(map(float, wavelengths_str.split()))
        absorbance_list = list(map(float, absorbances_str.split()))
        wavelengths = np.array(wavelength_list)
        absorbances = np.array(absorbance_list)

        # 检查数据长度
        if len(wavelengths) != len(absorbances):
            return "错误：波长数据和吸光度数据数量不匹配喵！"

        # 创建图形
        plt.figure(figsize=(8, 6))

        # 绘制数据点和连线
        plt.plot(wavelengths, absorbances, 'bo-', linewidth=1.5, markersize=6, label='数据')

        # 标记最大吸收波长
        max_index = np.argmax(absorbances)
        lambda_max = wavelengths[max_index]
        a_max = absorbances[max_index]
        plt.plot(lambda_max, a_max, 'ro', markersize=10, markeredgewidth=2,
                 label=f'$λ_{{\\max}}$ = {lambda_max} nm')

        # 给每个数据点标注坐标值
        for i in range(len(wavelengths)):
            if i == max_index:
                plt.annotate(f'({wavelengths[i]}, {absorbances[i]})',
                             (wavelengths[i], absorbances[i]),
                             textcoords="offset points",
                             xytext=(5, 5),
                             ha='left', fontsize=8)

        # 设置坐标轴
        plt.xlabel('波长λ(nm)', fontsize=12)
        plt.ylabel('吸光度A', fontsize=12)

        # 设置坐标范围
        plt.xlim(min(wavelengths) - 20, max(wavelengths) + 20)
        plt.ylim(0, max(absorbances) + 0.05)

        # 网格和图例
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(loc='best')

        # 美化布局
        plt.tight_layout()

        # 标题在下面
        plt.figtext(0.5, 0.01, f'图1 - {substance} 的吸收曲线', ha='center', fontsize=10)

        # 保存图片
        plt.savefig(f'{substance}_absorption_curve.png', dpi=150, bbox_inches='tight')

        # 显示图片
        plt.show()

        gc.collect()
        return f"图片已保存为 {substance}_absorption_curve.png，在与当前程序文件相同的目录"

    except Exception as e:
        return f"错误：{str(e)}"