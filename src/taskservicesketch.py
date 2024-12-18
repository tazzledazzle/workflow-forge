# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import sqlite3



class TaskServiceSketch:

    def __init__(self):
        self.connection = sqlite3.connect("tasks.db")
        self.cursor = self.connection.cursor()

    # Update a task's status
    def update_task_status(self, task_id: int, status: str):
        """Update the status of a task."""
        try:
            self.cursor.execute("""
            UPDATE tasks
            SET status = ?
            WHERE id = ?
            """, (status, task_id))
            self.connection.commit()
            print(f"Task ID {task_id} status updated to '{status}'.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            self.connection.close()

    # Delete a task
    def delete_task(self, task_id: int):
        """Delete a task from the database."""
        try:
            self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            self.connection.commit()
            print(f"Task ID {task_id} deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            self.connection.close()

    def setup_db_schema(self):
        # Create a table for tasks if it doesn't already exist
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.connection.commit()
        self.connection.close()

    def save_task(self, title: str, description: str = "", status: str = "pending"):
        """Save a task to the SQLite database."""
        try:
            # Insert the task into the tasks table
            self.cursor.execute("""
            INSERT INTO tasks (name, description, status)
            VALUES (?, ?, ?)
            """, (title, description, status))

            # Commit the transaction
            self.connection.commit()
            print(f"Task '{title}' saved successfully!")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the database connection
            self.connection.close()

    def list_tasks(self):
        tasks = []
        try:
            # select all the tasks
            self.cursor.execute("""
            SELECT * FROM tasks""", ())
            rows = self.cursor.fetchall()
            for row in rows:
                tasks.append({
                    "id": row[0],
                    "name":  row[1],
                    "description": row[2],
                    "status": row[3],
                    "created_at": row[4]
                })
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            self.connection.close()

        return tasks
