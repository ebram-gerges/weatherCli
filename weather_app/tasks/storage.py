from database import SessionLocal
from tasks.models import Tasks


class TasksStorage:
    """this class's job is to save and fetch the tasks"""

    def add_task(self, title, content, end_by=None):
        session = SessionLocal()

        try:
            # trys to create new task

            new_task = Tasks(
                title=title,
                content=content,
                end_by=end_by,
            )

            session.add(new_task)
            session.commit()
            print("✅ Task Saved!")
        except Exception as e:
            # prints the error if couldn't create task

            print(e)
        finally:
            # closes the session after ok or error
            session.close()

    def get_pending_task(self):
        # get all the tasks with with is_done
        session = SessionLocal()

        try:
            # trys to query
            results = session.query(Tasks).filter(Tasks.is_done == False).all()
            return results

        except Exception as e:
            print(e)
            return []
        finally:
            session.close()

    def mark_task_done(self, task_id):
        session = SessionLocal()

        try:
            task = session.query(Tasks).filter(Tasks.id == task_id).first()
            if task:
                task.is_done = True
                session.commit()
                print("✅ task updated!")
            else:
                print("❌ task not found!")

        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def list_all_tasks(self):
        session = SessionLocal()

        try:
            tasks = session.query(Tasks).order_by(Tasks.id.asc()).all()
            return tasks
        except Exception as e:
            print(f"error: {e}")
            return []
        finally:
            session.close()

    def edit_task(self, taskID, taskTitle, taskContent, taskEndBy):
        session = SessionLocal()
        try:
            task = session.query(Tasks).filter(Tasks.id == taskID).first()
            task.title = taskTitle
            task.content = taskContent
            task.end_by = taskEndBy
            session.commit()
        except Exception as e:
            print(e)
        finally:
            session.close()

    # get's a specific task
    def get_task_by_id(self, id):
        session = SessionLocal()
        try:
            task = session.query(Tasks).filter(Tasks.id == id).first()
            return task
        except Exception as e:
            print(e)
        finally:
            session.close()

    def delete_task(self, taskID):
        session = SessionLocal()

        try:
            task = session.query(Tasks).filter(Tasks.id == taskID).first()
            if task:
                session.delete(task)
                session.commit()
            else:
                return {"error": "we couldn't get your task sorry"}
        except Exception as e:
            print(e)
        finally:
            session.close()
