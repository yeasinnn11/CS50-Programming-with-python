import os
from tkinter import *
from tkinter import filedialog, colorchooser, font, Spinbox
from tkinter.messagebox import *

class TextEditor:
    def __init__(self, window):
        self.window = window
        self.window.title("Text Editor Program")
        self.file = None

        self.window_width = 500
        self.window_height = 500
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.x = int((self.screen_width / 2) - (self.window_width / 2))
        self.y = int((self.screen_height / 2) - (self.window_height / 2))

        self.window.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x, self.y))

        self.font_name = StringVar(self.window)
        self.font_name.set("Arial")

        self.font_size = StringVar(self.window)
        self.font_size.set("12")

        self.text_area = Text(self.window, font=(self.font_name.get(), self.font_size.get()))

        self.scroll_bar = Scrollbar(self.text_area)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.text_area.grid(sticky=N + E + S + W)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)

        self.frame = Frame(self.window)
        self.frame.grid()

        self.color_button = Button(self.frame,text="Color", command=self.change_color)
        self.color_button.grid(row=0, column=0)

        self.font_box = OptionMenu(self.frame, self.font_name, *font.families(), command=self.change_font)
        self.font_box.grid(row=0, column=1)

        self.size_box = Spinbox(self.frame, from_=1, to=100, textvariable=self.font_size, command=self.change_font)
        self.size_box.grid(row=0, column=2)

        self.menu_bar = Menu(self.window)
        self.window.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.Exit)

        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)

    def change_color(self):
        color = colorchooser.askcolor(title="Pick a color")
        self.text_area.config(fg=color[1])

    def change_font(self, *args):
        self.text_area.config(font=(self.font_name.get(), self.font_size.get()))

    def new_file(self):
        self.window.title("Untitled")
        self.text_area.delete(1.0, END)

    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Text Documents", "*.txt")])
        try:
            self.window.title(os.path.basename(file))
            self.text_area.delete(1.0, END)

            with open(file, "r") as f:
                self.text_area.insert(1.0, f.read())

        except Exception as e:
            print("Couldn't read file:", e)

    def save_file(self):
        file = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

        if file:
            try:
                self.window.title(os.path.basename(file))
                with open(file, "w") as f:
                    f.write(self.text_area.get(1.0, END))

            except Exception as e:
                print("Couldn't save this file:", e)

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def about(self):
        showinfo("About this program", "This program written by youuuu")

    def Exit(self):
        self.window.destroy()

if __name__ == "__main__":
    window = Tk()
    editor = TextEditor(window)
    window.mainloop()
