The implementation of the Huffmann Algorithm, has consisted as pseudo code tasks were resolved, in the construction of several classes, being:

1. Node
2. Queue
3. Tree
4. HuffmanEncoder

This has allowed to have a more encapsulated development, as well as, providing the project with a more consistent structure. The compresing algorithm has shown, for the tested example a reduction of almost 50% of its size.

In respects to the study of the time complexity, would be O(Ln), being L the maximum length of a codeword; If I had not used a built it function for sorting the input that takes O(n*log(n)); ending up the time complexity being O(n*log(n)). In respects to the space complexity, it is directly related to the size of the employed alphabet, in this case k, resulting in O(k).