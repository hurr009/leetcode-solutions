class Solution:
    """ ZigZag Conversion """

    def convert(self, s: str, numRows: int) -> str:
        count = 0
        cols = 0

        if len(s) <= numRows or numRows == 1:
            return s
        
        while count < len(s): # Calculating Columns
            if cols%(numRows-1) == 0:
                count += numRows
            else:
                count += 1
            cols += 1

        rows = [[0]*cols for _ in range(numRows)]
        index = 0

        for j in range(cols): # parsing 2D list
            for i in range(numRows):
                if j % (numRows-1) == 0:
                    if index >= len(s):
                        break
                    print("j: ", j)
                    rows[i][j] = s[index]
                    print(s[index])
                    index += 1
                else:
                    rows[numRows-(j%(numRows-1))-1][j] = s[index]
                    print("j: ", j)
                    print(s[index])
                    index += 1
                    break
                    
        result = "" # converting to string format
        for i in rows:
            for j in i:
                if j != 0:
                    result += j
        return result
