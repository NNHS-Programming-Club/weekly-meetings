#include <bits/stdc++.h>

using namespace std;

int N;

int main() {
  // delete these two lines for io from console
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  // read N
  cin >> N;

  vector<int> arr(N);
  int ans = 0;
  for (int i = 0; i < N; i++) {
    // cin automatically seperated by space
    cin >> arr[i];
    ans += arr[i];
  }

  // print ans
  cout << ans << endl;

  return 0;
}