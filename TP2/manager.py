import os
from multiprocessing.managers import BaseManager as bm

KEY = b"Ash_nazg_durbatuluk_ash_nazg_gimbatul_ash_nazg_thrakatuluk_agh_burzum_ishi_krimpatul"

PORT = 3000


# class of simple managers holding a queue
class QueueManager(bm):
    print("is here managerManagerInit0")
    pass


# class for the client queue
class QueueClient:

    # initialisation of the management by the manager
    def __init__(self):
        QueueManager.register("get_tasks")
        QueueManager.register("get_results")
        print("is here managerClientInit1")
        manager = QueueManager(
            address=(os.environ.get("MANAGER_HOST", "localhost"), PORT), authkey=KEY
        )
        print("is here managerClientInit2")
        manager.connect()
        print("is here managerClientInit3")
        self.tasks = manager.get_tasks()
        self.results = manager.get_results()
        print("is here managerClientInit4")
