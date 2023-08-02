#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

# @lc code=start
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        # Sort tasks based on enqueue times
        tasks = sorted([(start_time, task_dur, idx) for idx, (start_time, task_dur) in enumerate(tasks)], reverse=True)
        ret = []
        heap = []
        cur_time = 0
        while(tasks or heap):
            # If there are no queued tasks, move to the next arrival
            if not heap:
                cur_time = max(cur_time, tasks[-1][0])

            # Add all tasks that arrived at the same time
            while tasks and tasks[-1][0] <= cur_time:
                start_time, task_dur, idx = tasks.pop()

                heapq.heappush(heap, (task_dur, idx))

            next_task_dur, next_idx = heapq.heappop(heap)
            ret.append(next_idx)

            cur_time += next_task_dur

        return ret


# @lc code=end

