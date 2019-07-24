#rearrange digits problem3

this problem has been solved adopting the quicksort algorithm.
This ensures the time complexity at O(nlogn).

First the array is sorted using the quicksort.
After, the algorithm is traversed once from end to start to take alternatively the highest values and append them to the two result strings that are then returned, converted to int.

Time complexity is for this reason O(n(1+logn)) approximated to O(nlogn). 
Space complexity is from my analysis is O(n) because two new strings are used to store the result, each of them has size n/2 circa.