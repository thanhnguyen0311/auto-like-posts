import tkinter as tk
import webbrowser
import time
import pyautogui


def disable_resize(event=None):
    return False

class App:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Facebook Robot")
        self.root.geometry("800x600")

        self.view1_frame = tk.Frame(root)
        self.view2_frame = tk.Frame(root)

        self.label = tk.Label(self.view1_frame, text="Like Post ", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.entry = tk.Text(self.view1_frame,width=50, height=5, wrap="word")
        self.entry.pack(pady=20)

        self.result_label = tk.Label(self.view1_frame, text="", font=("Helvetica", 10))
        self.result_label.pack_forget()

        self.button_switch_to_view2 = tk.Button(self.view1_frame, text="like", command=self.on_submit)
        self.button_switch_to_view2.pack()
    
        label_view2 = tk.Label(self.view2_frame, text="View 2 Content")
        label_view2.pack(pady=10)

        self.button_switch_to_view1 = tk.Button(self.view2_frame, text="Switch to View 1", command=self.show_view1)
        self.button_switch_to_view1.pack()

        self.show_view1()

    def show_view1(self):
        self.view2_frame.pack_forget()
        self.view1_frame.pack()

    def show_view2(self):
        self.view1_frame.pack_forget()
        self.view2_frame.pack()

    def on_submit(self):
        self.input_posts = self.entry.get("1.0", "end-1c")
        for line in self.input_posts.split('\n'):
            webbrowser.open(f"https://www.facebook.com/{line}")
            time.sleep(4)
            pyautogui.press('l')

        self.result_label.configure(text=f"You liked {self.input_posts}")
        self.result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
