//
// Created by caizixiang on 2019-07-30.
//

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root)
            return true;
        else
            return dfs(root->left, root->right);
    }

    bool dfs(TreeNode* node1, TreeNode* node2)
    {
        if (!node1 && !node2)
            return true;
        else if (node1 && node2)
        {
            if (node1->val != node2->val)
                return false;
            else
            {
                return dfs(node1->left, node2->right) && dfs(node1->right, node2->left);
            }
        }
        else
            return false;
    }
};