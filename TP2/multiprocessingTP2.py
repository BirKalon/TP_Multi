import multiprocessing as mp
import os
from multiprocessing import Pool, Process


# parallelize the exectution of the function
def f(x):
    return x * x


# running processus, called by start
def g(name):
    print("function g")
    print("hello", name)


# gets the id of process involved
def info(title):
    print(title)
    print("module name ", __name__)
    print("parent process  ", os.getppid())
    print("process id  ", os.getpid())


# how to start and analyze process w/ process safe queue
def foo(queue):
    queue.put("hello")


if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    info("main line")
    o = Process(target=g, args=("bob",))
    o.start()
    o.join()

    # used once
    ssm = mp.set_start_method("spawn")
    qssm = ssm.Queue()
    oossm = ssm.Process(target=foo, args=(qssm,))
    oossm.start()
    print(qssm.get())
    oossm.join()

    # use multiple start method -> best to avoid inference
    ctx = mp.get_context("spawn")
    qctx = ctx.Queue()
    ooctx = ctx.Process(target=foo, args=(qctx,))
    ooctx.start()
    print(qctx.get())
    ooctx.join()
