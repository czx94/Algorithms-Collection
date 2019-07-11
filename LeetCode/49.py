class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        count_dic = {}
        for ch in strs:
            sort = str(sorted(ch))
            count_dic[sort] = count_dic.get(sort, []) + [ch]

        return list(count_dic.values())