# Task A: Computing 0+1
# Time: 0.0
# Task A: Computing 1+2
# Time: 1.0015077590942383
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.0019044876098633
# Task B: Computing 1+2
# Time: 3.0026352405548096
# Task B: Computing 3+3
# Time: 4.00391960144043
# Task B: Sum = 6

# Time: 5.00 sec


import asyncio
import time 

async def sleep():
    #  เวลาที่เริ่มต้นการทำงาน
    print(f'Time: {time.time() - start}')
    time.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#  สร้าง event loop ใน asyncio เพื่อทำให้สามารถเริ่มต้นการทำงานของ coroutine 
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1,2])),
    loop.create_task(sum("B", [1,2,3])),
]

loop.run_until_complete(asyncio.wait(tasks))
# ปิด event loop
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')
