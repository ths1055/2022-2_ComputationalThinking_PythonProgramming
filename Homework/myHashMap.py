class Entry: 
    def __init__(self, k, v): 
        self._key =k
        self._value =v
    def __str__(self):
        return str(self._value)
def CyclicShiftHashCode(str_key):
    mask= (1 << 32)-1
    h=0
    for ch in str_key:
        h= (h <<5& mask) | (h >> 27)
        h += ord(ch)
    return h
class Bucket(Entry):
    def __init__(self): 
        self._bucket = []
    def _getitem(self, k): 
        count=0
        for item in self._bucket: 
            if k == item._key:
                return item._value
            count+=1
        return None
    def _setitem(self, k, v): 
        for item in self._bucket: 
            if k == item._key: 
                item._value = v
                return
        self._bucket.append(Entry(k, v))
    def _delitem(self, k): 
        for j in range(len(self._bucket)):
            if k == self._bucket[j]._key: 
                self._bucket.pop(j)
                return 1
        return None
    def __len__(self):
        return len(self._bucket) 
    def __iter__(self):
        for item in self._bucket: 
            yield item._key
class HashMap(Bucket): 
    def __init__(self, capacity=11, prm=109345121): 
        self._hash_tbl = capacity * [None] 
        self._hash_tbl_size = capacity 
        self._num_entry =0
        self._prime = prm 
    def _hash_value(self, k):
        return CyclicShiftHashCode(k) % self._prime % self._hash_tbl_size 
    def __len__(self):
        return self._num_entry 
    def _getitem(self, k):
        hv = self._hash_value(k)
        if hv is not None:
            print('key(%s) => hash_tbl[%d]'%(k,hv))
        bucket= self._hash_tbl[hv]
        return bucket._getitem(k)

    def _setitem(self, k, v): 
        hv = self._hash_value(k) 
        if self._hash_tbl[hv] is None: 
            self._hash_tbl[hv]= Bucket() 
        bucket = self._hash_tbl[hv] 
        bucket._setitem(k, v) 

    def _delitem(self, k): 
        hv = self._hash_value(k) 
        bucket= self._hash_tbl[hv] 
        bucket._delitem(k) 
        self._num_entry -=1
        
    def __str__(self): 
        s=''
        for h in range(len(self._hash_tbl)): 
            bucket= self._hash_tbl[h] 
            if bucket is not None:
                s += "bucket[{:2d}] : ".format(h) 
                for item in bucket:
                    s += str(item) + ", " 
                s += "\n "
        return s