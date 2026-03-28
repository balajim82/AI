"""
In this file discussing about asyncio patterns..

 Rule : Never use blocking operations in async code. Use async equivalents:
- time.sleep() → asyncio.sleep()
- requests.get() → aiohttp.ClientSession().get()
- open() → aiofiles.open()

 Common Pattern  - Run synchronous CPU/IO Bound task in separate thread, don't run in existing event loop thread

"""

# Basic Async Function Patterns

# Pattern 1: Simple Async Function
import asyncio


async def fetch_user(user_id: int) -> dict:
    """Simulate fetching user data"""
    await asyncio.sleep(2)  # Simulate I/O
    return {"id": user_id, "name": f"User {user_id}"}


async def main():
    user = await fetch_user(1)
    print(user)


asyncio.run(main())

# Pattern 2: Running Multiple Tasks Concurrently


async def main():
    # Create tasks for concurrent execution
    tasks = [
        asyncio.create_task(fetch_user(1)),
        asyncio.create_task(fetch_user(2)),
        asyncio.create_task(fetch_user(3)),
    ]

    # Wait for all tasks
    users = await asyncio.gather(*tasks)
    print(users)


asyncio.run(main())


# Pattern 3: Using asyncio.gather with Error Handling
async def fetch_with_error(user_id: int):
    if user_id == 2:
        raise ValueError(f"User {user_id} not found")
    await asyncio.sleep(0.5)
    return {"id": user_id, "name": f"User {user_id}"}


async def main():
    tasks = [fetch_with_error(i) for i in range(1, 4)]

    # return_exceptions=True prevents one error from stopping all tasks
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"User {i}: Error - {result}")
        else:
            print(f"User {i}: {result}")


asyncio.run(main())


# Working with Timeouts
async def slow_operation():
    await asyncio.sleep(5)
    return "Done"


async def main():
    try:
        # Timeout after 2 seconds
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")


asyncio.run(main())


# Common Pitfalls and Solutions
# Blocking the Event Loop
# ❌ WRONG - Blocks the event loop
import asyncio
import time


async def bad_sleep():
    time.sleep(1)  # Blocks entire event loop!
    return "Done"


# ✅ CORRECT - Non-blocking
async def good_sleep():
    await asyncio.sleep(1)  # Allows other tasks to run
    return "Done"


import asyncio
import time


async def fn1():
    print("inside function one, starting the job...")
    time.sleep(8)  # Blocks entire event loop!
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

# Method 1:  asyncio.to_thread() (Python 3.9+) -  Recommended
# Best for: I/O-bound tasks (file operations, API calls, database queries)

import asyncio
import time
import requests
from datetime import datetime

# ============ BLOCKING SYNC FUNCTIONS ============


def blocking_io_task(duration: int) -> str:
    """Simulates blocking I/O operation (file read, API call)"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting blocking I/O task...")
    time.sleep(duration)  # Simulates I/O operation
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Blocking I/O task completed")
    return f"I/O Result after {duration}s"


def fetch_from_api(url: str) -> dict:
    """Blocking HTTP request using requests library"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching {url}...")
    response = requests.get(url)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetch completed")
    return response.json()


def process_large_file(filepath: str) -> int:
    """Blocking file processing"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Processing file...")
    time.sleep(2)  # Simulates file processing
    print(f"[{datetime.now().strftime('%H:%M:%S')}] File processed")
    return 1000  # Number of records


# ============ RUN IN SEPARATE THREAD ============


async def main():
    print("=== Starting async operations ===\n")

    # Run blocking I/O task in separate thread
    result1 = await asyncio.to_thread(blocking_io_task, 3)
    print(f"Result: {result1}\n")

    # Run multiple blocking tasks concurrently in separate threads
    results = await asyncio.gather(
        asyncio.to_thread(blocking_io_task, 2),
        asyncio.to_thread(blocking_io_task, 3),
        asyncio.to_thread(fetch_from_api, "https://api.github.com/users/github"),
        asyncio.to_thread(process_large_file, "data.csv"),
    )

    print(f"\n=== All results ===")
    for i, result in enumerate(results, 1):
        print(f"Task {i}: {result}")


if __name__ == "__main__":
    asyncio.run(main())

# Method 2: loop.run_in_executor() with ThreadPoolExecutor

# Best for: When you need control over thread pool size
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def blocking_database_query(query: str, duration: int) -> dict:
    """Simulates blocking database operation"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Executing: {query}")
    time.sleep(duration)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Query completed")
    return {"rows": 100, "query": query}


def blocking_file_read(filename: str) -> str:
    """Simulates blocking file read"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Reading {filename}")
    time.sleep(1)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] File read completed")
    return f"Content of {filename}"


async def main():
    # Create thread pool with max 5 workers
    executor = ThreadPoolExecutor(max_workers=5)
    loop = asyncio.get_event_loop()

    # Run single blocking task
    result = await loop.run_in_executor(
        executor, blocking_database_query, "SELECT * FROM users", 2
    )
    print(f"Query result: {result}\n")

    # Run multiple blocking tasks concurrently
    tasks = [
        loop.run_in_executor(
            executor, blocking_database_query, "SELECT * FROM orders", 2
        ),
        loop.run_in_executor(
            executor, blocking_database_query, "SELECT * FROM products", 3
        ),
        loop.run_in_executor(executor, blocking_file_read, "config.json"),
        loop.run_in_executor(executor, blocking_file_read, "data.csv"),
    ]

    results = await asyncio.gather(*tasks)

    print("\n=== All Results ===")
    for result in results:
        print(result)

    # Cleanup
    executor.shutdown(wait=True)


if __name__ == "__main__":
    asyncio.run(main())
