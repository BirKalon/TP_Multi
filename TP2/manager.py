import os
from multiprocessing.managers import BaseManager as bm

KEY = "Ash_nazg_durbatulûk_ash_nazg_gimbatul_ash_nazg_thrakatulûk_agh_burzum_ishi_krimpatul"
PORT = 3000


# class of simple managers holding a queue
class QueueManager(bm):
    pass


# class for the client queue
class QueueClient:

    # initialisation of the management by the manager
    def __init__(self):
        QueueManager.register("getTasks")
        QueueManager.register("getResults")
        manager = QueueManager(
            address=(os.environ.get("MANAGER_HOST", "localhost"), PORT), authkey=KEY
        )
        manager.connect()
        self.tasks = manager.get_tasks()
        self.results = manager.get_results()
