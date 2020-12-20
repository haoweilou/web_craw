import asyncio
import time
import aiohttp

async def request(url):
    print("downloading: "+url)
    #time.sleep(2)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            page_text = await response.text()
            #byte = response.read()
    print("finish: "+url)
    return page_text

if __name__ == '__main__':
    start = time.time()
    urls = ["https://www.baidu.com",
            "https://www.sogo.com",
            "https://www.douban.com"
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
    