'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from queue_arr import Queue

# def sliding_window_max(nums, k):
#     # Your code here
#     max_values = []

#     n = 0

#     if len(nums) <= k:
#         return max(nums)

#     while n <= len(nums) - k:
#         window = nums[n:k + n]
#         n += 1
#         max_values.append(sliding_window_max(window,k))

#     return max_values

def sliding_window_max(nums, k):
    max_vals = []
    q = Queue()
    # remove all elems from a queue

    for i, n in enumerate(nums):
        while len(q) > 0 and n > q[-1]:
            q.pop()

        q.append(n)

        # calc the window range
        window_range = i - k + 1

        # as long as our window range == k, then we will add elements to the queue
        if window_range >=0:
            # add the max elem (in this case 1st in the queue) to the max_vals
            max_vals.append(q[0])

            # check num on the left needs to be evicted
            # if so take it out of the start of the queue
            if nums[window_range] == q[0]:
                q.popleft()

        return max_vals

# Naive pass
    # max_vals = [0 for _ in range(len(nums) - k + 1)]

    # for i in range(len(nums)):
    #     current_elem = nums[i]

    #     for j in range(1, k):
    #         if nums[i + j] > current_elem:
    #             current_elem = nums[i + j]

    #     max_vals[i] = current_elem

    # return max_vals


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
