class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # new_position = {}

        # for i in range(len(position)):
        #     new_position[position[i]] = speed[i] + new_position.get(position[i], 0)

        # new_position = {key: new_position[key] for key in sorted(new_position.keys())}

        # position = list(new_position.keys())
        # speed = list(new_position.values())
        # stack = []
        
        # for i in range(len(position) -1, -1, -1):
        #     time = (target - position[i]) / speed[i]
            
        #     if not stack or time > stack[-1]:
        #         stack.append(time)

        # return len(stack)

        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(pair)[::-1]:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

        