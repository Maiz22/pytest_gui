import tkinter as tk
import tkinter.filedialog as fd


class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PyTestGUI")
        self.resizable(width=False, height=False)

        # setupt frame
        self.setup_frame = tk.Frame(self, borderwidth=2, relief="groove")
        self.setup_frame.pack(padx=10, pady=(5, 0), fill="both")

        self.path_label = tk.Label(self.setup_frame, text="Testcase Directory:")
        self.path_label.pack(side="left", padx=10, pady=5)
        self.cur_path = tk.StringVar()
        self.cur_path_label = tk.Label(self.setup_frame, textvariable=self.cur_path)
        self.cur_path_label.pack(side="left", padx=10, pady=5)
        self.select_path_btn = tk.Button(self.setup_frame, text="select")
        self.select_path_btn.pack(side="left", padx=10, pady=5)

        # text window
        self.output_frame = tk.Frame(self, borderwidth=2, relief="groove")
        self.output_frame.pack(padx=10, pady=(5, 0))
        self.text_box = tk.Text(
            self.output_frame,
            height=20,
            width=120,
            font=("Arial", 12),
            bg="black",
            fg="white",
        )
        self.text_box.pack(padx=5, pady=5)
        self.text_box.tag_configure("default", foreground="white")
        self.text_box.tag_configure("success", foreground="green")
        self.text_box.tag_configure("warning", foreground="yellow")
        self.text_box.tag_configure("failure", foreground="red")

        # control frame
        self.control_frame = tk.Frame(self, borderwidth=2, relief="groove")
        self.control_frame.pack(padx=10, pady=(5, 10), fill="both")

        self.start_test_btn = tk.Button(self.control_frame, text="Start")
        self.start_test_btn.pack(padx=5, pady=5, anchor="center")

    def select_path_btn_on_click(self, callback) -> None:
        self.select_path_btn.bind(
            "<Button-1>", lambda event, fd=fd: callback(event, fd)
        )

    def start_test_btn_on_click(self, callback) -> None:
        self.start_test_btn.bind("<Button-1>", callback)

    def append_text_box_content(self, text: str, tag_name: str = "success") -> None:
        """Append text to the Tkinter Text box and scroll to the end"""
        self.text_box.insert(tk.END, text + "\n\n", tag_name)
        self.text_box.see(tk.END)
        self.text_box.tag_add(tagName="default", index1=tk.END)
