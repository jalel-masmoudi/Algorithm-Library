#include <iostream>
#include <vector>
using namespace std;

/**
 * Binary Search Implementation
 * Time: O(log n)
 * Space: O(1) iterative, O(log n) recursive
 * Requires: Sorted array
 */

// Iterative approach
int binary_search_iterative(vector<int>& arr, int target) {
    int left =
