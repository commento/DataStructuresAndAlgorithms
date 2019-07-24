#sqrt problem 1

the problem has been itially approached searching linearly throught all the number between 2 and the target number but it was O(n) linear complexity.
Then it was mplemented using a variation of binary search algorithm. This ensures the O(logn) time complexity.
The array parameter has been removed because there is no data structure but only a range on number (start_index and end_index have been kept as variable names even if they are not indexes but actual values). This allows an implementation with constant space complexity O(1).

In case the division operation (operation variable) does not fulfill the expected condition, the binary search continues evaluating the result of the operation.