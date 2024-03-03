import boss

if __name__ == "__main__":

    boss = boss.Boss()
    id = 0
    while id != 10:
        boss.sub_task(id, 900)
        id += 1
    boss.run()
