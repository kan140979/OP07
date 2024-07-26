"""Напишите программу на Python с использованием модуля tkinter,
оторая позволяет пользователю ввести свое имя в окно ввода,
а затем выводит на экран сообщение "Привет, [имя]!"."""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Первый проект")

def on_button_click():
    messagebox.showinfo("Приветствие", f"Привет, {entry.get()}!")
    #label.config(text=f"Привет, {entry.get()}!")

label = tk.Label(root, text="Введите свое имя в поле ввода")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Вывести сообщение", command=on_button_click)
button.pack()

root.mainloop()
