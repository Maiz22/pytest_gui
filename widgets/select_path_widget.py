from customtkinter import CTkFrame, CTkCheckBox, CTkLabel, CTkButton
from tkinter import BooleanVar, StringVar


class SelectPathWidget(CTkFrame):
    """
    Widget created for selecting paths.
    """

    def __init__(
        self, master, path_type: str, has_checkbox: bool, btn_state: str = "normal"
    ) -> None:
        super().__init__(master, border_width=1)
        self.report_selected = BooleanVar()
        self.path = StringVar()
        self.create_ui(path_type, has_checkbox, btn_state)

    def create_ui(self, path_type: str, has_checkbox: bool, btn_state: bool) -> None:
        """
        Creates all of the widgets ui elements.
        """
        if has_checkbox:
            self.checkbox = CTkCheckBox(
                self,
                text=f"{path_type}",
                width=180,
                variable=self.report_selected,
                onvalue=True,
                offvalue=False,
            )
            self.checkbox.pack(side="left", padx=10, pady=5)
        else:
            CTkLabel(self, text=path_type, width=180).pack(side="left", padx=10, pady=5)
        self.label = CTkLabel(
            self,
            textvariable=self.path,
            width=420,
            wraplength=420,
        )
        self.change_path_btn = CTkButton(self, text="change", state=btn_state)
        self.label.pack(side="left", padx=10, pady=5)
        self.change_path_btn.pack(side="left", padx=10, pady=5)
