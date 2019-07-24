# max min in unordered random list problem6

The solution is a single-traversal of the list. The max and min variables are initially both assigned to the first element of the list in order to have a starting point for the comparisons.

Each element is then compared in order to find out if there is a new relative max and min. Finally, the absolute max and min are found.

Time complexity is O(n) with a single-traversal.
Space complexity is O(1), only two ints are used to store max and min but they are indipendent from the size of the number list.