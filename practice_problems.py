"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    return len(product_ids) != len(set(product_ids))

#I choose to do a set because, sets dont store any duplicate items, so if we compare the initial input to the set, if it has the same items, they do not have duplicates however if it changes they have duplicates, the expected run time is super short

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear =  None
    
    def add_task(self, task):
        new_node = Node(task)
        if not self.rear:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_oldest_task(self):

        if not self.front:
            return None
        removed_task = self.front
        self.front = self.front.next
        if not self.front: 
            self.rear = None
        return removed_task.value
        
Taskqueue = TaskQueue() 
# I choose a Queue becuase we need to keep a list of the task in the order they are, so the keep the principle of FIFO first in first out, then I created a Node, and then we created the self.front and the self.rear to keep track of the first and the last item, in the add task we keep track of the back of the line. so if we add a task the rear changes to the next item i added, this haapens in the remove but in the opposite. the expected run time is short but if we include more items it will be more slow 
"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.items = set()

    def add(self, value):
        self.items.add(value)

    def get_unique_count(self):
        return len(self.items)

tracker = UniqueTracker()

#I choose a set cause i can store unique values, and then que created an add to add the values to the set and then when we want to return the unique count, we just len(self.items) to count how many they are. the expected run time is super short
