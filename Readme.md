<H1>
File Handling Made Eazy!
</H1>



<h2>What Project is all about?</h2>  

****CRUD operation System for files****


## What It Does

FileOps wraps Python's built-in file I/O and the `os` module into a clean menu-driven interface. No external libraries needed — just pure Python 3.

- **Create** — Initialise a new empty file using exclusive mode (`open(name, 'x')`)
- **Read** — Open and print the full contents of any file (`open(name, 'r')`)
- **Update** — Overwrite (`'w'`) or append (`'a'`) content to an existing file
- **Delete** — Permanently remove a file using `os.remove()`

---

## How to Run

Make sure you have Python installed, then:

```bash
python Main.py
```

Follow the on-screen menu:

```
Press 1 for creating a file
Press 2 for Reading a file
Press 3 for Updating a file
Press 4 for deleting a file
Press other number to Exit
```

---

## Web UI

Open `UI.html` in any browser for a visual, terminal-style interface that mirrors the same CRUD operations in a live interactive demo — no server needed.


---

## File Structure

```
FileOps/
│
├── Main.py        # Core CLI file manager (Python 3)
├── UI.html        # Terminal-style web UI demo
└── README.md      # Project documentation
```

---


## Author

**Atharv Vhanalkar** — CS Student, UpGrad Pune  
Built as a Python fundamentals project exploring file I/O operations.
