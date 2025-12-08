#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using pii = pair<int, int>;

const int MOD = 1e9 + 7;

int main() {
  // ios_base::sync_with_stdio(false);
  // cin.tie(NULL);
  freopen("1.in", "r", stdin);
  freopen("1.out", "w", stdout);

  string num; int p;
  cin >> num >> p;

  int N = num.size();
  int pd = num[N-p] - '0';
  cout << pd << endl;
  for (int i = 0; i < N-p; i++) {
    num[i] = ((num[i] - '0') + pd) % 10 + '0';
  }

  for (int i = N-p+1; i < N; i++) {
    num[i] = abs(num[i] - '0' - pd) + '0';
  }

  cout << num << endl;
  return 0;
}