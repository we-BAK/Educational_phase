class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]           
        pre=self.getRow(rowIndex-1)
        row=[1]
        for i in range(len(pre)-1):
            row.append(pre[i]+pre[i+1])
        row.append(1)
        return row


      


        
        