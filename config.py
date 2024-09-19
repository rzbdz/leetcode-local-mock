import os
import argparse


def replacer(src, key, snip=None, snip_file=None, dst=None):
    with open(src, "r") as f:
        template = f.read()
        if snip is None:
            with open(snip_file, "r") as f1:
                snip = f1.read()
        template = template.replace(key, snip)
    if dst is not None:
        with open(dst, "w") as f:
            f.write(template)
    return dst

solution_template = \
"""#include <bits/stdc++.h>
using namespace std;

"""
solution_template_sig = \
"""#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    REPLACEME {

    }
};
"""
input_template = \
"""INIT_INPUTS();
INPUT();
INPUT(); 

"""
output_template = \
"""#include <bits/stdc++.h>

void HANDLE_OUTPUT(std::string output) {
    std::cout<<"output: "<< output <<std::endl;
}

"""

def main():
    # 创建解析器对象
    parser = argparse.ArgumentParser(description="生成 engine.cpp 文件")
    # 添加参数
    parser.add_argument("--problem", type=str, required=True, help="题目名称")
    parser.add_argument("--gen", type=bool, required=False, help="指定为生成新solution")
    parser.add_argument("--sig", type=str, required=False, help="指定为生成新solution的函数签名")
    # parser.add_argument("--input", type=str, required=True, help="输入文件")
    # 解析命令行参数
    args = parser.parse_args()
    os.makedirs("build", exist_ok=True)
    if args.gen:
        os.makedirs(f"./solutions/{args.problem}", exist_ok=True)
        with open(f"./solutions/{args.problem}/input.txt", "w") as f:
            f.write(input_template)
        with open(f"./solutions/{args.problem}/output.cpp", "w") as f:
            f.write(output_template)
        with open(f"./solutions/{args.problem}/{args.problem}.h", "w") as f:
            if type(args.sig) is str:
               f.write(solution_template_sig.replace("REPLACEME", args.sig))
            else:
                f.write(solution_template)
        return
    gen1 = "template/engine.cpp"
    gen1 = replacer(
        gen1,
        "SOLUTION_PLACEHOLDER",
        snip=f"../solutions/{args.problem}/{args.problem}",
        dst="build/engine.cpp",
    )
    gen1 = replacer(
        gen1,
        "USER_INPUT_PLACEHOLDER//REPLACEME",
        snip_file=f"solutions/{args.problem}/input.txt",
        dst="build/engine.cpp",
    )
    gen1 = replacer(
        gen1,
        "TARGET_FUNCTION_PLACEHOLDER",
        snip=f"{args.problem}",
        dst="build/engine.cpp",
    )
    gen1 = replacer(
        gen1,
        "HANDLE_OUTPUT_PLACEHOLDER//REPLACEME",
        snip_file=f"solutions/{args.problem}/output.cpp",
        dst="build/engine.cpp",
    )
    gen1 = replacer(
        gen1,
        "//COMMENT_START",
        snip="/*",
        dst="build/engine.cpp",
    )
    gen1 = replacer(
        gen1,
        "//COMMENT_END",
        snip="*/",
        dst="build/engine.cpp",
    )



if __name__ == "__main__":
    main()
