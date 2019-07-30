//
// Created by caizixiang on 2019-07-29.
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> order;
        if (!root)
            return order;

        int flag = 1;
        stack<TreeNode*> current_layer;
        current_layer.push(root);

        while (!current_layer.empty())
        {
            vector<int> this_layer;
            stack<TreeNode*> next_layer;
            while (!current_layer.empty())
            {
                TreeNode* node = current_layer.top();
                current_layer.pop();
                this_layer.push_back(node->val);
                if (flag)
                {
                    if (node->left)
                        next_layer.push(node->left);
                    if (node->right)
                        next_layer.push(node->right);
                } else
                {
                    if (node->right)
                        next_layer.push(node->right);
                    if (node->left)
                        next_layer.push(node->left);
                }

            }

            order.push_back(this_layer);
            current_layer = next_layer;
            flag = 1 - flag;
        }

        return order;
    }
};