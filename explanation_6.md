For the union and intersection problem, the approach has been to transform the linked lists, a format which is harder to work with, on something much simpler as is a list. Once the transformation has been done, the combination with the handy object sets, has done all the work.

In the study of the time complexity, we find that the transformation from linked list to list, takes O(n) time complexity, the the set function is in the same or less order of magnitude, as for the variations:

1. Union: we find the creation of the final array, again O(n), making n*O(n) be resulting to O(n)
2. Intersection: we find the creation of the final array, which is a double for-loop (operation x in s, acts with O(n)), resulting finally in O(n^n)

In respect to the space time complexity, we generate for both functions, 3 auxiliary lists, being O(3n); and resulting in O(n).