import tkinter as tk

def check_numbers(numbers):
    check_failed = len(numbers) > 12\
     or len(numbers) >= 6 and sums[0] != numbers[0] + numbers[1] + numbers[4] + numbers[5]\
     or len(numbers) >= 7 and sums[1] != numbers[1] + numbers[2] + numbers[5] + numbers[6]\
     or len(numbers) >= 8 and sums[2] != numbers[2] + numbers[3] + numbers[6] + numbers[7]\
     or len(numbers) >= 10 and sums[3] != numbers[4] + numbers[5] + numbers[8] + numbers[9]\
     or len(numbers) >= 11 and sums[4] != numbers[5] + numbers[6] + numbers[9] + numbers[10]\
     or len(numbers) == 12 and sums[5] != numbers[6] + numbers[7] + numbers[10] + numbers[11]
    return not check_failed

def find_solutions(guess, numbers):
    if check_numbers(guess):
        if len(numbers) == 0:
            solutions.append(guess)
        else:
            for i in range(len(numbers)):
                new_guess = guess + [numbers[i]]
                new_numbers = numbers[:i] + numbers[i+1:]
                if len(new_guess) == user_num1_pos:
                    new_guess.insert(user_num1_pos, user_num1)
                elif len(new_guess) == user_num2_pos:
                    new_guess.insert(user_num2_pos, user_num2)
                find_solutions(new_guess, new_numbers)

user_num1 = 1
user_num1_pos = 4
user_num2 = 5
user_num2_pos = 7
sums = [23, 37, 30, 27, 40, 24]
numbers = [elem for elem in range(1,13) if elem not in [user_num1, user_num2]]
solutions = []
find_solutions([], numbers)

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

