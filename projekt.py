def check_numbers(arr):
    if len(arr) > 12:
        return False
    else:
        return sums[5] == arr[6] + arr[7] + arr[10] + arr[11] and sums[4] == arr[5] + arr[6] + arr[9] + arr[10] and sums[3] == arr[4] + arr[5] + arr[8] + arr[9] and sums[2] == arr[2] + arr[3] + arr[6] + arr[7] and sums[1] == arr[1] + arr[2] + arr[5] + arr[6] and sums[0] == arr[0] + arr[1] + arr[4] + arr[5]

def permute(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr]
    else:
        res = []
        for i in range(len(arr)):
            elem = arr[i]
            rem = arr[:i] + arr[i+1:]
            for p in permute(rem):
                res.append([elem] + p)
        return res

user_num1 = 1
user_num1_pos = 4
user_num2 = 5
user_num2_pos = 7
sums = [23, 37, 30, 27, 40, 24]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
arr = [elem for elem in arr if elem not in [user_num1, user_num2]]

perm_arr = permute(arr)

solutions = []
for perm in perm_arr:
    perm_to_check = perm[:user_num1_pos] + [user_num1] + perm[user_num1_pos:user_num2_pos-1] + [user_num2] + perm[user_num2_pos-1:]
    if check_numbers(perm_to_check):
        solutions.append(perm_to_check)

if len(solutions) == 0:
    print("Nincs megoldás!")
else:
    for solution in solutions:
        for i in range(len(solution)):
            print(str(solution[i]).center(4), end=" ")
            if i == 3:
                print("\n " + ("(" + str(sums[0]) + ")").center(5) + ("(" + str(sums[1]) + ")").center(5) + ("(" + str(sums[2]) + ")").center(5))
            if i == 7:
                print("\n " + ("(" + str(sums[3]) + ")").center(5) + ("(" + str(sums[4]) + ")").center(5) + ("(" + str(sums[5]) + ")").center(5))
