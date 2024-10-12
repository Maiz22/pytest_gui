import tkinter as tk
import tkinter.filedialog as fd
import customtkinter as ctk
from widgets.select_path_widget import SelectPathWidget

ctk.set_appearance_mode("dark")


class View(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("PyTestGUI")
        self.resizable(width=False, height=False)

        self.testcase_path_widget = SelectPathWidget(
            self,
            path_type="TestCases Path",
            has_checkbox=False,
            btn_state="disabled",
        )
        self.testcase_path_widget.pack(padx=10, pady=(5, 0), fill="both")

        # command line arg widgets
        self.command_line_args_frame = ctk.CTkFrame(self, border_width=1)
        self.command_line_args_frame.pack(padx=10, pady=(5, 0), fill="both")
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

        self.html_report_widget = SelectPathWidget(
            self, path_type="HTML-Report", has_checkbox=True
        )
        self.html_report_widget.pack(padx=10, pady=(5, 0), fill="both")
        self.json_report_widget = SelectPathWidget(
            self, path_type="JSON-Report", has_checkbox=True
        )
        self.json_report_widget.pack(padx=10, pady=(5, 0), fill="both")

        # text window frame
        self.output_frame = ctk.CTkFrame(self, border_width=1)
        self.output_frame.pack(padx=10, pady=(5, 0))
        # custom_font = ctk.CTkFont(family="Helvetica", size=16)
        self.text_box = ctk.CTkTextbox(
            self.output_frame, height=400, width=800, border_width=1
        )
        self.text_box.pack()

        # define textbox tags
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
        """
        Binds buttons on click event to a callback function.
        """
        self.json_report_widget.change_path_btn.bind(
            "<Button-1>", lambda event, fd=fd: callback(event, fd)
        )

    def select_html_report_path_btn_on_click(self, callback) -> None:
        """
        Binds buttons on click event to a callback function.
        """
        self.html_report_widget.change_path_btn.bind(
            "<Button-1>", lambda event, fd=fd: callback(event, fd)
        )

    def select_json_report_path_btn_on_click(self, callback) -> None:
        """
        Bind buttons on click event to a callback function.
        """
        self.json_report_widget.change_path_btn.bind(
            "<Button-1>", lambda event, fd=fd: callback(event, fd)
        )

    def start_test_btn_on_click(self, callback) -> None:
        """
        Bind buttons on click event to a callback function.
        """
        self.start_test_btn.bind("<Button-1>", callback)

    def append_text_box_content(self, text: str, tag_name: str = "default") -> None:
        """
        Append text to the Tkinter Text box and scroll to the end.
        """
        self.text_box.insert(tk.END, text + "\n\n", tag_name)
        self.text_box.see(tk.END)
        self.text_box.tag_add(tagName="default", index1=tk.END)
