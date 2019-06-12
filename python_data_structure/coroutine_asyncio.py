#!/usr/bin/python3
# coding: utf-8


import asyncio
import time



async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"Started at {time.strftime('%X')}")
    
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"End as {time.strftime('%X')}")


async def main2():
    task1 = asyncio.create_task(say_after(1, "hello"))

    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"Started as {time.strftime('%X')}")

    await task1
    await task2

    print(f"End as {time.strftime('%X')}")


async def func1(future):
    await asyncio.sleep(1)
    future.set_result('Future is Donw')


def func1Main():
    loop = asyncio.get_evnet_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func1(future))
    print(loop.is_running())
    loop.run_until_complete(future)
    print(future.result())
    loop.close()


async def func2(future):
    await asyncio.sleep(1)
    future.set_result('Future is Done')


def call_result(future):
    print(future.result())
    loop.stop()


def func2Main():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(func2(future))
    future.add_done_callback(call_result)
    try:
        loop.run_forever()
    finally:
        loop.close()


if __name__ == "__main__":
    print("-" * 10, "Main1", "-" * 10)
    asyncio.run(main())
    
    print("-" * 10, "Main2", "-" * 10)
    asyncio.run(main2())

    print("-" * 10, "run_until_complete", "-" * 10)
    func1Main()

    print("-" * 10, "run_foever", "-" * 10)
    func2Main()

