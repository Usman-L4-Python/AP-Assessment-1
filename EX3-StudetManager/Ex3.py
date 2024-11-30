import tkinter as tk
from tkinter import messagebox

def load(filePath):
    data = []
    try:
        with open(filePath, "r") as file:
            count = file.readline().strip()
            if not count.isdigit():
                messagebox.showerror("Error", "The first line must indicate the number of students.")
                return []

            for line in file:
                row = line.strip().split(",")
                if len(row) != 6:
                    messagebox.showerror("Error", "Each line should have exactly 6 fields.")
                    return []

                code = int(row[0])
                name = row[1].strip()
                coursework = sum(map(int, row[2:5]))
                exam = int(row[5])
                total = coursework + exam
                percent = (total / 160) * 100
                grade = "A" if percent >= 70 else "B" if percent >= 60 else "C" if percent >= 50 else "D" if percent >= 40 else "F"
                data.append({"code": code, "name": name, "coursework": coursework, "exam": exam, "total": total, "percent": percent, "grade": grade})
    except:
        messagebox.showerror("Error", "There was an issue reading the file.")
    return data

def viewAll():
    if not records:
        messagebox.showinfo("Information", "No records found.")
        return
    text = ""
    for record in records:
        text += f"{record['name']} (ID: {record['code']}): Coursework: {record['coursework']}, Exam: {record['exam']}, Percentage: {record['percent']:.2f}%, Grade: {record['grade']}\n"
    text += f"\nTotal Students: {len(records)}, Average Percentage: {sum(r['percent'] for r in records) / len(records):.2f}%"
    result.config(text=text)

def viewIndividual():
    search = entry.get().strip().lower()
    for record in records:
        if record["name"].lower() == search:
            result.config(text=f"{record['name']} (ID: {record['code']}): Coursework: {record['coursework']}, Exam: {record['exam']}, Percentage: {record['percent']:.2f}%, Grade: {record['grade']}")
            return
    messagebox.showinfo("Information", "Student not found.")

def highestScore():
    if not records:
        messagebox.showinfo("Information", "No records available.")
        return
    top = max(records, key=lambda x: x["total"])
    result.config(text=f"Highest Score: {top['name']} (ID: {top['code']}): Coursework: {top['coursework']}, Exam: {top['exam']}, Percentage: {top['percent']:.2f}%, Grade: {top['grade']}")

def lowestScore():
    if not records:
        messagebox.showinfo("Information", "No records found.")
        return
    low = min(records, key=lambda x: x["total"])
    result.config(text=f"Lowest Score: {low['name']} (ID: {low['code']}): Coursework: {low['coursework']}, Exam: {low['exam']}, Percentage: {low['percent']:.2f}%, Grade: {low['grade']}")

root = tk.Tk()
root.title("Student Records")
root.geometry("600x400")

records = load("Marks.txt")

entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="View All Records", command=viewAll).pack(pady=5)
tk.Button(root, text="View Student", command=viewIndividual).pack(pady=5)
tk.Button(root, text="Highest Score", command=highestScore).pack(pady=5)
tk.Button(root, text="Lowest Score", command=lowestScore).pack(pady=5)

result = tk.Label(root, text="", wraplength=500, justify="left")
result.pack(pady=10)

root.mainloop()
