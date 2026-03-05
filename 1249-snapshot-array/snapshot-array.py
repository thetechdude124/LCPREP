class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        #the snap id refers to the status of each element given the snap id
        #as in, snapid starts at 0, not 1. 
        #so, we can set the elements with snapid (because we've implicitly)
        #made our self.snapid initialzation w.r.t. the future snap id!
        self.future_snapid = 0
        self.idx_hists = {}
        for i in range(length):
            self.idx_hists[i] = []
        
    def set(self, index: int, val: int) -> None:
        self.idx_hists[index].append((self.future_snapid, val))
        
    def snap(self) -> int:
        self.future_snapid += 1
        return self.future_snapid - 1

    #using later evalution to get the value of each index!
    def get(self, index: int, snap_id: int) -> int:
        idx_hists = self.idx_hists[index]
        #find the change at the snap id <= the requested one
        lo = 0
        hi = len(idx_hists) #that's the arr we're sampling from/against
        val = 0 #default value
        while lo < hi:
            mid = lo + (hi - lo)//2
            cand_id, cand_val = idx_hists[mid]
            if cand_id <= snap_id:
                val = cand_val
                lo = mid + 1
            else:
                hi = mid
        return val

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)