import tkinter as tk
import tkinter.filedialog as fd
import customtkinter as ctk

ctk.set_appearance_mode("dark")


class View(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PyTestGUI")
        self.resizable(width=False, height=False)

        # top frames
        self.setup_frame = ctk.CTkFrame(self, border_width=1)
        self.setup_frame.pack(padx=10, pady=(5, 0), fill="both")
        self.command_line_args_frame = ctk.CTkFrame(self, border_width=1)
        self.command_line_args_frame.pack(padx=10, pady=(5, 0), fill="both")
        self.html_report_frame = ctk.CTkFrame(self, border_width=1)
        self.html_report_frame.pack(padx=10, pady=(5, 0), fill="both")
        self.json_report_frame = ctk.CTkFrame(self, border_width=1)
        self.json_report_frame.pack(padx=10, pady=(5, 0), fill="both")

        # testcase path widgets
        self.path_label = ctk.CTkLabel(
            self.setup_frame, text="Testcase Directory @", width=180
        )
        self.path_label.pack(side="left", padx=10, pady=5)
        self.cur_path = tk.StringVar()
        self.cur_path_label = ctk.CTkLabel(
            self.setup_frame, textvariable=self.cur_path, width=420, wraplength=420
        )
        self.cur_path_label.pack(side="left", padx=10, pady=5)
        # self.select_path_btn = ctk.CTkButton(self.setup_frame, text="change")
        # self.select_path_btn.pack(side="left", padx=10, pady=5)

        # command line arg widgets
        self.command_line_label = ctk.CTkLabel(
            self.command_line_args_frame, text="Command Line Arguments", width=180
        )
        self.command_line_label.pack(side="left", padx=10, pady=5)
        self.command_line_args = ctk.CTkEntry(
            self.command_line_args_frame,
            placeholder_text="Enter pytest arguments, e.g.: -v, -r",
            width=580,
        )
        self.command_line_args.pack(side="left", padx=10, pady=5)

        # html report widgets
        self.html_report_selected = tk.BooleanVar()
        self.html_report_option = ctk.CTkCheckBox(
            self.html_report_frame,
            text="Create HTML Report @",
            width=180,
            variable=self.html_report_selected,
            onvalue=True,
            offvalue=False,
        )
        self.html_report_option.pack(side="left", padx=10, pady=5)
        self.html_report_path = tk.StringVar()
        self.html_report_path_label = ctk.CTkLabel(
            self.html_report_frame,
            textvariable=self.html_report_path,
            width=420,
            wraplength=420,
        )
        self.html_report_path_label.pack(side="left", padx=10, pady=5)
        self.html_report_path_btn = ctk.CTkButton(self.html_report_frame, text="change")
        self.html_report_path_btn.pack(side="left", padx=10, pady=5)

        # json report widgets
        self.json_report_selected = tk.BooleanVar()
        self.json_report_option = ctk.CTkCheckBox(
            self.json_report_frame,
            text="Create JSON Report @",
            width=180,
            variable=self.json_report_selected,
            onvalue=True,
            offvalue=False,
        )
        self.json_report_option.pack(side="left", padx=10, pady=5)
        self.json_report_path = tk.StringVar()
        self.json_report_path_label = ctk.CTkLabel(
            self.json_report_frame,
            textvariable=self.json_report_path,
            width=420,
            wraplength=420,
        )
        self.json_report_path_label.pack(side="left", padx=10, pady=5)
        self.json_report_path_btn = ctk.CTkButton(self.json_report_frame, text="change")
        self.json_report_path_btn.pack(side="left", padx=10, pady=5)

        # text window frame
        self.output_frame = ctk.CTkFrame(self, border_width=1)
        self.output_frame.pack(padx=10, pady=(5, 0))
        # custom_font = ctk.CTkFont(family="Helvetica", size=16)
        self.text_box = ctk.CTkTextbox(
            self.output_frame, height=400, width=800, border_width=1
        )
        self.text_box.pack()
        self.text_box.tag_config("default", foreground="white")
        self.text_box.tag_config("success", foreground="green")
        self.text_box.tag_config("warning", foreground="yellow")
        self.text_box.tag_config("failure", foreground="red")

        # control frame
        self.control_frame = ctk.CTkFrame(self, border_width=1)
        self.control_frame.pack(padx=10, pady=(5, 10), fill="both")

        self.start_test_btn = ctk.CTkButton(self.control_frame, text="Start")
        self.start_test_btn.pack(padx=5, pady=5, anchor="center")

    def select_path_btn_on_click(self, callback) -> None:
        self.select_path_btn.bind(
            "<Button-1>", lambda event, fd=fd: callback(event, fd)
        )

    def select_html_report_path_btn_on_click(self, callback) -> None:
        self.html_report_path_btn.bind(
            "<Button-1>", lambda event, fd=fd: callback(event, fd)
        )

    def select_json_report_path_btn_on_click(self, callback) -> None:
        self.json_report_path_btn.bind(
            "<Button-1>", lambda event, fd=fd: callback(event, fd)
        )

    def start_test_btn_on_click(self, callback) -> None:
        self.start_test_btn.bind("<Button-1>", callback)

    def append_text_box_content(self, text: str, tag_name: str = "default") -> None:
        """Append text to the Tkinter Text box and scroll to the end"""
        self.text_box.insert(tk.END, text + "\n\n", tag_name)
        self.text_box.see(tk.END)
        self.text_box.tag_add(tagName="default", index1=tk.END)
