import itertools
import tkinter as tk

#def permute(arr):
#    if len(arr) == 0:
#        return []
#    elif len(arr) == 1:
#        return [arr]
#    else:
#        res = []
#        for i in range(len(arr)):
#            elem = arr[i]
#            rem = arr[:i] + arr[i+1:]
#            for p in permute(rem):
#                res.append([elem] + p)
#        return res

def check_numbers(arr):
    if len(arr) != 12:
        return False
    else:
        return sums[5] == arr[6] + arr[7] + arr[10] + arr[11] and sums[4] == arr[5] + arr[6] + arr[9] + arr[10] and sums[3] == arr[4] + arr[5] + arr[8] + arr[9] and sums[2] == arr[2] + arr[3] + arr[6] + arr[7] and sums[1] == arr[1] + arr[2] + arr[5] + arr[6] and sums[0] == arr[0] + arr[1] + arr[4] + arr[5]

user_num1 = 1
user_num1_pos = 4
user_num2 = 5
user_num2_pos = 7
sums = [23, 37, 30, 27, 40, 24]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
arr = [elem for elem in arr if elem not in [user_num1, user_num2]]

perm_arr = itertools.permutations(arr)

solutions = []
for perm in perm_arr:
    perm = list(perm)
    perm_to_check = perm[:user_num1_pos] + [user_num1] + perm[user_num1_pos:user_num2_pos-1] + [user_num2] + perm[user_num2_pos-1:]
    if check_numbers(perm_to_check):
        solutions.append(perm_to_check)

if len(solutions) == 0:
    print("Nincs megoldás!")
else:
    cells = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    solved_values = dict(zip(cells, solutions[0]))

    def draw_puzzle(canvas, start_x, start_y, title, values):
       
        canvas.create_text(
            start_x + 160, start_y - 30,
            text=title,
            font=("Arial", 14, "bold")
        )

        cell_pos = {
            "a": (start_x + 40,  start_y + 40),
            "b": (start_x + 120, start_y + 40),
            "c": (start_x + 200, start_y + 40),
            "d": (start_x + 280, start_y + 40),
    
            "e": (start_x + 40,  start_y + 120),
            "f": (start_x + 120, start_y + 120),
            "g": (start_x + 200, start_y + 120),
            "h": (start_x + 280, start_y + 120),
    
            "i": (start_x + 40,  start_y + 200),
            "j": (start_x + 120, start_y + 200),
            "k": (start_x + 200, start_y + 200),
            "l": (start_x + 280, start_y + 200),
        }

        circle_pos = [
            (start_x + 80,  start_y + 80, sums[0]),
            (start_x + 160, start_y + 80, sums[1]),
            (start_x + 240, start_y + 80, sums[2]),
            (start_x + 80,  start_y + 160, sums[3]),
            (start_x + 160, start_y + 160, sums[4]),
            (start_x + 240, start_y + 160, sums[5]),
        ]
    
        box_size = 34
        for cell, (x, y) in cell_pos.items():
            canvas.create_rectangle(
                x - box_size // 2, y - box_size // 2,
                x + box_size // 2, y + box_size // 2,
                width=2
            )

            value = values.get(cell)
            if value is not None:
                canvas.create_text(
                    x, y,
                    text=str(value),
                    font=("Arial", 16, "bold")
                )

        r = 18
        for x, y, number in circle_pos:
            canvas.create_oval(x - r, y - r, x + r, y + r, width=2)
            canvas.create_text(
                x, y,
                text=str(number),
                font=("Arial", 11, "bold")
            )

    original_values_arr = [None] * 12
    original_values_arr[user_num1_pos] = user_num1
    original_values_arr[user_num2_pos] = user_num2
    original_values = dict(zip(cells, original_values_arr))

    root = tk.Tk()
    root.title("Számok a szomszédban")

    canvas = tk.Canvas(root, width=760, height=470, bg="white")
    canvas.pack()

    canvas.create_text(
        380, 30,
        text=f"Talált megoldások száma: {len(solutions)}",
        font=("Arial", 16, "bold"),
        justify="center"
    )

    draw_puzzle(canvas, 30, 200, "Feladvány", original_values)
    draw_puzzle(canvas, 400, 200, "Lehetséges kitöltés", solved_values)
    
    root.mainloop()
