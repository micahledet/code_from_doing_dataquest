## 2. Using Mutable Values for Changing Information ##

class Counter():
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000):
        counter.increment()
class Counter():
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count
    
def count_up_100000(counter):
    for i in range(100000):
        counter.increment()

counter = Counter()
initial_count = counter.get_count()
count_up_100000(counter)
final_count = counter.get_count()