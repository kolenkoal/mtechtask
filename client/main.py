import os
import asyncio
import random
from fastapi import FastAPI
import aiohttp

app = FastAPI()

N = int(os.getenv("NUM_REQUESTS", 5))
M = int(os.getenv("MAX_DELAY", 1000))


async def send_requests():
    ip_address = "0.0.0.0"
    http_method = "POST"
    url = "http://web:8000/api/data/"
    uri = '/api/data'

    async with aiohttp.ClientSession() as session:
        for _ in range(N):
            http_response = random.randint(200, 500)

            async with session.post(url, json={
                "log": f"{ip_address} {http_method} {uri} {http_response}"}) as response:
                log_text = f"{ip_address} {http_method} {uri} {http_response}\n"

                # print(response)
                json_data = await response.json()

                print(json_data)

                with open("request_logs.txt", "a") as log_file:
                    log_file.write(log_text)

                await asyncio.sleep(random.uniform(0, M) / 1000)


@app.get("/simulate_requests/")
async def simulate_requests():
    tasks = [send_requests() for _ in range(N)]
    await asyncio.gather(*tasks)
    return {"message": f"{N} requests simulated"}
