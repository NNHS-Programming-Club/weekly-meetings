import java.io.*;
import java.util.*;

class InputOutput {
  private static StringTokenizer st;
  public static void main(String[] args) throws IOException {
    // user typed input:
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // Scanner sc = new Scanner(System.in);

    // input from file
    BufferedReader br = new BufferedReader(new FileReader("input.txt"));

    // print output to console
    // PrintWriter pw = new PrintWriter(System.out);

    // output to file
    PrintWriter pw = new PrintWriter(new File("output.txt"));

    // reading a line
    st = new StringTokenizer(br.readLine());

    // reading N from st
    int N = Integer.parseInt(st.nextToken());

    // reading second line
    st = new StringTokenizer(br.readLine());

    int[] arr = new int[N];
    int ans = 0;
    for (int i = 0; i < N; i++) {
      // get each integer seperated by space
      arr[i] = Integer.parseInt(st.nextToken());
      ans += arr[i];
    }

    pw.println(ans);

    pw.close();
    br.close();
  }
}