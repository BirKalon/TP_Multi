import task

if __name__ == "__main__":

    a = task.Task(id="42")
    txta = a.to_json()

    b = task.Task.from_json(txta)

    print(a == b)
