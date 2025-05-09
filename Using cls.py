class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

if __name__ == "__main__":
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    
    print(f"Number of Counter objects created: {Counter.get_count()}")
    
    c4 = Counter()
    print(f"Number of Counter objects created: {Counter.get_count()}") 