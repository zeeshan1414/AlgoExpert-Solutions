#include<bits/stdc++.h>
// #include<iostream>
// #include<vector>
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

int sumOfAllBranches(node* root, int sum) {
	if(root == NULL)
		return 0;
	return root->data + sumOfAllBranches(root->left, sum) + sumOfAllBranches(root->right, sum);
}

int sumOfdepth(node* root, int sum) {
	if(root == NULL)
		return 0;
	return sum + sumOfdepth(root->left, sum+1) + sumOfdepth(root->right, sum+1);
}

int main() {
	node *root = new node(1);
	root->left = new node(2);  
    root->right = new node(3);  
    root->left->left = new node(4);  
    root->left->right = new node(5);
	root->right->left = new node(6);
    root->right->right = new node(7);
	root->left->left->left = new node(8);
	root->left->left->right = new node(9);
	print(root);
	cout<<endl;
	cout<<sumOfdepth(root, 0);
	cout<<endl;
	return 0;
}