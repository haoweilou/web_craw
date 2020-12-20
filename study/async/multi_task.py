import asyncio
import time
async def request(url):
    print("url is: "+url)
    #time.sleep(2)
    await asyncio.sleep(2)
    return "finish"

if __name__ == '__main__':
    start = time.time()
    urls = ["baidu.com",
            "sogo.com",
            "douban.com"
    ]
    task_list = []
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        task_list.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    end = time.time()
    print(end-start)
    