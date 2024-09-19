# leetcode local tester

Usage:

When you want to create a new solution, just run:

```bash
python3 config.py --problem lengthOfLongestSubstring --sig="int lengthOfLongestSubstring(string s)" --gen=True
```

It will generate some template files in solutions/lengthOfLongestSubstring.

then you should edit the following files:

solutions/lengthOfLongestSubstring/input.txt:

```cpp
INIT_INPUTS(string);
INPUT("abcabcabb");
INPUT("abcabcbb"); 
```

solutions/lengthOfLongestSubstring/output.cpp:

```cpp
#include <bits/stdc++.h>

void HANDLE_OUTPUT(int output) {
    std::cout<<"output: "<< output <<std::endl;
}
```

solutions/lengthOfLongestSubstring/lengthOfLongestSubstring.h:
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        return 5;
    }
};

```


When all test case are ready, you then can run the following command to genearate source codes:

```bash
python3 config.py  --problem lengthOfLongestSubstring
```

Then you can build it with:

```bash
make
```

Then you can run the solution and check the results:

```bash
leetcode-local-mock$ ./engine
output: 5
output: 5
```

A existing demo is in solutions/echo_test directory.