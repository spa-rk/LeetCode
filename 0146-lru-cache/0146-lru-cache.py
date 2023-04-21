class LRUCache:

    def __init__(self, capacity: int):
        self.cp=capacity
        self.d=collections.OrderedDict()        

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        v=self.d.pop(key)
        self.d[key]=v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        else:
            if len(self.d)>=self.cp:
                self.d.popitem(last=False)
        self.d[key]=value
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)