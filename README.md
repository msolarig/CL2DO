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
*   Clear, check, uncheck entire list with a single command

---

## Installation

CL2DO can be installed and ran natively on MacOS, Windows, and Linux machines by following these steps:
	
 1.	Clone the repository:

	```
 	git clone https://github.com/msolarig/CL2DO.git

 	cd CL2DO/src
	```
 
2.	Make sure you have Python 3 installed on your system:

	```
	python3 --version
 	```
 
3.	Run the application:

	```
	python3 main.py
	```
 
 The application has not been bundled into an executable or .app file due to distribution limitations. It is recommended to automate the access to CL2DO with additional tools such as MacOS' Automator or a hot key manager.
 
 This is an example of how I have it setup with an automator .app! I have included the same png with the identifier I used (notebook emoji) in the assets directory.
 
 ![Alt text](/assets/screenshots/screenshot_2(?).png?raw=true "screenshot 2")
 

---

## Usage

Once running, the app displays your current task list and waits for commands. Commands are typed directly into the terminal.

Entire List of Commands
* add '<task>'
* rem '<task>'
* remall
* check '<task>'
* checkall
* uncheck '<task>'
* uncheckall
* q

Command Examples
* add Buy groceries
* check Buy groceries
* uncheck Buy groceries
* rem Buy groceries
* remall
* checkall
* uncheckall
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

## Contributing

This is a project I made primarily for personal use. Still, contributions are welcome! Feel free to fork the repo, submit issues, or propose new features.

---

## License

This project is licensed under the GNU GPL v3.0 License.
