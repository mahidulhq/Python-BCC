import tkinter as tk
import time
import math


class AnimatedWallpaper:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Animated Clock - Developer Edition")

        self.width = 800
        self.height = 600
        self.canvas = tk.Canvas(
            root, width=self.width, height=self.height, bg='#0d0d0d', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.angle = 0
        self.update_clock()

    def draw_rounded_ring(self):
        self.canvas.delete("ring")
        cx, cy = self.width // 2, self.height // 2
        radius = 210

        for i in range(0, 360, 15):
            start_angle = (i + self.angle) % 360
            color_val = int(
                100 + 155 * abs(math.sin(math.radians(start_angle))))
            color = f"#{color_val:02x}44ff"

            self.canvas.create_arc(
                cx - radius,
                cy - radius,
                cx + radius,
                cy + radius,
                start=start_angle,
                extent=10,
                outline=color,
                width=8,
                style="arc",
                tags="ring"
            )

        self.angle += 3

    def update_clock(self):
        current_time = time.strftime("%I:%M:%S %p")
        day_name = time.strftime("%A")
        date_string = time.strftime("%B %d, %Y")
        dev_name = "Developed by: Md. Shoeb Akhter"

        self.canvas.delete("text")
        cx, cy = self.width // 2, self.height // 2

        self.canvas.create_text(
            cx,
            cy - 30,
            text=current_time,
            fill="#ffffff",
            font=("Century Gothic", 55, "bold"),
            tags="text"
        )

        self.canvas.create_text(
            cx,
            cy + 45,
            text=f"{day_name} | {date_string}",
            fill="#00e5ff",
            font=("Century Gothic", 18),
            tags="text"
        )

        self.canvas.create_text(
            cx,
            self.height - 50,
            text=dev_name,
            fill="#555555",
            font=("Consolas", 12, "italic"),
            tags="text"
        )

        self.canvas.create_line(
            cx - 100,
            self.height - 35,
            cx + 100,
            self.height - 35,
            fill="#333333",
            tags="text"
        )

        self.draw_rounded_ring()
        self.root.after(20, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedWallpaper(root)
    root.mainloop()
