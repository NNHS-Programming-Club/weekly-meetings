# Input and Output

###### Author: Alan Tao

The first thing that one should know in competitive programming is input and output. Specifically, reading and writing to files or to the console. In this lesson, we look at all the input/output for Python, Java, and C++.

## Python
Python is the most straightforward and simplist. 

### Console
No need to define any variable. Just use `input()` to get a line and `print()` to print something out to the console. Notice that if the values are seperated by spaces, then use can use `.split()` to split it into an list. We also need to use `int()` to convert string into integers

```python
n = int(input())
arr = input().split()
```

### File
We will need two variables, one for the input file and one for the output file. They can be defined like:

```python
fin = open("input.txt", "r")
fout = open("output.txt", "w")
```

Please don't name the variable `input` or `in` because they are keywords in Python. 

To read a line, we simply do
```python
fin.readline()
```

to print a line, we simply do
```python
fout.write("hi\n")
```

Notice that if we want to print a new line at the end, we need to attatch a `"\n"` at the end. 

## Java

Java is the most complicated out of the three, so it is best to save it or make a template so that you don't have to type it out everytime 

### Console

There are two ways, the first way is to use a Scanner. 

```java
Scanner sc = new Scanner(System.in);

int N = Integer.parseInt(sc.nextLine());

sc.close();
```
`Integer.parseInt()` is a function that converts a string to integer. Don't forget to close the Scanner at the end of the program. 


Here is a way using BufferedReader and PrintWriter, this looks more complicated, but they need to be used when doing input and output through a file. So it's good to learn them for console as well. 

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
PrintWriter pw = new PrintWriter(System.out);

int N = Integer.parseInt(br.readLine());

pw.println(N);

br.close();
pw.close();
```

Notice that `pw.println()` prints a new line automatically, so there's no need for `"\n"`. Close both `br` and `pw` at the end. 

### File

```java
BufferedReader br = new BufferedReader(new FileReader("input.txt"));
PrintWriter pw = new PrintWriter(new File("output.txt"));

int N = Integer.parseInt(br.readLine());

pw.println(N);

br.close();
pw.close();
```

Very similar to the previous method. 

## C++
In my opinion, C++ has the easiest input and output for competitive programming. 

### Console
```cpp
int N;
cin >> N;

vector<int> arr(N);
for (int i = 0; i < N; i++) {
  cin >> arr[i];
}

cout << N << endl;
```

Very simple. The direction of the arrows matter. The `endl` means new line. It's technically `std::endl` if there's no `using namespace std;` in the program. 

Another thing is the C++ automatically seperates things by spaces, if the input is `2 3 4 2 3`, `cin` would read the integers one by one. There's also no need to convert it to an integer, because `cin` does that automatically when reading into an integer variable. This is why C++ is good for competitive programming. 

### File
We need two extra lines for file input and output. It is very similar to Python. 
```cpp
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);

cin >> N;

cout << N << endl;
```

That's it. The `cin` and `cout` is the exact same. 

## Conclusion
You do NOT need to memorize this. Creating a template for input and output is perfectly fine. I have provided programs with comments about this, so you don't need to write it yourself. 