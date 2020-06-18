// https://practice.geeksforgeeks.org/problems/find-the-closest-element-in-bst/1

/*The Node structure is

struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/

// Return the minimum absolute difference between any tree node and the integer K
int minDiff(Node *root, int K)
{
    //Your code here
    int closest = INT_MAX;
    Node* temp = root;
    while(temp != NULL) {
        int i = abs(temp->data - K);
        if(i<abs(K-closest)) {
            closest = temp->data;
        }
        if(closest == K) {
            return 0;
        } else if(K>temp->data) {
            temp = temp->right;
        } else if(K<temp->data) {
            temp = temp->left;
        }
    }
    return abs(closest-K);
}
