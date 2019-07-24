# rotated array problem2

this implementation uses the binary search algorithm to keep the time complexity to O(logn)

two modified version of binary search are used:
- the first looks for the "pivot" (start index of the pre-rotation array) using the element at index 0 as the rotation check condition.
- the second looks for the element in the sorted array (rotated back)

The reverse rotation to the intitial array state is performed with constant time O(1) thanks to the "pivot" information.

Time complexity is for this reason O(2logn) which is equivalent to O(logn).

Concerning space complexity a copy of the list is used in order to perform the reverse rotation, so O(n).

UPDATE: I noticed that it was possible to reuse the same list and for this reason I updated the code in order to handle the problem without copying the data. This reduces the space complexity to O(1)

Also, from my understanding also the previous implementation was not introducing a copy because slicing only copy the reference and does not duplicate the object, reference: https://stackoverflow.com/questions/5131538/slicing-a-list-in-python-without-generating-a-copy