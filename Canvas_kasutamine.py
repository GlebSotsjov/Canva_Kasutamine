import tkinter as tk
from random import choice
from math import sqrt

# Функция для отображения флага Эстонии
def draw_estonia_flag(canvas):
    canvas.delete("item")
    canvas.create_rectangle(0, 0, 500, 100, fill="blue", tags="item")
    canvas.create_rectangle(0, 100, 500, 200, fill="black", tags="item") 
    canvas.create_rectangle(0, 200, 500, 300, fill="white", tags="item")

# Функция для отображения флага России
def draw_russia_flag(canvas):
    canvas.delete("item")
    canvas.create_rectangle(0, 0, 500, 100, fill="white", tags="item")
    canvas.create_rectangle(0, 100, 500, 200, fill="blue", tags="item")
    canvas.create_rectangle(0, 200, 500, 300, fill="red", tags="item")

# Функция для отображения флага Багамских островов
def draw_bahamas_flag(canvas):
    canvas.delete("item")
    canvas.create_rectangle(0, 0, 500, 100, fill="aqua", tags="item")
    canvas.create_rectangle(0, 100, 500, 200, fill="yellow", tags="item")
    canvas.create_rectangle(0, 200, 500, 300, fill="aqua", tags="item")
    canvas.create_polygon(0, 0, 250, 150, 0, 300, fill="black", outline="", tags="item")

# Функция для отображения радужного шара
def draw_rainbow_ball(canvas):
    canvas.delete("item")
    colors = ["black", "cyan", "magenta", "red", "blue", "gray", "yellow", "green", "lightblue", "pink", "gold"]
    x0 = 0
    y0 = 0
    x1 = 600
    y1 = 600
    p = 2
    for i in range(150):
        x0 += p
        y0 += p
        x1 -= p
        y1 -= p
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors), tags="item")

# Функция для отображения квадрата в квадрате
def draw_square_in_square(canvas):
    canvas.delete("item")
    k = 10
    x0 = 65
    y0 = 65
    x1 = 400
    y1 = 400
    a = 200
    r = int(sqrt(a ** 2 + a ** 2))
    p = a - r 
    for i in range(k):
        x0 += p 
        y0 += p 
        x1 -= p 
        y1 -= p
        canvas.create_rectangle(x0, y0, x1, y1, width=1, outline="blue", fill="Red", tags="item")
        canvas.create_oval(x0, y0, x1, y1, width=1, outline="blue", fill="Yellow", tags="item")
        p = r - a
        r = r - p
        a = int((r * sqrt(2)) / 2)

# Функция для отображения шахматной доски
def draw_chessboard(canvas):
    canvas.delete("item")
    size = 500
    rows = 8
    cols = 8
    square_size = size // max(rows, cols)
    colors = ["white", "black"]    
    for row in range(rows):
        for col in range(cols):            
            color_index = (row + col) % 2  # Alternating colors
            color = colors[color_index]            
            x0 = col * square_size
            y0 = row * square_size            
            x1 = x0 + square_size
            y1 = y0 + square_size            
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="", tags="item")

# Функция для отображения светофора
def draw_traffic_light(canvas, color):
    canvas.delete("item")
   # Отрисовка стержней светофора
    canvas.create_rectangle(95, 400, 105, 50, fill="gray", outline="black", width=2, tags="item")
    canvas.create_rectangle(95, 50, 105, 0, fill="gray", outline="black", width=2, tags="item")
   # Отрисовка кругов светофора
    canvas.create_oval(50, 50, 150, 150, fill="red" if color == "red" else "gray", outline="black", width=2, tags="item")
    canvas.create_oval(50, 170, 150, 270, fill="yellow" if color == "yellow" else "gray", outline="black", width=2, tags="item")
    canvas.create_oval(50, 290, 150, 390, fill="green" if color == "green" else "gray", outline="black", width=2, tags="item")
    

# Функция для обработки выбора элемента
def display_item():
    selected_item = item_var.get()
    if selected_item == "estonia":
        draw_estonia_flag(canvas)
    elif selected_item == "russia":
        draw_russia_flag(canvas)
    elif selected_item == "bahamas":
        draw_bahamas_flag(canvas)
    elif selected_item == "rainbow_ball":
        draw_rainbow_ball(canvas)
    elif selected_item == "square_in_square":
        draw_square_in_square(canvas)
    elif selected_item == "chessboard":
        draw_chessboard(canvas)
    elif selected_item == "traffic_light":
        draw_traffic_light(canvas, traffic_light_color_var.get())

# Создание окна Tkinter
root = tk.Tk()
root.title("Элементы")

# Создание холста
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(pady=20)

# Создание радиокнопок для выбора элемента
item_var = tk.StringVar()
item_var.set("estonia")
estonia_radio = tk.Radiobutton(root, text="Флаг Эстонии", variable=item_var, value="estonia", command=display_item)
estonia_radio.pack(pady=5)
russia_radio = tk.Radiobutton(root, text="Флаг России", variable=item_var, value="russia", command=display_item)
russia_radio.pack(pady=5)
bahamas_radio = tk.Radiobutton(root, text="Флаг Багамских островов", variable=item_var, value="bahamas", command=display_item)
bahamas_radio.pack(pady=5)
rainbow_radio = tk.Radiobutton(root, text="Радужный шар", variable=item_var, value="rainbow_ball", command=display_item)
rainbow_radio.pack(pady=5)
square_radio = tk.Radiobutton(root, text="Квадрат в квадрате", variable=item_var, value="square_in_square", command=display_item)
square_radio.pack(pady=5)
chessboard_radio = tk.Radiobutton(root, text="Шахматная доска", variable=item_var, value="chessboard", command=display_item)
chessboard_radio.pack(pady=5)
traffic_light_radio = tk.Radiobutton(root, text="Светофор", variable=item_var, value="traffic_light", command=display_item)
traffic_light_radio.pack(pady=5)

# Создание радиокнопок для выбора цвета светофора
traffic_light_color_var = tk.StringVar()
traffic_light_color_var.set("red")
red_radio = tk.Radiobutton(root, text="Красный", variable=traffic_light_color_var, value="red", command=display_item)
red_radio.pack(pady=5)
yellow_radio = tk.Radiobutton(root, text="Желтый", variable=traffic_light_color_var, value="yellow", command=display_item)
yellow_radio.pack(pady=5)
green_radio = tk.Radiobutton(root, text="Зеленый", variable=traffic_light_color_var, value="green", command=display_item)
green_radio.pack(pady=5)

# Отображение начального элемента
draw_estonia_flag(canvas)

root.mainloop()
