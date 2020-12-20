import requests
import asyncio
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

async def request(url):
    print(url)
    return "finish"

def callback(task):
    print(task.result())

if __name__ == "__main__":
    a = request("www.baidu.com")
    '''event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(a)'''
    '''
    loop = asyncio.get_event_loop()
    task = loop.create_task(a)
    print(task)
    loop.run_until_complete(task)
    print(task)
    '''
    '''
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(a)
    print(task)
    loop.run_until_complete(task)
    print(task)
    '''
    loop = asyncio.get_event_loop()
    task = loop.create_task(a)
    task.add_done_callback(callback)
    loop.run_until_complete(task)