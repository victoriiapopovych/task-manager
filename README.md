# 📝 Task Manager: Smart Console Productivity App

This project is a console-based task manager application built with Python.  
It helps users organize their tasks, track progress, and improve productivity using simple and efficient tools.

---

## 🔐 Core Functionality

- Add new tasks with category and priority
- View all tasks in a structured format
- Mark tasks as completed
- Delete tasks
- Automatically save and load tasks using JSON

---

## 📋 Task Structure

Each task contains:

- **ID** — unique identifier
- **Title** — task description
- **Status** — Done / Not done
- **Category** — e.g. study, work, personal
- **Priority** — low, medium, high

---

## ⚙️ Features

### 🟢 Task Management
- Create new tasks
- Delete existing tasks
- Mark tasks as completed
- Display all tasks

### 💾 Data Persistence
- Tasks are saved in a `tasks.json` file
- Data is automatically loaded when the program starts

### 🧠 Object-Oriented Design
- `Task` class represents a single task
- `TaskManager` class manages all tasks