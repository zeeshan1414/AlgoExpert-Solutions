#include<iostream>
#include<vector>
using namespace std;

class node {
	public:
	int data;
	node* left;
	node* right;
	
	node(int d) {
		left = right = NULL;
		data = d;
	}
};

void print(node* root) {
	if(root==NULL)
		return;
	print(root->left);
	cout<<root->data<<" ";
	print(root->right);
}

void branchSum(node* root, int sum, vector<int> &v) {
	if(root == NULL)
		return;
	int runningSum = sum + root->data;
	
	if(root->left == NULL && root->left == NULL) {
		v.push_back(runningSum);
		return;
	}
	branchSum(root->left, runningSum, v);
	branchSum(root->right, runningSum, v);
}

int main() {
	node *root = new node(10);
	root->left = new node(8);  
    root->right = new node(2);  
    root->left->left = new node(3);  
    root->left->right = new node(5);  
    root->right->left = new node(2);
	print(root);
	cout<<endl;
	vector<int> res;
	branchSum(root, 0, res);
	// printing the sums of each branch
	for(int it: res) {
		cout<<it<<" ";
	}
	cout<<endl;
	return 0;
}