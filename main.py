# quick search for item in sorted list
def count_item(arr, item, start):
        c = 0
        for i in range(start, len(arr)):
            if item < arr[i]:
                break
            if item == arr[i]:
                c += 1
        return (c, i)

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    d = {}
    arr = []
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    items = sorted(set(nums1))
    i, j = 0, 0
    for item in items:
        if item in nums2:
            count1, i = count_item(nums1, item, i)
            count2, j = count_item(nums2, item, j)
            d[item] = min(count1, count2)
    for key in d.keys():
        arr.extend([key] * d[key])

    return arr