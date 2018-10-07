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
    vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if(!root)return {};
    queue<TreeNode*> q;
    q.push(root);

    while(q.empty() == false)
    {
        TreeNode *node = q.front();
        cout<<node->val;
        q.pop();
        if(node->left!=NULL){
            q.push(node->left);

        }
        if(node->right!=NULL){
            q.push(node->right);
        }
        
    }
        
        
        
        
        return result;
        
        
    }
};
