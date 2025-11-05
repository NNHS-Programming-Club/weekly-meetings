#include <bits/stdc++.h>
using namespace std;
void p(string s) {cout << s << endl;}
int main() {
  int T; cin >> T;
  while (T--) {
    string c; cin >> c; int N = c.size();
    if (N < 2) continue;
    int sum = 0;
    for (int i = 0; i < N; i++) {
      int v = c[i] - '0';
      sum += (N%2) ^ (i%2) ? v : v*2/10+v*2%10;
    }
    if (sum%10 != 0) { p("INVALID"); continue; }
    string pre = c.substr(0, 2);
    if ((pre == "34" || pre == "37") && N == 15) p("AMEX");
    else if (stoi(pre) <= 55 && stoi(pre) >= 51 && N == 16) p("MASTERCARD");
    else if (pre[0] == '4' && (N == 13 || N==16)) p("VISA");
    else p("INVALID");
  }
  return 0;
}