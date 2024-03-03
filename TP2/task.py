import json
import time

import numpy as np


# define what is a task
class Task:

    # initialize the task and it's args
    def __init__(self, id, size=None, x=None, y=None):
        self.id = id  # task identifyer

        self.size = size or np.random.randint(
            300, 3_000
        )  # size of the task, determinated or randomized
        self.x = x or np.random.rand(
            self.size, self.size
        )  # matrix of given or randomized size
        self.y = y or np.random.rand(self.size)  # vector of given or randomized size

        self.time = 0  # at the begining, the compilation time is zero

    # create the workload to be done to complete a task
    def work(self):
        start_time = time.perf_counter()  # save the starting time
        self.z = np.linalg.solve(self.x, self.y)  # the work part
        self.time = (
            time.perf_counter() - start_time
        )  # compute the time needed for the linalg solveer

    # create a doc with all needed info inside
    def to_json(self) -> str:
        info = {
            "id": self.id,
            "size": self.size,
            "x": self.x.tolist(),
            "y": self.y.tolist(),
            # "z": self.z.tolist(),
            "time": self.time,
        }
        return json.dumps(info)

    @classmethod
    def from_json(cls, text: str) -> "Task":
        info = json.loads(text)
        task = cls(id=info["id"], size=info["size"], x=info["x"], y=info["y"])
        # task.z = np.array(info["z"])
        task.time = info["time"]
        return task

    def __eq__(self, other: "Task") -> bool:
        if isinstance(other, Task):
            if np.array_equal(self.x, other.x) and np.array_equal(self.y, other.y):
                return True
            return False
