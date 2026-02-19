import matplotlib.pyplot as plt
import numpy as np
import gc
from time import sleep


# 字体配置
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

"""
# 吸收曲线需要的数据（这个是老数据，让我注释掉了，不用管）
wavelengths = np.array([520, 540, 560, 580, 600, 610, 615, 620, 625, 630, 640])  # λ/nm
absorbance = np.array([0.055, 0.069, 0.084, 0.057, 0.136, 0.130, 0.149, 0.195, 0.122, 0.099, 0.095])  # A
wavelengths = np.array([520, 540, 560, 580, 600, 610, 615, 620, 625, 630, 640])  # λ/nm
absorbance = np.array([0.063, 0.080, 0.094, 0.107, 0.108, 0.108, 0.109, 0.110, 0.108, 0.107, 0.104])  # A
"""

def process_data():
    while True:
        try:
            # 按逗号分隔输入
            wavelength_list = list(map(float, input("输入波长数据，空格分隔：").split()))
            absorbance_list = list(map(float, input("输入吸光度数据，空格分隔：").split()))
            wavelengths = np.array(wavelength_list)
            absorbance = np.array(absorbance_list)
            break

        except ValueError:
            print("输入格式错误，请重新输入~~")
            continue

        except Exception as e:
            print(f"发生错误：{e}！你测出了bug！请汇报给lfw同学！")
            continue

    # 创建图形
    plt.figure(figsize=(8, 6))  # 设置图的大小，使其饱满

    # 绘制数据点和连线
    # 'bo-' 表示蓝色(b)圆圈(o)实线(-)
    plt.plot(wavelengths, absorbance, 'bo-', linewidth=1.5, markersize=6, label='数据')

    # 标记最大吸收波长
    max_index = np.argmax(absorbance)
    lambda_max = wavelengths[max_index]
    a_max = absorbance[max_index]
    plt.plot(lambda_max, a_max, 'ro', markersize=10, markeredgewidth=2,
             label=f'$λ_{{\\max}}$ = {lambda_max} nm')

    # 给每个数据点标注坐标值
    for i in range(len(wavelengths)):
        if i == max_index:
            plt.annotate(f'({wavelengths[i]}, {absorbance[i]})',
                         (wavelengths[i], absorbance[i]),
                         textcoords="offset points",
                         xytext=(5, 5),  # 标注文字距离点的偏移量
                         ha='left', fontsize=8)

    # 设置坐标轴
    plt.xlabel('波长λ(nm)', fontsize=8)
    plt.ylabel('吸光度A', fontsize=8)

    # 设置刻度 - 遵循1,2,5原则
    plt.xticks(np.arange(520, 641, 20))  # 从520到640，步长为20
    plt.yticks(np.arange(0, 0.30, 0.01))  # 根据数据调整

    # 设置坐标范围 - 让数据点分散占满
    plt.xlim(510, 650)
    plt.ylim(0, 0.20)

    # 网格和图例
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 美化布局
    plt.tight_layout()

    # 标题在下面
    plt.figtext(0.5, 0.01, r'图1 - $\mathrm{[Cu(NH_3)_4]^{2+}}$ 的吸收曲线', ha='center', fontsize=10)

    # 保存图片
    plt.savefig('absorption_curve.png', dpi=150, bbox_inches='tight')

    # 显示图片
    plt.show()

    gc.collect()

def main():
    print("你好，我是lfw！")
    sleep(0.8)
    print("欢迎使用lfw同学用python开发的化学实验数据处理工具之————吸收曲线图像绘制~")
    sleep(1.5)
    print("因为这是临时做的程序，所以不太健壮，输入离谱内容或不匹配的数据个数会崩。")
    sleep(1.5)
    print("说明：输入完成所有数据后，程序会弹出图像窗口。你可以调节该窗口的大小。\n我给这个程序加了自动保存图表的功能，但是可能有字体显示的问题。所以建议直接给窗口截图。")
    sleep(4)
    print("将窗口关闭后，程序会继续运行。")
    sleep(1)
    print("不说别的了，代码能跑就行！！")
    sleep(2)
    while True:
        print("=======================================================================")
        process_data()
        print("如果图像上什么都没有，可能是输入的数据不合理。")
        print("图片已保存。文件名：absorption_curve.png")
        input("输入任意内容，即可重新运行程序。")

if __name__ == "__main__":
    main()