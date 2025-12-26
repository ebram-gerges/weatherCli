from datetime import datetime

from rich.console import Console
from rich.table import Table

console = Console()


class TaskDisplay:
    @staticmethod
    def display_tasks_table(tasks, title="Task List"):
        """
        Takes a list of Task objects and prints a pretty table.
        """
        # 0. Normalize Data: If it's a single object (not a list), wrap it in a list.
        if tasks and not isinstance(tasks, list):
            tasks = [tasks]

        if not tasks:
            console.print(f"[yellow]No tasks found for: {title}[/]")
            return

        # 1. Create the Table
        table = Table(title=title, show_header=True, header_style="bold magenta")

        # 2. Add Columns
        table.add_column("ID", style="cyan", width=4)
        table.add_column("Title", style="green")
        table.add_column("Content", style="white")
        table.add_column("Status", justify="center")
        table.add_column("Deadline", style="red")

        # 3. Loop through tasks and add rows
        for task in tasks:
            # Format status
            status = "[green]Done[/]" if task.is_done else "[yellow]Pending[/]"

            # Format Date (Handle None)
            if task.end_by:
                deadline = task.end_by.strftime("%Y-%m-%d")
            else:
                deadline = "No Deadline"

            # Add the row
            table.add_row(str(task.id), task.title, task.content, status, deadline)

        # 4. Print the table
        console.print(table)
