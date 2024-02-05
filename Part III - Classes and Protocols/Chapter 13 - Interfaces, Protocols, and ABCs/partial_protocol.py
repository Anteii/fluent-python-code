import collections.abc

# NOTE: The whole example with testing classes with isinstance()
# against collections.abc.Sequence is an ERROR
# as there're several abc classes that can't be tested this way
# https://docs.python.org/3/library/collections.abc.html

class PartialSequence1:
    
    data = ['a', 'b', 'c', 'd']
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, i):
        return self.data[i]
    

class PartialSequence2:
    
    data = ['a', 'b', 'c', 'd']
    
    def __getitem__(self, i):
        return self.data[i]

class Iterator:
    
    data = ['a', 'b', 'c', 'd']
    cur_ind = 0
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_ind == len(self.data):
            raise StopIteration()
        
        item = self.data[self.cur_ind]
        self.cur_ind += 1
        
        return item
        
            
    
partial_seq_obj1 = PartialSequence1()
partial_seq_obj2 = PartialSequence2()
iterator_obj = Iterator()


print(f'Is `iterator_obj` an abc.Iterable: {isinstance(iterator_obj, collections.abc.Iterable)}') # __iter__
print(f'Is `iterator_obj` an abc.Iterator: {isinstance(iterator_obj, collections.abc.Iterator)}') # __iter__ __next___
print(f'Is `partial_seq_obj1` an abc.Sequence: {isinstance(partial_seq_obj1, collections.abc.Sequence)}')
print(f'Is `partial_seq_obj2` an abc.Sequence: {isinstance(partial_seq_obj2, collections.abc.Sequence)}')


print(''.join(x for x in partial_seq_obj1))
print(''.join(x for x in partial_seq_obj2))
print(''.join(x for x in iterator_obj))
