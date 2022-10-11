class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

    def print_queue(self):
        for i in self.queue:
            print(i)

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in queue"


new_queue = Queue()
new_queue.add("Mon")
new_queue.add("Tue")
new_queue.add("Wed")
new_queue.remove()
new_queue.print_queue()