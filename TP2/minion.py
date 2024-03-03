import queue
import time

from manager import QueueClient as QC


# define the ppeasant working for the bossman
class Minion(QC):
    def __init__(self):
        super().__init__()

    def run(self):

        while True:
            # pick smting to do
            try:
                time.sleep(1)  # infinite loop elsewise
                task = self.tasks.get_nowait()

            except queue.Empty:
                print("No tasks to fufill")
                time.sleep(5)
                continue

            # actually does the work
            task.work()
            # record the results
            self.results.put((task.id, task.time))
            # com the result
            print(f"The task {task.id} has been completed in {task.time}")
