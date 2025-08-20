
# ✏️ Undo-Redo System (Python)
This is a simple Python program that implements an *Undo and Redo system* using stacks.  
It allows you to make changes, undo them, redo them, and display the current text.

---

## 📌 How It Works

1. The user can enter a string using the *Make Changes* option.  
2. All changes are stored in an *Undo Stack*.  
3. When undo is used, the last change is removed from the Undo Stack and pushed into the *Redo Stack*.  
4. When redo is used, the last undone change is moved back to the Undo Stack.  
5. Display option shows the current text present in the Undo Stack.  

---

## 🛠️ Technologies Used

- Python 3  
- List (used as stack for Undo and Redo operations)  

---

## Example 
----Menu----

1. Make Changes
2. Undo
3. Redo
4. Display
5. Exit
Enter your Choice: 1 Enter String: Hello
Enter your Choice: 1 Enter String: World
Enter your Choice: 4 Current Text: Hello World
Enter your Choice: 2 (Undo done)
Enter your Choice: 4 Current Text: Hello

---
👨‍💻 About Me

I'm Prajwal Butte, currently in 2nd year of Computer Engineering at Trinity College of Engineering and Research, Pune.
I'm learning Python, Java, and Web Development by building small, useful projects like this one.
My goal is to get a good placement by final year with a strong project portfolio.

---
## 🚀 How to Run

1. Save the code in a file named undo_redo.py.  
2. Run the file using:  

```bash
python undo_redo.py



