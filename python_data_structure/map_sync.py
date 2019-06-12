#!/usr/bin/python
# coding: utf-8

import time
import asyncio
from threading import Thread

now = lambda :time.time()


async def do_some_work(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


def callback(future):
    print("CallBack:", future.result())


def callback2(t, future):
    print("CallBack2:", t, future.result())


def first_async():
    coroutine = do_some_work(3)

    start = now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)

    print("TIME:", now() - start)


def second_async():
    coroutine = do_some_work(3)

    start = now()
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)
    print(task, "exec before")
    loop.run_until_complete(task)
    print(task, "exec after")
    print("TIME:", now() - start)


def third_async():
    coroutine = do_some_work(3)

    start = now()
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    print(task, "1" * 8)
    task.add_done_callback(callback)
    print(task, "2" * 8)
    loop.run_until_complete(task)
    print(task, "3" * 8)
    print("Task ret:", task.result())
    print("TIME:", now() - start)


def four_async():
    start = now()
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(3)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print("Task ret:", task.result())
    print("TIME:", now() - start)


def five_async():

    async def main():
        coroutine1 = do_some_work(1)
        coroutine2 = do_some_work(2)
        coroutine3 = do_some_work(3)

        tasks = [
            asyncio.ensure_future(coroutine1),
            asyncio.ensure_future(coroutine2),
            asyncio.ensure_future(coroutine3),
        ]

        results = await asyncio.gather(*tasks)

        for result in results:
            print("Task ret:", result)

    start = now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('TIME: ', now() - start)


def six_async():

    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(3)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    start = now()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as err:
        print(asyncio.Task.all_tasks())
        print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
    print('TIME: ', now() - start)



def seven_async():

    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def do_more_work(x):
        print("More Work {}", x)
        await asyncio.sleep(x)
        print("Finished Work {}", x)

    def more_work(x):
        print("More Work {}", x)
        time.sleep(x)
        print("Finished Work {}", x)

    def more_main():
        start = now()
        new_loop = asyncio.new_event_loop()
        t = Thread(target=start_loop, args=(new_loop, ))
        t.start()
        print(t)
        print('TIME start: {}'.format(now() - start))
        h1 = new_loop.call_soon_threadsafe(more_work, 6)
        print(h1, id(h1))
        h2 = new_loop.call_soon_threadsafe(more_work, 3)
        print(h2, id(h2))
        new_loop.stop()
        print('TIME end: {}'.format(now() - start))


    def do_more_main():
        start = now()
        new_loop = asyncio.new_event_loop()
        t = Thread(target=start_loop, args=(new_loop, ))
        t.start()
        print(t)
        h3 = asyncio.run_coroutine_threadsafe(do_more_work(6), new_loop)
        print(h3, id(h3))
        h4 = asyncio.run_coroutine_threadsafe(do_more_work(3), new_loop)
        print(h4, id(h4))
        loop = asyncio.get_event_loop()
        loop.stop()
        print('TIME end: {}'.format(now() - start))

    # more_main()
    do_more_main()


def eight_async():
    pass


seven_async()
