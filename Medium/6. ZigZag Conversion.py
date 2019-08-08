class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1): return s
        outer_list = []
        for rows in range(numRows): 
            outer_list.append([])
        
        def next_row(current_row, sign):
            if (current_row == 0):
                return 1, 1
            elif (current_row == numRows - 1):
                return current_row - 1, 0
            elif (sign == 1):
                return current_row + 1, 1
            elif (sign == 0):
                return current_row - 1, 0
        
        row, sign = 0, 1
        
        for each_character in s:
            outer_list[row].append(each_character)
            row, sign = next_row(row, sign)
        
        final_answer = ""
        
        for each_inner_list in outer_list:
            final_answer += "".join(each_inner_list)
        
        print(outer_list, final_answer)
        return final_answer