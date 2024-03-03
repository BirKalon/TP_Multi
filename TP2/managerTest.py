import multiprocessing as mp

import manager

KEY = b"Ash_nazg_durbatuluk_ash_nazg_gimbatul_ash_nazg_thrakatuluk_agh_burzum_ishi_krimpatul"

PORT = 3000

if __name__ == "__main__":

    # manager test

    taskQueue = mp.Queue()
    resultQueue = mp.Queue()

    manager.QueueManager.register("get_tasks", callable=lambda: taskQueue)
    print("isHere managerTest1")
    manager.QueueManager.register("get_results", callable=lambda: resultQueue)
    print("isHere managerTest2")

    try:
        manager.QueueManager(
            address=("", PORT), authkey=KEY
        ).get_server().serve_forever()
        print("isHere managerTest3")
    finally:
        print()
        print(
            f"Exiting w/ about {taskQueue.qsize()} task in queue"
            f" and {resultQueue.qsize()} results"
        )
