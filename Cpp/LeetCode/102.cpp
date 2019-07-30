//
// Created by caizixiang on 2019-07-30.
//
#include <iostream>
#include <vector>
#include <queue>
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> order;
        if (!root)
            return order;

        queue<TreeNode*> current_layer;
        current_layer.push(root);

        while (!current_layer.empty())
        {
            vector<int> this_layer;
            queue<TreeNode*> next_layer;
            while (!current_layer.empty())
            {
                TreeNode* node = current_layer.front();
                current_layer.pop();
                this_layer.push_back(node->val);
                if (node->left)
                    next_layer.push(node->left);
                if (node->right)
                    next_layer.push(node->right);


            }

            order.push_back(this_layer);
            current_layer = next_layer;
        }

        return order;
    }
};