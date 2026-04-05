import asyncio
import httpx

URL = "http://127.0.0.1:8000/process/{}"

timeout = httpx.Timeout(15)  # increase timeout


async def send_request(n):
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get(URL.format(n))
        print(response.json())


async def main():
    tasks = [send_request(i) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
