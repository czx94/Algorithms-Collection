class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        count_dict = {}

        index_sum = len(list1) + len(list2)
        chosen_res = []
        for i in range(len(list1)):
            res = list1[i]
            count_dict[res] = i

        i = 0
        while i < len(list2):
            res = list2[i]
            if res in count_dict:
                current_sum = count_dict[res] + i
                if current_sum < index_sum:
                    chosen_res = [res]
                    index_sum = current_sum
                elif current_sum == index_sum:
                    chosen_res.append(res)

            i += 1

        return chosen_res

