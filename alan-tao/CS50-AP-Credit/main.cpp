#include <bits/stdc++.h>
using namespace std;

int T;

int main() {
  // freopen("1.in", "r", stdin);
  // freopen("1.out", "w", stdout);

  cin >> T;
  while (T--) {
    string c;
    cin >> c;
    int N = c.size();
    if (N < 2) continue;
    int sum = 0;
    for (int i = 0; i < N; i++) {
      int v = c[i] - '0';
      if ((N%2) ^ (i%2)) {
        sum += v;
      } else {
        sum += v*2/10;
        sum += v*2%10;
      }
    }

    if (sum%10 != 0) {
      cout << "INVALID" << endl;
      continue;
    }

    string pre = c.substr(0, 2);
    if ((pre == "34" || pre == "37") && N == 15) {
      cout << "AMEX" << endl;
    } else if (stoi(pre) <= 55 && stoi(pre) >= 51 && N == 16) {
      cout << "MASTERCARD" << endl;
    } else if (pre[0] == '4' && (N == 13 || N==16)) {
      cout << "VISA" << endl;
    } else {
      cout << "INVALID" << endl;
    }
  }
  
  return 0;
}