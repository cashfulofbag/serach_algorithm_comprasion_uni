import random
import tkinter as tk
from tkinter import ttk
import time

# Just pseudorandom guessing 
def random_search(target, lst):
    count = 0
    guess = 0
    while guess != target:
        count += 1
        guess = random.choice(lst)
    return count

# Simple iteration    
def iterate_search(target, lst):
    count = 0
    for value in lst:
        count += 1
        if value == target:
            return count

# Binary search 
def binary_search(target, lst):
    low = 0
    high = len(lst) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            return count
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return count

# Interpolation search
def interpolation_search(target, lst):
    low = 0
    high = len(lst) - 1
    count = 0

    while low <= high and lst[low] <= target <= lst[high]:
        count += 1
        if low == high:
            if lst[low] == target:
                return count
            return None

        pos = low + ((target - lst[low]) * (high - low)) // (lst[high] - lst[low])
        if pos < low or pos > high:
            return None

        if lst[pos] == target:
            return count
        elif lst[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return None

def start_search():
    #Generate list
    list_numbers = list(range(1, 1000001))
    random.shuffle(list_numbers)
    
    #Check if user input is valid
    try:
        target = int(target_value.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number between 1 and 1,000,000.")
        return
    
    if target < 1 or target > 1000000:
        result_label.config(text="Please enter a number between 1 and 1,000,000.")
        return
    
    #Start search algorithms with timing
    start = time.time()
    count = random_search(target, list_numbers)
    end = time.time()
    elapsed = end - start
    result_label_random.config(text=f"Guessing: {elapsed:.6f} seconds in {count} iterations")
    
    start = time.time()
    count = iterate_search(target, list_numbers)
    end = time.time()
    elapsed = end - start
    result_label_iter.config(text=f"Iterating: {elapsed:.6f} seconds in {count} iterations")
    
    start = time.time()
    list_numbers.sort()
    end = time.time()
    elapsed = end - start
    result_label_sort.config(text=f"Sorting: {elapsed:.6f} seconds")
    
    start = time.time()
    count = binary_search(target, list_numbers)
    end = time.time()
    elapsed = end - start
    result_label_bin.config(text=f"Binary search: {elapsed:.6f} seconds in {count} iterations")
    
    start = time.time()
    count = interpolation_search(target, list_numbers)
    end = time.time()
    elapsed = end - start
    result_label_inter.config(text=f"Interpolation search: {elapsed:.6f} seconds in {count} iterations")

# Initialize tkinter
main = tk.Tk()
main.title("Search Algorithms Comparison")
main.geometry("600x400")

#Set style
style = ttk.Style(main)
style.theme_use('alt')

frame = ttk.Frame(main, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Create field for user input
target_label = ttk.Label(frame, text="Enter a number between 1 and 1,000,000:")
target_label.pack(pady=5)

target_value = ttk.Entry(frame)
target_value.pack(pady=5)

# Create search button
search = ttk.Button(frame, text="Start Searching", command=start_search)
search.pack(pady=10)

# Labels to return time and number of iterations used to reach target value
result_label = ttk.Label(frame, text="")
result_label.pack(pady=5)

result_label_random = ttk.Label(frame, text="Guessing: ")
result_label_random.pack(pady=5)

result_label_iter = ttk.Label(frame, text="Iterating: ")
result_label_iter.pack(pady=5)

result_label_sort = ttk.Label(frame, text="Sorting: ")
result_label_sort.pack(pady=5)

result_label_bin = ttk.Label(frame, text="Binary search: ")
result_label_bin.pack(pady=5)

result_label_inter = ttk.Label(frame, text="Interpolation search: ")
result_label_inter.pack(pady=5)

# Start tkinter window main loop
main.mainloop()