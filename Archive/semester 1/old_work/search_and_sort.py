import tkinter as tk
import random

def selection_sort(scores):
    for i in range(len(scores)):
        min_idx = i
        for j in range(i + 1, len(scores)):
            if scores[j] < scores[min_idx]:
                min_idx = j
        scores[i], scores[min_idx] = scores[min_idx], scores[i]
        update_canvas(scores)

def update_canvas(scores):
    canvas.delete("all")
    width = 20
    max_score = max(scores)
    height_ratio = 250 / max_score
    for i, score in enumerate(scores):
        x0 = i * width
        y0 = 300
        x1 = x0 + width
        y1 = y0 - score * height_ratio
        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        canvas.create_text((x0+x1) / 2,y1 -10, text=str(score))

        
def start_sorting():
    global exam_scores
    selection_sort(exam_scores)

root = tk.Tk()
root.title("Exam Scores Sorting Visualisation")
root.geometry("500x400")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

exam_scores = [random.randint(50, 100) for _ in range(20)]

update_canvas(exam_scores)

sort_button = tk.Button(root, text="Start Sorting", command=start_sorting)
sort_button.pack()

root.mainloop()