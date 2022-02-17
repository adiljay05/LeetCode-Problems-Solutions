class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        return self.findsum(candidates,target,[],[])
                
    def findsum(self,arr,target,res,path):
        if target==0:
            res.append(path)
            return
        if target<0: return
        
        for i in range(len(arr)):
            rem=target-arr[i]
            self.findsum(arr[i:],rem,res,path+[arr[i]])
            
        return res