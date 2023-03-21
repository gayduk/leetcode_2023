class PriorityQueueWithChangeKey():
    def __init__(self, compfunc=lambda x,y: x>=y):
        self.compfunc=compfunc
        self.keys=[None]
        self.keyindex={}
        self.keypriority={}
        self.N=0
    
    
    def _swap(self, i, j):
        i_val_orig=self.keys[i]
        self.keys[i]=self.keys[j]
        self.keys[j]=i_val_orig
        self.keyindex[self.keys[i]]=i
        self.keyindex[self.keys[j]]=j
    
    
    def _priority(self, i):
        return self.keypriority[self.keys[i]]
    
    
    def _swim(self, i):
        while i//2>0 and not self.compfunc(self._priority(i//2),self._priority(i)):
            self._swap(i, i//2)
            i=i//2
            
    
    def _has_left_child(self, i):
        return 2 * i <= self.N and self.keys[2 * i] is not None
    
    
    def _has_right_child(self, i):
        return 2 * i + 1 <= self.N and self.keys[2 * i + 1] is not None
    
    
    def _sink(self, i):
        while self._has_left_child(i) or self._has_right_child(i):
            if self._has_left_child(i) and self._has_right_child(i):
                priority_root = self._priority(i)
                child_left = 2 * i
                child_right = 2 * i + 1
                priority_left = self._priority(child_left)
                priority_right = self._priority(child_right)
                
                if self.compfunc(priority_left, priority_right):
                    larger_child = child_left
                    priority_larger_child = priority_left
                else:
                    larger_child = child_right
                    priority_larger_child = priority_right
                
                if self.compfunc(priority_root, priority_larger_child):
                    break
                else:
                    self._swap(i, larger_child)
                    i = larger_child
                
            else:
                if self._has_left_child(i):
                    child = 2 * i
                else:
                    child = 2 * i + 1
                    
                priority_root = self._priority(i)
                priority_child = self._priority(child)
                
                if self.compfunc(priority_root, priority_child):
                    break
                else:
                    self._swap(i, child)
                    i = child
                

    def insert(self, key, priority):
        self.keys.append(key)
        self.N += 1
        self.keyindex[key] = self.N
        self.keypriority[key] = priority
        self._swim(self.N)
        
    
    def delete_top(self):
        top_key = self.keys[1]
        top_priority = self._priority(1)
        self._swap(1, self.N)
        self.keys.pop()
        self.N -= 1
        del self.keyindex[top_key]
        del self.keypriority[top_key]
        self._sink(1)
        return top_key, top_priority
    
    
    def change_key(self, key, new_priority):
        old_priority = self.keypriority[key]
        self.keypriority[key] = new_priority
        if self.compfunc(new_priority, old_priority):
            self._swim(self.keyindex[key])
        else:
            self._sink(self.keyindex[key])
            
    
    def __str__(self):
        rep = ""
        for i in range(1, self.N + 1):
            rep += str((i, self.keys[i], self._priority(i))) + "\n"
        return rep


def basic_test():
    """
    >>> MaxPQ=PriorityQueueWithChangeKey()
    >>> MaxPQ.insert("beta", 10.0)
    >>> MaxPQ.insert("gamma", 5.0)
    >>> MaxPQ.insert("delta", 4.0)
    >>> print(MaxPQ)
    (1, 'beta', 10.0)
    (2, 'gamma', 5.0)
    (3, 'delta', 4.0)
    <BLANKLINE>
    >>> MaxPQ.insert("eta", 6.0)
    >>> print(MaxPQ)
    (1, 'beta', 10.0)
    (2, 'eta', 6.0)
    (3, 'delta', 4.0)
    (4, 'gamma', 5.0)
    <BLANKLINE>
    >>> MaxPQ.insert("alpha", 100.0)
    >>> print(MaxPQ)
    (1, 'alpha', 100.0)
    (2, 'beta', 10.0)
    (3, 'delta', 4.0)
    (4, 'gamma', 5.0)
    (5, 'eta', 6.0)
    <BLANKLINE>
    >>> MaxPQ.insert("epsilon", 8.0)
    >>> print(MaxPQ)
    (1, 'alpha', 100.0)
    (2, 'beta', 10.0)
    (3, 'epsilon', 8.0)
    (4, 'gamma', 5.0)
    (5, 'eta', 6.0)
    (6, 'delta', 4.0)
    <BLANKLINE>
    >>> MaxPQ.change_key('eta', 200.0)
    >>> print(MaxPQ)
    (1, 'eta', 200.0)
    (2, 'alpha', 100.0)
    (3, 'epsilon', 8.0)
    (4, 'gamma', 5.0)
    (5, 'beta', 10.0)
    (6, 'delta', 4.0)
    <BLANKLINE>
    >>> MaxPQ.delete_top()
    ('eta', 200.0)

    >>> print(MaxPQ);
    (1, 'alpha', 100.0)
    (2, 'beta', 10.0)
    (3, 'epsilon', 8.0)
    (4, 'gamma', 5.0)
    (5, 'delta', 4.0)
    <BLANKLINE>
    """
    pass
