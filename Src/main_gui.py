import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import webbrowser
import absorption_curve
import working_curve


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("吸收/工作（标准）曲线绘制程序")
        self.root.geometry("550x550")
        self.root.resizable(False, False)

        # 设置样式
        style = ttk.Style()
        style.theme_use('clam')

        # 主标题
        title_label = tk.Label(root, text="吸收/工作（标准）曲线绘制程序", font=("微软雅黑", 20, "bold"), fg="#2C3E50")
        title_label.pack(pady=20)

        # 副标题
        subtitle_label = tk.Label(root, text="请选择要进行的分析类型", font=("微软雅黑", 12), fg="#7F8C8D")
        subtitle_label.pack(pady=(0, 30))

        # 按钮框架
        button_frame = tk.Frame(root)
        button_frame.pack(expand=True)

        # 吸收曲线按钮
        self.absorption_btn = tk.Button(
            button_frame,
            text="吸收曲线分析",
            font=("微软雅黑", 14),
            bg="#3498DB",
            fg="white",
            width=20,
            height=2,
            command=self.open_absorption_window,
            relief="raised",
            bd=2
        )
        self.absorption_btn.pack(pady=15)

        # 工作曲线按钮
        self.working_btn = tk.Button(
            button_frame,
            text="工作（标准）曲线分析",
            font=("微软雅黑", 14),
            bg="#E67E22",
            fg="white",
            width=20,
            height=2,
            command=self.open_working_window,
            relief="raised",
            bd=2
        )
        self.working_btn.pack(pady=15)

        # 软件详情按钮（新增）
        self.detail_btn = tk.Button(
            button_frame,
            text="软件详情",
            font=("微软雅黑", 12),
            bg="#cccccc",
            fg="white",
            width=15,
            height=1,
            command=self.open_about_window,
            relief="raised",
            bd=2
        )
        self.detail_btn.pack(pady=(30, 10))

        # 设置按钮悬停效果
        self.setup_hover_effects()

    def setup_hover_effects(self):
        def on_enter(btn, color):
            btn['background'] = color

        def on_leave(btn, color):
            btn['background'] = color

        self.absorption_btn.bind("<Enter>", lambda e: on_enter(self.absorption_btn, "#2980B9"))
        self.absorption_btn.bind("<Leave>", lambda e: on_leave(self.absorption_btn, "#3498DB"))
        self.working_btn.bind("<Enter>", lambda e: on_enter(self.working_btn, "#D35400"))
        self.working_btn.bind("<Leave>", lambda e: on_leave(self.working_btn, "#E67E22"))
        self.detail_btn.bind("<Enter>", lambda e: on_enter(self.detail_btn, "#A9A9A9"))
        self.detail_btn.bind("<Leave>", lambda e: on_leave(self.detail_btn, "#cccccc"))

    def open_about_window(self):
        """打开软件详情窗口"""
        about_window = tk.Toplevel(self.root)
        about_window.title("软件详情")
        about_window.geometry("700x350")
        about_window.resizable(False, False)
        about_window.configure(bg="#f5f5f5")

        # 居中显示
        about_window.transient(self.root)
        about_window.grab_set()

        # 主框架
        main_frame = tk.Frame(about_window, bg="#f5f5f5", padx=25, pady=25)
        main_frame.pack(fill="both", expand=True)

        # 作者名称
        tk.Label(main_frame, text="作者：Aqua_65535", font=("微软雅黑", 18, "bold"), fg="#2C3E50", bg="#f5f5f5").pack()

        # 描述
        desc_text = "你好！我是Aqua_65535，一个喜欢化学与编程的应用化学专业女生。\n这个小软件是我用AI编程辅助做的，希望它能帮你解决问题！\n如果可以的话，希望你能在Github上为我点个Star，谢谢你！"
        tk.Label(main_frame, text=desc_text, font=("微软雅黑", 10), fg="#7F8C8D", bg="#f5f5f5").pack(pady=(5, 15))

        # 分隔线
        tk.Frame(main_frame, height=2, bg="#E0E0E0", relief="flat").pack(fill="x", pady=10)

        # 项目地址
        project_frame = tk.Frame(main_frame, bg="#f5f5f5")
        project_frame.pack(fill="x", pady=8)
        tk.Label(project_frame, text="项目地址：", font=("微软雅黑", 10, "bold"), fg="#2C3E50", bg="#f5f5f5").pack(side="left")
        project_link = tk.Label(project_frame, text="点击访问https://github.com/Aqua65535/Absorption_and_Calibration_Curves", font=("微软雅黑", 10), fg="#3498DB", bg="#f5f5f5", cursor="hand2")
        project_link.pack(side="left", padx=(5, 0))
        project_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Aqua65535/Absorption_and_Calibration_Curves"))

        # 个人网站
        website_frame = tk.Frame(main_frame, bg="#f5f5f5")
        website_frame.pack(fill="x", pady=8)
        tk.Label(website_frame, text="个人网站：", font=("微软雅黑", 10, "bold"), fg="#2C3E50", bg="#f5f5f5").pack(side="left")
        website_link = tk.Label(website_frame, text="点击访问https://aqua65535.netlify.app/", font=("微软雅黑", 10), fg="#3498DB", bg="#f5f5f5", cursor="hand2")
        website_link.pack(side="left", padx=(5, 0))
        website_link.bind("<Button-1>", lambda e: webbrowser.open("https://aqua65535.netlify.app/"))

        # 联系方式
        contact_frame = tk.Frame(main_frame, bg="#f5f5f5")
        contact_frame.pack(fill="x", pady=(15, 5))
        tk.Label(contact_frame, text="联系我：", font=("微软雅黑", 10, "bold"), fg="#2C3E50", bg="#f5f5f5").pack(side="left")
        tk.Label(contact_frame, text="lfwchemistry520@outlook.com", font=("微软雅黑", 9), fg="#7F8C8D", bg="#f5f5f5").pack(side="left", padx=(5, 0))

        # 版本信息
        tk.Label(main_frame, text="版本 v1.0.0", font=("微软雅黑", 8), fg="#BDC3C7", bg="#f5f5f5").pack(pady=(20, 0))


    def open_absorption_window(self):
        """打开吸收曲线输入窗口"""
        window = tk.Toplevel(self.root)
        window.title("吸收曲线分析 - 数据输入")
        window.geometry("650x550")
        window.resizable(False, False)

        # 主框架
        main_frame = tk.Frame(window, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # 物质名称
        tk.Label(main_frame, text="物质名称:", font=("微软雅黑", 11)).grid(row=0, column=0, sticky="w", pady=10)
        substance_entry = tk.Entry(main_frame, font=("微软雅黑", 11), width=40)
        substance_entry.grid(row=0, column=1, pady=10, padx=10)

        # 波长数据
        tk.Label(main_frame, text="波长λ(nm):", font=("微软雅黑", 11)).grid(row=1, column=0, sticky="nw", pady=10)
        wavelength_text = scrolledtext.ScrolledText(main_frame, height=5, width=40, font=("Consolas", 10))
        wavelength_text.grid(row=1, column=1, pady=10, padx=10)
        tk.Label(main_frame, text="(空格分隔，如: 400 420 440)", font=("微软雅黑", 9), fg="gray").grid(row=2, column=1,
                                                                                                    sticky="w")

        # 吸光度数据
        tk.Label(main_frame, text="吸光度A:", font=("微软雅黑", 11)).grid(row=3, column=0, sticky="nw", pady=10)
        absorbance_text = scrolledtext.ScrolledText(main_frame, height=5, width=40, font=("Consolas", 10))
        absorbance_text.grid(row=3, column=1, pady=10, padx=10)
        tk.Label(main_frame, text="(空格分隔，与波长数据一一对应)", font=("微软雅黑", 9), fg="gray").grid(row=4, column=1,
                                                                                                  sticky="w")

        # 结果输出区域
        tk.Label(main_frame, text="运行结果:", font=("微软雅黑", 11)).grid(row=5, column=0, sticky="nw", pady=10)
        result_text = scrolledtext.ScrolledText(main_frame, height=6, width=50, font=("Consolas", 10), state="normal")
        result_text.grid(row=5, column=1, pady=10, padx=10, columnspan=1)
        result_text.insert("1.0", "数据还未计算")
        result_text.config(state="disabled")

        # 按钮区域
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        def run_analysis():
            substance = substance_entry.get().strip()
            wavelengths = wavelength_text.get("1.0", tk.END).strip()
            absorbances = absorbance_text.get("1.0", tk.END).strip()

            if not substance:
                messagebox.showwarning("啊哦！", "请输入物质名称！")
                return
            if not wavelengths or not absorbances:
                messagebox.showwarning("啊哦！", "请输入波长和吸光度数据！")
                return

            # 清空并显示结果
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)
            result_text.insert("1.0", "正在计算中，请稍候...\n")
            result_text.config(state="disabled")
            window.update()

            # 执行分析
            result = absorption_curve.run_absorption_curve(substance, wavelengths, absorbances)

            # 显示结果
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)
            result_text.insert("1.0", result)
            result_text.config(state="disabled")

        def clear_input():
            substance_entry.delete(0, tk.END)
            wavelength_text.delete("1.0", tk.END)
            absorbance_text.delete("1.0", tk.END)
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)
            result_text.insert("1.0", "数据还未计算")
            result_text.config(state="disabled")

        tk.Button(button_frame, text="开始画图", font=("微软雅黑", 11), bg="#3498DB", fg="white",
                  command=run_analysis, padx=20, pady=5).pack(side="left", padx=10)
        tk.Button(button_frame, text="清空输入", font=("微软雅黑", 11), bg="#95A5A6", fg="white",
                  command=clear_input, padx=20, pady=5).pack(side="left", padx=10)

    def open_working_window(self):
        """打开工作曲线输入窗口"""
        window = tk.Toplevel(self.root)
        window.title("工作（标准）曲线分析 - 数据输入")
        window.geometry("700x650")
        window.resizable(False, False)

        # 主框架
        main_frame = tk.Frame(window, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        # 物质名称
        tk.Label(main_frame, text="物质名称:", font=("微软雅黑", 11)).grid(row=0, column=0, sticky="w", pady=10)
        substance_entry = tk.Entry(main_frame, font=("微软雅黑", 11), width=40)
        substance_entry.grid(row=0, column=1, pady=10, padx=10)

        # 浓度数据
        tk.Label(main_frame, text="已知样浓度(mg/mL):", font=("微软雅黑", 11)).grid(row=1, column=0, sticky="nw", pady=10)
        concentration_text = scrolledtext.ScrolledText(main_frame, height=5, width=40, font=("Consolas", 10))
        concentration_text.grid(row=1, column=1, pady=10, padx=10)
        tk.Label(main_frame, text="(空格分隔，第一项必须为0，如: 0 0.1 0.2)", font=("微软雅黑", 9), fg="gray").grid(row=2,
                                                                                                           column=1,
                                                                                                           sticky="w")

        # 吸光度数据
        tk.Label(main_frame, text="已知样吸光度A:", font=("微软雅黑", 11)).grid(row=3, column=0, sticky="nw", pady=10)
        absorbance_text = scrolledtext.ScrolledText(main_frame, height=5, width=40, font=("Consolas", 10))
        absorbance_text.grid(row=3, column=1, pady=10, padx=10)
        tk.Label(main_frame, text="(空格分隔，第一项必须为0，与浓度一一对应)", font=("微软雅黑", 9), fg="gray").grid(row=4, column=1,
                                                                                                      sticky="w")

        # 未知样品吸光度
        tk.Label(main_frame, text="未知样吸光度:", font=("微软雅黑", 11)).grid(row=5, column=0, sticky="w", pady=10)
        Ax_entry = tk.Entry(main_frame, font=("微软雅黑", 11), width=20)
        Ax_entry.grid(row=5, column=1, sticky="w", pady=10, padx=10)

        # 结果输出区域
        tk.Label(main_frame, text="运行结果:", font=("微软雅黑", 11)).grid(row=6, column=0, sticky="nw", pady=10)
        result_text = scrolledtext.ScrolledText(main_frame, height=8, width=50, font=("Consolas", 10), state="normal")
        result_text.grid(row=6, column=1, pady=10, padx=10, columnspan=1)
        result_text.insert("1.0", "数据还未计算")
        result_text.config(state="disabled")

        # 按钮区域
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        def run_analysis():
            substance = substance_entry.get().strip()
            concentrations = concentration_text.get("1.0", tk.END).strip()
            absorbances = absorbance_text.get("1.0", tk.END).strip()
            Ax_str = Ax_entry.get().strip()

            if not substance:
                messagebox.showwarning("啊哦！", "请输入物质名称！")
                return
            if not concentrations or not absorbances:
                messagebox.showwarning("啊哦！", "请输入浓度和吸光度数据！")
                return
            if not Ax_str:
                messagebox.showwarning("啊哦！", "请输入未知样品的吸光度！")
                return

            try:
                Ax = float(Ax_str)
            except ValueError:
                messagebox.showwarning("啊哦！", "未知样品吸光度必须是数字！")
                return

            # 清空并显示结果
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)
            result_text.insert("1.0", "正在计算中，请稍候...\n")
            result_text.config(state="disabled")
            window.update()

            # 执行分析
            result = working_curve.run_working_curve(substance, concentrations, absorbances, Ax)

            # 显示结果
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)
            result_text.insert("1.0", result)
            result_text.config(state="disabled")

        def clear_input():
            substance_entry.delete(0, tk.END)
            concentration_text.delete("1.0", tk.END)
            absorbance_text.delete("1.0", tk.END)
            Ax_entry.delete(0, tk.END)
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)
            result_text.insert("1.0", "数据还未计算")
            result_text.config(state="disabled")

        tk.Button(button_frame, text="开始画图", font=("微软雅黑", 11), bg="#E67E22", fg="white",
                  command=run_analysis, padx=20, pady=5).pack(side="left", padx=10)
        tk.Button(button_frame, text="清空输入", font=("微软雅黑", 11), bg="#95A5A6", fg="white",
                  command=clear_input, padx=20, pady=5).pack(side="left", padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()