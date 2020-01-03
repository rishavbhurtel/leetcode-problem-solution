class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         strings = []
#         string_without_duplicates = []
    
#         for char in s:
#             strings.append(char)
        
#         for i in range(len(strings)):
#             for j in range(i+2,len(strings)+1):
#                     string_without_duplicates.append(strings[i:j])
    
#         for i in range(len(string_without_duplicates)):
#             string_without_duplicates[i] = list(dict.fromkeys(string_without_duplicates[i]))
    
#         #print(string_without_duplicates)
#         return max(map(len,string_without_duplicates))
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength