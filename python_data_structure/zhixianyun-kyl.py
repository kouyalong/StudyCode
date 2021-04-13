# -*- coding: utf-8 -*-

from typing import List


def equality_distribution(
        assembly_lines: List[int], month: int) -> int:
    """
    第一题：优化生产线产量
    :param assembly_lines: 流水线产量
    :param month: 优化月份
    :return: 优化
    """
    max_index = 0

    # 找到产量最大的
    n = len(assembly_lines)
    for i in range(1, n):
        if assembly_lines[max_index] < assembly_lines[i]:
            max_index = i

    for _ in range(month):
        # 产量最大的生产线减去 n-1 产量
        assembly_lines[max_index] -= (n - 1)
        new_max_index = 0
        for i in range(n):
            if max_index != i:
                # 其他生产线 产量各+1
                assembly_lines[i] += 1
            # 在变更后的产量里面找最大的 生产线
            # 如果最大产量有相同的生产线，取index靠前的
            if assembly_lines[i] > assembly_lines[new_max_index]:
                new_max_index = i
        max_index = new_max_index
    return assembly_lines


def find_gt_first(array: List[int]) -> dict:
    """
    从数组每位元素当前位置开始，往后找到⼤于⾃⼰本身的第⼀位元素，并返回
    如果没有找到，返回-1
    :param array: 数组
    :return: 每个index位置的元素 在其后面第一个大于自己本身的元素的index
    """
    stack = []
    n = len(array)
    result = dict()
    for i in range(n):
        item = array[i]
        if not stack:
            stack.append(i)
        else:
            # 如果当前元素 比前面的大，得到前面元素的第一个大于它本身的元素位置
            # 已经知道结果的元素从栈中推出
            while stack and item > array[stack[-1]]:
                result[stack[-1]] = i
                stack.pop()
            stack.append(i)
    # 剩余在栈中的所有元素 都没有比其更大的元素，结果都为-1
    while stack:
        result[stack.pop()] = -1
    return result


def loop_long_string(string: str) -> int:
    """
    :param string: 12字符串
    :return: 最长12连续串的 长度
    """
    if not string:
        return 0

    # 考虑到首位可以12或者21连续的情况，分隔字符串使得最前面和最后面两个字符都一致
    # 从前往后遍历，找到第一处连续的字符相同的位置，切断拼接到最后面
    new_string = ""
    n = len(string)
    for i in range(n-1):
        if string[i] == string[i+1]:
            new_string = string[i+1:]+string[:i+1]
            break
    if not new_string:
        new_string = string

    # 使用滑动窗口，找到最长的12连续串
    i, j, max_loop = 0, 1, 0
    while j < n:
        if new_string[j-1] != new_string[j]:
            max_loop = max(max_loop, j-i)
        else:
            i = j
        j += 1

    # 全为1 或者全为2的串  12串的长度为0
    return max_loop + 1 if max_loop else 0


# 第四题
class Solution4:
    """第四题"""

    def __init__(self):
        self.max_sum_gap = 0

    def sum_gap(self, array):
        gap = 0
        pre = 0
        for i in range(1, len(array)):
            gap += abs(array[pre] - array[i])
            pre += 1
        return gap

    def model_sort(self, array1: List[int], array2: List[int], new_array, current_index=0):
        """
        :param array1: 第一个数组，确定的顺序
        :param array2: 第二个数组，待排序
        :return: 使用回溯法，找到所有按照第一个顺序排序的第二个数组，然后求最大的间距和
        """
        if current_index == len(array2):
            new_gap = self.sum_gap(new_array)
            self.max_sum_gap = self.max_sum_gap \
                if self.max_sum_gap > new_gap else new_gap
            return
        for row in range(len(array2)):
            if current_index < len(array2):
                new_array[current_index], flag = array2[row], True

                if array2[row] in new_array[:current_index]:
                    flag = False

                if current_index > 0 and flag:
                    pf = array1[current_index-1] - array1[current_index]
                    npf = new_array[current_index-1]-new_array[current_index]
                    if pf * npf < 0:
                        flag = False
                if flag:
                    self.model_sort(array1, array2, new_array, current_index+1)


if __name__ == "__main__":
    # al = [10, 7, 5, 4]
    # print(equality_distribution(al, 12))
    # al = [15, 2, 8, 13, 16, 1, 0, 20]
    # print(find_gt_first(al))
    # sl = "12221212"
    # print(loop_long_string(sl))

    import time
    start_time = time.time()
    q = Solution4()
    a1 = [1, 4, 3, 7, 2, 8, 5, 10, 9, 6, 11, 12]
    a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    na = [0] * len(a1)
    q.model_sort(a1, a2, na)
    print(q.max_sum_gap)
    print(time.time() - start_time)
