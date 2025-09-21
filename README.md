# CL2DO -> A CLI 2do List

Are you tired of over-complicated, resource-intensive applications that always seem to have a subscription-based model?

I was.

So I made CL2DO!

A simple task manager that runs straight from the terminal. No background processes. No subscriptions.

---

## Features
*   Add new tasks with a single command
*   Remove tasks when they’re completed or no longer needed
*	Mark tasks as complete or incomplete
*   Automatic persistence: tasks are saved locally and loaded every time the app runs
*	Simple, clear terminal interface with real-time task list display

---

## Installation
	
 1.	Clone the repository:

	```
 	git clone https://github.com/msolarig/CL2DO.git

 	cd CL2DO
	```
 
2.	Make sure you have Python 3 installed on your system:

	```
	python3 --version
 	```
 
3.	Run the application:

	```
	python3 main.py
	```


---

## Usage

Once running, the app displays your current task list and waits for commands. Commands are typed directly into the terminal.

Entire List of Commands
* add '<task>'
* rem '<task>'
* check '<task>'
* uncheck '<task>'
* q

Command Examples
* add Buy groceries
* check Buy groceries
* uncheck Buy groceries
* rem Buy groceries
* q (Quit Application)

Tasks are displayed in the format:

```
[ ] Task description   # incomplete
[x] Task description   # completed
```

---

## File Storage

* Tasks are stored in a simple text file called task_file.txt within the project directory.
* Each line represents a task with its status, e.g., [ ] Buy groceries or [x] Walk the dog.
* This makes it easy to edit or back up tasks manually if needed.

---
## Screenshots

![Alt text](/assets/screenshots/screenshot_1.png?raw=true "Screenshot 1")

---

## Future Improvements

* Error handling for invalid commands or missing tasks
* Task numbering for easier selection
* Optional priority or category system
* Extra functionality such as mark all or clean list
* Potential packaging as a standalone executable for macOS, Linux, and Windows

---

## Contributing

Contributions are welcome! Feel free to fork the repo, submit issues, or propose enhancements.

---

## License

This project is licensed under the GNU GPL v3.0 License.
