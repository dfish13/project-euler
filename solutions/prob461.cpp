#include <iostream>
#include <limits>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <random>
#include <cmath>

using namespace std;

typedef struct Node * nptr;

struct Node
{
	double key;
	pair<int, int> val;
	int height;
	nptr left, right;
	Node(double k, pair<int, int> v = make_pair(0, 0), int h = 0, nptr l = nullptr, nptr r = nullptr) : key(k), val(v), height(h), left(l), right(r) {};
};

class BST
{
	public:
	BST()
	{
		root = nullptr;
	}

	BST(double key)
	{
		root = new struct Node(key);
	}

	void insert(double key, const pair<int, int> & val = make_pair(0, 0))
	{
		insert(key, val, root);
	}

	nptr find(double key);

	nptr findClosest(double key)
	{
		closest = root;
		minDif = numeric_limits<double>::max();

		findClosest(root, key);

		return closest;
	}

	nptr root, closest;
	double minDif;
	int start;

	void print()
	{
		start = 1;
		print(root);
		cout << '\n';
	}

	private:


	void insert(const double & key, const pair<int, int> & val, nptr & n)
	{
		if (n == nullptr)
			n = new struct Node(key, val);
		else if (key < n->key)
			insert(key, val, n->left);
		else if (key > n->key)
			insert(key, val, n->right);

		balance(n);
	}

	void balance(nptr & n)
	{
		int hl = height(n->left), hr = height(n->right);
		if (!n)
			return;
		if (hl - hr > 1)
			if (height(n->left->left) >= height(n->left->right))
				rotateWithLeftChild(n);
			else
				doubleWithLeftChild(n);
		else if (hr - hl > 1)
			if (height(n->right->right) >= height(n->right->left))
				rotateWithRightChild(n);
			else
				doubleWithRightChild(n);

		n->height = (hl > hr ? hl : hr) + 1;		
	}

	void rotateWithLeftChild(nptr & k2)
	{
		nptr k1 = k2->left;
		k2->left = k1->right;
		k1->right = k2;
		k2->height = max(height(k2->left), height(k2->right)) + 1;
		k1->height = max(height(k1->left), k2->height) + 1;
		k2 = k1;
	}

	void doubleWithLeftChild(nptr & k3)
	{
		rotateWithRightChild(k3->left);
		rotateWithLeftChild(k3);
	}

	void rotateWithRightChild(nptr & k2)
	{
		nptr k1 = k2->right;
		k2->right = k1->left;
		k1->left = k2;
		k2->height = max(height(k2->left), height(k2->right)) + 1;
		k1->height = max(height(k1->right), k2->height) + 1;
		k2 = k1;
	}

	void doubleWithRightChild(nptr & k3)
	{
		rotateWithLeftChild(k3->right);
		rotateWithRightChild(k3);
	}

	int height(nptr n) const
	{
		return !n ? -1 : n->height;
	}

	void print(nptr n)
	{
		if (n)
		{
			print(n->left);
			if (!start)
				cout << ", " ;
			else
				start = 0;
			cout << n->key ;
			print(n->right);
		}
	}

	nptr find(nptr n, double key) const
	{
		if (n)
		{
			if (key < n->key)
				return find(n->left, key);
			else if (key > n->key)
				return find(n->right, key);
		}
		return nullptr;
	}

	void findClosest(nptr n, double key)
	{
		if (n)
		{
			if (minDif > abs(n->key - key))
			{
				minDif = abs(n->key - key);
				closest = n;
			}
			
			if (key < n->key)
				findClosest(n->left, key);
			else if(key > n->key)
				findClosest(n->right, key);
			else
				return;
		}	
	}

};

int main(int argc, char **argv)
{
	BST myBST;
	double den = 200;
	int lim = 0;
	if (argc > 1)
		den = stoi(argv[1]);
	double e, k, pi = 3.141592653589793238;
	double minDif = numeric_limits<double>::max();
	pair<int, int> p1, p2;
	nptr p;
	while (exp(lim++/den) - 1 < pi)
		; 
	for (int i = 0; i < lim; i++)
		for (int j = i; j < lim; j++)
		{
			k = exp(i/den) + exp(j/den) - 2;
			if (k < pi)
			{
				myBST.insert(k, make_pair(i, j));
				p = myBST.findClosest(pi - k);
				if (abs(pi - (p->key + k)) < minDif)
				{
					minDif = abs(pi - (p->key + k));
					p1 = make_pair(i, j);
					p2 = p->val;
				}
			}				
		}		 

	cout << p1.first << ' ' << p1.second << ' ' << p2.first << ' ' << p2.second << '\n';

	return 0;
}
