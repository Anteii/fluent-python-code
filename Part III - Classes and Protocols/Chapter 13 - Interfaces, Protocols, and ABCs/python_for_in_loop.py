

class ConfusingSequence:
    
    data1 = ['a', 'b', 'c', 'd']
    data2 = ['1', '2', '3', '4']
    
    def __init__(self) -> None:
        self.cur_ind = 0
    
    def __getitem__(self, i):
        return self.data1[i]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_ind == len(self.data2):
            raise StopIteration()
        
        item = self.data2[self.cur_ind]
        self.cur_ind += 1
        
        return item

confusing_seq_obj = ConfusingSequence()

# __iter__ has priority over __getitem__
print(''.join(x for x in confusing_seq_obj))