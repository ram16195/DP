/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* r) {
        if (!r) return;
        flatten(r->left);      // flatten left subtree
        auto R = r->right;
        r->right = r->left;   // modify to set flattened left subtree as right subtree
        r->left = NULL;     // remove left subtree
        auto cur = r;
        while (cur->right) cur = cur->right; // find rightmost node after flatten
        flatten(R);                         // flatten right subtree
        cur->right = R;                // append flattened right subtree to rightmost node
    }

};
