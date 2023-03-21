class UF():
    def __init__(self, n):
        self.n=n
        self.parents=[i for i in range(self.n)]
        self.sizes=[1 for i in range(self.n)]
    def find(self, i):
        checked=[i]
        root=i
        while self.parents[root]!=root:
            root=self.parents[root]
            checked.append(root)
        for node in checked:
            self.parents[node]=root
        return root
    def connect(self, i, j):
        root_i=self.find(i)
        root_j=self.find(j)
        if self.sizes[root_i]>=self.sizes[root_j]:
            self.parents[root_j]=root_i
            self.sizes[root_i]+=self.sizes[root_j]
        else:
            self.parents[root_i]=root_j
            self.sizes[root_j]+=self.sizes[root_i]
    def __str__(self):
        component_mapping={}
        reverse_component_mapping={}
        #components=set()
        for i in range(self.n):
            root_i=self.find(i)
            component_mapping[i]=root_i
            #components.add(root_i)
            if root_i not in reverse_component_mapping:
                reverse_component_mapping[root_i]=[i]
            else:
                reverse_component_mapping[root_i].append(i)
        rep=""
        for component,items in reverse_component_mapping.items():
            rep+=f"size = {self.sizes[component]}, members: {items}\n"
        return rep


#run via python -m doctest UF.py
def basic_test():
    """
    >>> tuf=UF(6)
    >>> print(tuf)
    size = 1, members: [0]
    size = 1, members: [1]
    size = 1, members: [2]
    size = 1, members: [3]
    size = 1, members: [4]
    size = 1, members: [5]
    <BLANKLINE>
    >>> tuf.connect(0,1)
    >>> tuf.connect(2,3)
    >>> tuf.connect(3,4)
    >>> tuf.connect(1,4)
    >>> print(tuf)
    size = 5, members: [0, 1, 2, 3, 4]
    size = 1, members: [5]
    <BLANKLINE>
    >>> print(tuf.find(4))
    2
    """
    pass
