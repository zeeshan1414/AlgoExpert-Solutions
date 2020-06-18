// https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
#include<iostream>
#include<map>
#include <algorithm>
using namespace std;

bool isPair(int arr[], int n, int x) {
    for(int i=0; i<n-1; i++) {
        for(int j=i+1; j<n; j++) {
            if(arr[i]+arr[j] == x) {
                return true;
            }
        }
    }
    return false;
}

bool isPairHashMap(int arr[], int n, int target) {
    unordered_map<int, bool> umap;
    for(int i=0; i<n; i++) {
        int x = arr[i];
        int y = target - x;
        if(umap.count(y)) {
            return true;
        } else {
            umap[x] = true;
        }
    }
    return false;
}

bool isPairSorting(int arr[], int n, int x) {
    sort(arr, arr+n);
    int i=0, j=n-1;
    while(i<j) {
        int sum = arr[i]+arr[j];
        if(sum == x) {
            return true;  
        } else if(sum<x) {
            i++;
        } else {
            j--;
        }
    }
    return false;
}

int main()
 {
	//code
	int t;
	cin>>t;
	while(t--) {
	int n;
	cin>>n;
	int x;
	cin>>x;
	int arr[n];
	for(int i=0; i<n; i++) {
	    cin>>arr[i];
	}
	if(isPairSorting(arr, n, x))
	cout<<"Yes"<<endl;
	else
	cout<<"No"<<endl;
	}
	return 0;
}