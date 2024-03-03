import queue
import time

from manager import QueueClient as QC
from task import Task as T


# difine what is a boss
class Boss(QC):
    def __init__(self):
        super().__init__()

    def sub_task(self, task_id, task_size):
        task = T(task_id, task_size)

        self.tasks.put(task)

        print(f"The Boss require {task_id} to be done")

    def run(self):
        while True:
            try:
                result_id, result_time = self.results.get_nowait()
                print(f"The Boss had to wait {result_time} to see {result_id} done")
            except queue.Empty:
                print("There is nothing to be done")
                time.sleep(5)
                continue
