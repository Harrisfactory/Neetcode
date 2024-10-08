class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key in self.hashset:
            return
        self.hashset.append(key)

    def remove(self, key: int) -> None:
        ctr = len(self.hashset) - 1
        while ctr >= 0:
            if self.hashset[ctr] == key:
                self.hashset.pop(ctr)
                return
            ctr-=1


    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
