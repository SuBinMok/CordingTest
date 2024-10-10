#include <iostream>
#include <string.h>
#include <stack>
using namespace std;

int main() {
	stack<char> b;
	stack<char> a;
	char c[100001];
	char s;
	cin >> c;
	int n;
	int num = strlen(c);
	for (int i = 0; i < num; i++) {
		b.push(c[i]);
	}
	cin >> n;
	for (int j = 0; j < n;j++) {
		cin >> s;
		if (s == 'L') {
			if (!b.empty()) {
				a.push(b.top());
				b.pop();
			}
		}
		else if (s == 'D') {
			if (!a.empty()) {
				b.push(a.top());
				a.pop();
			}
		}
		else if (s == 'B') {
			if (!b.empty()) {
				b.pop();
			}
		}
		else if (s == 'P') {
			char x;
			cin >> x;
			b.push(x);
		}
	}
	for (int t = b.size() ; t >0 ;t--) {
		a.push(b.top());
		b.pop();
	}
	for (int u = a.size(); u >0 ; u--) {
		cout << a.top();
		a.pop();
	}
}