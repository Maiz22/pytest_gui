from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tkinter import Text

import tkinter as tk
from colorama import init, Fore, Back, Style
import re

# Initialize colorama
init(autoreset=True)

# Regular expression to match ANSI escape sequences
ansi_escape = re.compile(r"\x1b\[([0-9;]*m)")

# Dictionary mapping ANSI color codes to Tkinter colors
ansi_to_tk = {
    "30": "black",
    "31": "red",
    "32": "green",
    "33": "yellow",
    "34": "blue",
    "35": "magenta",
    "36": "cyan",
    "37": "white",
    "90": "grey",
    "91": "light red",
    "92": "light green",
    "93": "light yellow",
    "94": "light blue",
    "95": "light magenta",
    "96": "light cyan",
    "97": "white",
}


class RedirectLogger:
    def __init__(self, text_widget: Text):
        self.text_widget = text_widget

    def write(self, message):
        self.process_message(message)

    def process_message(self, message):
        pos = 0
        for match in ansi_escape.finditer(message):
            start, end = match.span()
            if pos > 0:
                self.text_widget.insert(tk.END, message[pos:start], code)
            code = match.group(1)[0:-1]
            # print(code)

            # Insert plain text before the escape sequence
            # if start > pos:
            #    self.text_widget.insert(tk.END, message[pos:start])

            # Apply the corresponding color code if it exists
            if code in ansi_to_tk:
                # print(f"Found Code: {code} = {ansi_to_tk[code]}")
                # print(self.text_widget.tag_names())
                self.text_widget.tag_configure(
                    tagName=code, foreground=ansi_to_tk[code]
                )
                # self.text_widget.insert(tk.END, "", code)

            pos = end

        # Insert any remaining text after the last escape sequence
        if pos < len(message):
            self.text_widget.insert(tk.END, message[pos:])

        # Scroll to the end of the Text widget
        self.text_widget.see(tk.END)

    def flush(self):
        pass  # This method is needed for file-like objects

    def isatty(self):
        return True  # For compatibility with systems that expect isatty
