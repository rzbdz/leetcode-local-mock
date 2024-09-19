#include <bits/stdc++.h>

#include "SOLUTION_PLACEHOLDER.h"

/*
使用方法，
1. 替换 "USER_INPUT_PLACEHOLDER//REPLACEME" 为特定格式
    如：
    INIT_INPUTS(std::string);
    INPUT("abc");
    INPUT("bcd"); 
2. 替换本文件的 SOLUTION_PLACEHOLDER 为你要执行的 solutions/xx.h
3. 替换本文件的 TARGET_FUNCTION_PLACEHOLDER 为你要执行的成员函数。
4. 替换本文将的 HANDLE_OUTPUT_PLACEHOLDER 为你要处理output的函数。
*/


template<typename... Args>
class InputCollector {
public:
    // 初始化一个空的 array
    InputCollector() {
        // 使用默认构造函数初始化
    }
    // 添加输入
    void addInput(Args... args) {
        inputs.emplace_back(std::make_tuple(args...));
    }
    // 获取输入
    auto getInputs() const {
        return inputs;
    }
private:
    std::vector<std::tuple<Args...>> inputs; // 假设最大输入数量为 10
};

// 宏定义用于方便输入
#define INIT_INPUTS(...) InputCollector<__VA_ARGS__> collector
#define INPUT(...) collector.addInput(__VA_ARGS__)
#define INPUTS collector.getInputs()


#ifdef DEV_CLANGD
#define USER_INPUT_PLACEHOLDER \
    INIT_INPUTS(std::string);\
    INPUT("abc");  \
    INPUT("bcd"); 
#endif

inline auto generate_input_tuples() {
    USER_INPUT_PLACEHOLDER//REPLACEME
    return INPUTS; // 返回收集到的输入
}

//COMMENT_START
#ifdef DEV_CLANGD
#define HANDLE_OUTPUT(output) \
    std::cout << output << std::endl;
#define HANDLE_OUTPUT_PLACEHOLDER 
#endif
//COMMENT_END

HANDLE_OUTPUT_PLACEHOLDER//REPLACEME

int main(void) {
  Solution sol;
  auto inputs = generate_input_tuples();
  for (auto &in_args : inputs) {
    auto res = std::apply(
        [&sol](auto &&...args) {
          return sol.TARGET_FUNCTION_PLACEHOLDER(
              std::forward<decltype(args)>(args)...);
        },
        in_args);
    HANDLE_OUTPUT(res);
  }
  return 0;
}

