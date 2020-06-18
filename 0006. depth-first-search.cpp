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

void printVector(const vector<int> &vect) {
	for(int i: vect) {
		cout<<i<<" ";
	}
	cout<<endl;
}

int sumOfNodesAtMaxDepth(node* root, int sum) {
	if(root == NULL)
		return 0;
	if(root->left == NULL && root->right == NULL) {
		return root->data + sum;
	}
	return sumOfNodesAtMaxDepth(root->left, sum)+
	sumOfNodesAtMaxDepth(root->right, sum);
}

void DFS(node* root, vector<int> &res) {
	if(root == NULL)
		return;
	res.push_back(root->data);
	DFS(root->left, res);
	DFS(root->right, res);
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
	vector<int> res;
	DFS(root, res);
	printVector(res);
	return 0;
}