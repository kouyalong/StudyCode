# coding: utf-8


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1  # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem

    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n // 2)):
        _siftup(x, i)


def heap_adjust(A, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    max_index = i
    if left < size and A[left] > A[max_index]:
        max_index = left
    if right < size and A[right] > A[max_index]:
        max_index = right
    if max_index != i:
        temp = A[i]
        A[i] = A[max_index]
        A[max_index] = temp
        heap_adjust(A, max_index, size)


l = [3, 4, 8, 10, 11, 6, 12]
heapify(l)
print(l)


def merge_cobain():
    pass


def merge_sort_cobain(array, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    merge_sort_cobain(array, left, mid)
    merge_sort_cobain(array, mid+1, right)
    merge_cobain(array, array[left:mid], array[mid+1:right])


def merge_sort_main(array):
    merge_sort_cobain(array, 0, len(array)-1)
