# sort012 problem4

The sorting as been implemented with a single traversal taking advantage of the absence of restriction in the size complexity.
The sorting infact is not in-place but uses a "result" list to store the sorted array.

The implementation was also possible using an in-place algorithm but for the sake of semplicity this solution has been adopted.

The sorting algorithm simply prepend zeros and append twos.
Additionally, it keeps an index for ones (that is incremented every time a new 0 is added) and insert them accordingly.

time complexity is O(n) and implementation is single-traversal.
space complexity is O(n) because for n element requires a list of the same size to store result. It can be optimized reusing the same list as result list but it requires additional logic and probably time complexity.

UPDATE: the algorithm has been updated as suggested in order not to use the list insertion operation (not allowed).