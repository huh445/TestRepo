import tkinter as tk
import random
import tkinter as tk
import random

def selection_sort(scores):
    sorted_scores = scores[:]  
    for i in range(len(sorted_scores)):
        min_idx = i
        for j in range(i + 1, len(sorted_scores)):
            if sorted_scores[j] < sorted_scores[min_idx]:
                min_idx = j
        sorted_scores[i], sorted_scores[min_idx] = sorted_scores[min_idx], sorted_scores[i]
        update_canvas(sorted_scores)  
        root.update()
    return sorted_scores  
    
def quick_sort(scores):
    root.update()
    root.after(5)
    if len(scores) <= 1:
        root.update()
        return scores
    else:
        pivot = scores[0]
        less_than_pivot = [x for x in scores[1:] if x <= pivot]
        root.update()
        greater_than_pivot = [x for x in scores[1:] if x > pivot]
        root.update()
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def update_canvas(scores):
    canvas.delete("all")
    width = float(2)
    max_score = max(scores)
    height_ratio = 250 / max_score
    for i, score in enumerate(scores):
        x0 = i * width
        y0 = 300
        x1 = x0 + width
        y1 = y0 - score * height_ratio
        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        canvas.create_text((x0 + x1) / 2, y1 - 10, text=str(score))

def start_sorting(sort_func):
    global exam_scores
    sorted_scores = sort_func(exam_scores)
    update_canvas(sorted_scores)
root = tk.Tk()
root.title("Exam Scores Sorting Visualisation")
root.geometry("500x400")

canvas = tk.Canvas(root, width=10000, height=300, bg="white")
canvas.pack()

exam_scores = [random.randint(1, 400) for _ in range(1000)]

update_canvas(exam_scores)

selection_sort_button = tk.Button(root, text="Start Selection Sort", command=lambda: start_sorting(selection_sort))
selection_sort_button.pack(side=tk.LEFT)

quick_sort_button = tk.Button(root, text="Start Quick Sort", command=lambda: start_sorting(quick_sort))
quick_sort_button.pack(side=tk.RIGHT)

randomize = tk.Button(root, text="Start Randomize", command=lambda: update_canvas(exam_scores))
randomize.pack(side=tk.BOTTOM)

root.mainloop()