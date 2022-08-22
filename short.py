def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1.sort()
    nums2.sort()
    arr = []
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    for n in nums1:
        if n1 in nums2:
            arr.append(n)
            nums2.remove(n)
    return arr