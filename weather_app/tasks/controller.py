import questionary
from questionary import Choice
from rich.console import Console
from tasks.storage import TasksStorage
from tasks.ui import TaskDisplay

console = Console()

# Initialize storage here (or pass it in)
task_db = TasksStorage()


class TaskController:
    """This is the main controller for the tasks"""

    @staticmethod  # <--- CRITICAL FIX
    def run():
        console.clear()
        taskChoice = questionary.select(
            "Which service do you need?",
            choices=[
                "Add Task",
                "Edit Task",
                "Delete Task",
                "Mark Task Done",
                "List Pending",
                "List All",
                "Back",
            ],  # Added "Back"
        ).ask()

        console.print("[bold cyan]Managing tasks...[/]")
        # adds new task
        if taskChoice == "Add Task":
            try:
                task_title = questionary.text("Enter task title:").ask()
                task_content = questionary.text("Enter task content:").ask()
                date_str = questionary.text(
                    "Enter deadline (YYYY-MM-DD) or leave blank:"
                ).ask()

                task_end_by = None
                if date_str:
                    try:
                        from datetime import datetime

                        task_end_by = datetime.strptime(date_str, "%Y-%m-%d")
                    except ValueError:
                        console.print(
                            "[red]Invalid format! Saving without deadline.[/]"
                        )

                task_db.add_task(
                    title=task_title, content=task_content, end_by=task_end_by
                )
            except Exception as e:
                console.print(f"[red]Error: {e}[/]")
        # marks tasks done
        elif taskChoice == "Mark Task Done":
            task = questionary.text("enter the task id").ask()

            if task:

                try:
                    task_db.mark_task_done(task)

                except Exception as e:
                    print(f"error {e}")
        # lists all pending tasks in the database
        elif taskChoice == "List Pending":
            results = task_db.get_pending_task()
            TaskDisplay.display_tasks_table(results, title="Pending Tasks")
        # lists all the tasks in the database
        elif taskChoice == "List All":
            console.print("Fetching tasks...")
            try:
                tasks = task_db.list_all_tasks()
                TaskDisplay.display_tasks_table(tasks, title="All Tasks")
            except Exception as e:
                console.print(f"[red]Error: {e}[/]")

        # edit task
        elif taskChoice == "Edit Task":
            try:
                tasks = task_db.list_all_tasks()
                choices = [
                    Choice(title=f"{x.id}.  {x.title}", value=x.id) for x in tasks
                ]
                choosenTask = questionary.select(
                    "choose the task to edit", choices=choices
                ).ask()

                # get's the task by id
                task = task_db.get_task_by_id(choosenTask)
                if task:
                    new_title = questionary.text(
                        "enter a new title or leave blank: "
                    ).ask()
                    if new_title == "":
                        new_title = task.title

                    new_content = questionary.text(
                        "enter the content or leave blank"
                    ).ask()
                    if new_content == "":
                        new_content = task.content

                    new_end_by_input = questionary.text(
                        "enter a new end date or leave blank"
                    ).ask()
                    if new_end_by == "":
                        new_end_by = task.end_by
                        try:
                            from datetime import datetime

                            new_end_by = datetime.strptime(new_end_by_input, "%Y-%m-%d")
                        except ValueError:
                            print("Invalid date format, keeping old date.")
                            new_end_by = task.end_by

                    task_db.edit_task(task.id, new_title, new_content, new_end_by)
                    task_after_update = task_db.get_task_by_id(task.id)
                    TaskDisplay.display_tasks_table(
                        [task_after_update], title=f"updated task {task.id}"
                    )
            except Exception as e:
                print(e)

        elif taskChoice == "Delete Task":
            try:
                tasks = task_db.list_all_tasks()
                choices = [
                    Choice(title=f"{x.id}.  {x.title}", value=x.id) for x in tasks
                ]
                choosenTask = questionary.select(
                    "choose the task to delete", choices=choices
                ).ask()

                if choosenTask:
                    try:
                        task_db.delete_task(choosenTask)
                    except Exception as e:
                        print(e)

            except Exception as e:
                print(e)

        elif taskChoice == "Back":
            return  # Just return to main menu
