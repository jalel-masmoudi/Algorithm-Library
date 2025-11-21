# Algorithm Library 📚

A comprehensive, well-documented collection of **fundamental algorithms** and **data structures** implemented in **Python** and **C++**. This repository is designed for learning, reference, and interview preparation.

---

## 📋 Table of Contents

- [Sorting Algorithms](#sorting-algorithms)
- [Searching Algorithms](#searching-algorithms)
- [Graph Algorithms](#graph-algorithms)
- [Data Structures](#data-structures)
- [Dynamic Programming](#dynamic-programming)
- [Installation & Usage](#installation--usage)
- [Complexity Analysis](#complexity-analysis)

---

## 🔄 Sorting Algorithms

| Algorithm | Time (Avg) | Time (Worst) | Space | Stable | Implementation |
|-----------|-----------|-------------|-------|--------|-----------------|
| Bubble Sort | O(n²) | O(n²) | O(1) | ✅ | `sorting/bubble_sort.py` |
| Quick Sort | O(n log n) | O(n²) | O(log n) | ❌ | `sorting/quick_sort.cpp` |
| Merge Sort | O(n log n) | O(n log n) | O(n) | ✅ | `sorting/merge_sort.py` |
| Heap Sort | O(n log n) | O(n log n) | O(1) | ❌ | `sorting/heap_sort.cpp` |
| Insertion Sort | O(n) | O(n²) | O(1) | ✅ | `sorting/insertion_sort.py` |
| Selection Sort | O(n²) | O(n²) | O(1) | ❌ | `sorting/selection_sort.py` |

---

## 🔍 Searching Algorithms

### Linear Search
- **Time:** O(n)
- **Space:** O(1)
- **Use Case:** Unsorted arrays, small datasets
- **File:** `searching/linear_search.py`

### Binary Search
- **Time:** O(log n)
- **Space:** O(1)
- **Prerequisites:** Sorted array
- **File:** `searching/binary_search.cpp`

### Jump Search
- **Time:** O(√n)
- **Space:** O(1)
- **File:** `searching/jump_search.py`

---

## 🌐 Graph Algorithms

### Traversal
- **Breadth-First Search (BFS)** - O(V + E)
- **Depth-First Search (DFS)** - O(V + E)
- **Topological Sort** - O(V + E)

### Shortest Path
- **Dijkstra's Algorithm** - O((V + E) log V)
- **Bellman-Ford** - O(VE)
- **Floyd-Warshall** - O(V³)

### Minimum Spanning Tree
- **Kruskal's Algorithm** - O(E log E)
- **Prim's Algorithm** - O(V²)

### Implementation Files**
```
graphs/
├── bfs.py
├── dfs.cpp
├── dijkstra.py
├── bellman_ford.cpp
├── kruskal.py
└── prim.cpp
```

---

## 📦 Data Structures

### Basic Structures
- **Linked List** - O(n) search, O(1) insertion
- **Stack** - LIFO, O(1) push/pop
- **Queue** - FIFO, O(1) enqueue/dequeue

### Tree Structures
- **Binary Search Tree** - O(log n) average operations
- **AVL Tree** - Self-balancing, O(log n) guaranteed
- **Heap** - O(log n) insertion/deletion
- **Trie** - O(m) string operations (m = string length)

### Hash-Based
- **Hash Table** - O(1) average lookup
- **Hash Map** - Dynamic key-value storage

### Advanced
- **Graph** - Adjacency List/Matrix representation
- **Disjoint Set (Union-Find)** - O(α(n)) amortized

---

## ⚙️ Dynamic Programming

| Problem | DP State | Time | Space | File |
|---------|----------|------|-------|------|
| Fibonacci | fib[n] | O(n) | O(n) | `dp/fibonacci.py` |
| 0/1 Knapsack | dp[i][w] | O(nW) | O(nW) | `dp/knapsack.cpp` |
| Longest Common Subsequence | dp[i][j] | O(mn) | O(mn) | `dp/lcs.py` |
| Coin Change | dp[i] | O(n*amount) | O(amount) | `dp/coin_change.py` |
| Matrix Chain Mult. | dp[i][j] | O(n³) | O(n²) | `dp/matrix_chain.cpp` |
| Longest Increasing Subseq. | dp[i] | O(n²) | O(n) | `dp/lis.py` |

---

## 🚀 Installation & Usage

### Clone Repository
```bash
git clone https://github.com/jalel-masmoudi/algorithm-library.git
cd algorithm-library
```

### Python Examples
```bash
# Run a sorting algorithm
python3 sorting/quick_sort.py

# Run with test cases
python3 -m pytest sorting/test_sorts.py

# Profile performance
python3 benchmark/compare_sorts.py
```

### C++ Examples
```bash
# Compile
g++ -O2 -o binary_search searching/binary_search.cpp

# Run
./binary_search

# With optimization flags
g++ -O3 -std=c++17 -o dijkstra graphs/dijkstra.cpp
./dijkstra
```

---

## 📊 Complexity Analysis

Every implementation includes:

### Example: Quick Sort
```
Algorithm: Quick Sort
Time Complexity:
  - Best Case: O(n log n)
  - Average Case: O(n log n)
  - Worst Case: O(n²) - when pivot is always smallest/largest

Space Complexity: O(log n) - recursion depth

Advantages:
  ✓ In-place sorting (O(1) extra space)
  ✓ Fast in practice
  ✓ Good cache locality

Disadvantages:
  ✗ Not stable
  ✗ Worst case O(n²)
  ✗ Not adaptive
```

---

## 📚 Structure

```
algorithm-library/
├── sorting/
│   ├── bubble_sort.py
│   ├── quick_sort.cpp
│   ├── merge_sort.py
│   └── test_sorts.py
├── searching/
│   ├── binary_search.cpp
│   ├── linear_search.py
│   └── test_search.py
├── graphs/
│   ├── bfs.py
│   ├── dijkstra.cpp
│   └── graph_utils.py
├── data_structures/
│   ├── linked_list.py
│   ├── binary_tree.cpp
│   └── hash_table.py
├── dp/
│   ├── fibonacci.py
│   ├── knapsack.cpp
│   └── lcs.py
├── benchmark/
│   └── compare_sorts.py
├── tests/
│   └── test_all.py
└── README.md
```

---

## 🎯 Learning Path

**Beginner** → Start with:
1. Sorting algorithms (Bubble, Merge, Quick)
2. Binary search
3. Basic data structures (List, Stack, Queue)

**Intermediate** → Learn:
1. Graph algorithms (BFS, DFS)
2. Dynamic programming basics
3. Tree structures (BST, AVL)

**Advanced** → Master:
1. Complex graph algorithms
2. Advanced DP problems
3. Optimization techniques

---

## 💡 Key Concepts

### Big O Notation
- **O(1)** - Constant time (best)
- **O(log n)** - Logarithmic
- **O(n)** - Linear
- **O(n log n)** - Linearithmic (optimal for sorting)
- **O(n²)** - Quadratic
- **O(2ⁿ)** - Exponential
- **O(n!)** - Factorial (worst)

### Practical Tips
- ✅ Understand the problem before coding
- ✅ Analyze time & space complexity
- ✅ Consider edge cases
- ✅ Write clean, readable code
- ✅ Test thoroughly
- ✅ Optimize after correctness

---

## 🧪 Testing

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific test file
python3 -m pytest tests/test_sorts.py

# Generate coverage report
pytest --cov=. tests/
```

---

## 🤝 Contributing

Found a bug or want to add an algorithm? Contributions welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-algorithm`)
3. Add your algorithm with:
   - Correct implementation
   - Test cases
   - Complexity analysis
   - Documentation
4. Submit a pull request

---

## 📖 Resources

- **Books:** "Introduction to Algorithms" (CLRS)
- **Websites:** LeetCode, HackerRank, GeeksforGeeks
- **Visualizers:** VisuAlgo, Algorithm Visualizer
- **Practice:** Project Euler, CodeSignal

---

## 📝 License

MIT License - Feel free to use for learning and projects!

---

## 👤 Author

**Jalel Masmoudi**  
Computer Science Student | North American University of Sfax  
📧 Contact: m.j.masmoudi1@gmail.com

---

*Last Updated: November 2025*  
*⭐ If this helps you learn, please star the repository!*
