class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hashmap = {}
        for c in tasks:
            # decrementing to make a max heap
            hashmap[c] = hashmap.get(c, 0) - 1
        
        time = 0 # idle time
        queue = [] # pair or [count, idleTime]
        tasks = [i for i in hashmap.values()]
        heapq.heapify(tasks)

        while tasks or queue:
            time += 1

            if tasks:
                # get task with max count
                count = heapq.heappop(tasks)
                # decrement count because we processed it(we wanted a max heap therefore count is negative therefore +1 instead of -1)
                count = count + 1

                # if count becomes 0 means the CHAR is finished, don't append to queue
                if count:
                    queue.append([count, time + n])

            # pick this entry if idle time reahced
            if queue and queue[0][1] == time:
                heapq.heappush(tasks, queue.pop(0)[0])

        return time
