"""
Why Async Programming Matters
The Problem with Synchronous Code - In traditional synchronous programming, when you make an I/O operation (API call, database query, file read), your thread blocks and waits:

Importent Methods

async def methodname()
await
asyncio.sleep()
asyncio.gather()
asyncio.run()
asyncio.create_task()

"""

# Synchronous Program (The below code explain sync program treats)
import time


def fn1():
    print("inside function one, starting the job...")
    time.sleep(2)  # assume some I/O Job
    print("inside function one, job is done...")


def fn2():
    print("inside function two, starting the job...")
    time.sleep(3)  # assume some I/O Job
    print("inside function two, job is done...")


def fn3():
    print("inside function Three, starting the job...")
    time.sleep(3)  # assume some I/O Job
    print("inside function Three, job is done...")


# calling function in synchronous ways from main function

if __name__ == "__main__":
    fn1()
    fn2()
    fn3()

# asyncio ( The above program how to run in async)
import asyncio
import time


async def fn1():
    print("inside function one, starting the job...")
    await asyncio.sleep(8)  # assume some I/O Job
    print("inside function one, job is done...")
    return "Result from fn1"


async def fn2():
    print("inside function two, starting the job...")
    await asyncio.sleep(5)  # assume some I/O Job
    print("inside function two, job is done...")
    return "Result from fn2"


async def fn3():
    print("inside function Three, starting the job...")
    await asyncio.sleep(3)  # assume some I/O Job
    print("inside function Three, job is done...")
    return "Result from fn3"


async def run_concurrent():
    print("\n=== Running CONCURRENTLY ===")
    start = time.time()

    # All three functions run at the same time
    results = await asyncio.gather(fn1(), fn2(), fn3())

    elapsed = time.time() - start
    print(f"\n✓ All jobs completed in {elapsed:.2f} seconds")
    print(f"Results: {results}")
    return results


if __name__ == "__main__":
    asyncio.run(run_concurrent())


# Core Concepts
# Coroutines - A coroutine is a function that can pause and resume execution. Defined with async def:
async def my_coroutine():
    print("Starting")
    await asyncio.sleep(1)  # Pause here, let other tasks run
    print("Finished")
    return "Result"


# Calling a coroutine returns a coroutine object, doesn't execute it
coro = my_coroutine()  # <coroutine object>

# To execute, you need to await it or run it in an event loop
# result = await my_coroutine()  # Inside another async function
# OR
if __name__ == "__main__":
    asyncio.run(my_coroutine())  # Entry point


# Event Loop
import asyncio


async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


# Method 1: High-level API (recommended)
asyncio.run(say_hello())

# Method 2: Low-level API (for advanced use)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(say_hello())
finally:
    loop.close()


# Tasks - Tasks wrap coroutines and schedule them for execution:


async def count(name, n):
    for i in range(n):
        print(f"{name}: {i}")
        await asyncio.sleep(0.1)


async def main():
    # Create tasks - they start running immediately
    task1 = asyncio.create_task(count("A", 3))
    task2 = asyncio.create_task(count("B", 3))

    # Wait for both to complete
    await task1
    await task2

    # Or use gather to wait for multiple tasks
    # await asyncio.gather(task1, task2)


asyncio.run(main())
