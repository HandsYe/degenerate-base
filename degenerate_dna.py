#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
处理含有兼并碱基的DNA序列，输出所有可能的具体序列组合
"""

# 定义兼并碱基映射关系
DEGENERATE_BASE_MAP = {
    'A': ['A'],
    'T': ['T'],
    'C': ['C'],
    'G': ['G'],
    'R': ['A', 'G'],      # 嘌呤
    'Y': ['C', 'T'],      # 嘧啶
    'S': ['G', 'C'],
    'W': ['A', 'T'],
    'K': ['G', 'T'],
    'M': ['A', 'C'],
    'B': ['C', 'G', 'T'],
    'D': ['A', 'G', 'T'],
    'H': ['A', 'C', 'T'],
    'V': ['A', 'C', 'G'],
    'N': ['A', 'C', 'G', 'T']  # 任意碱基
}

def get_all_combinations(sequence):
    """
    根据输入的兼并碱基序列，生成所有可能的具体序列组合
    
    Args:
        sequence (str): 含有兼并碱基的DNA序列
        
    Returns:
        list: 所有可能的具体序列组合
    """
    if not sequence:
        return ['']
    
    # 获取第一个字符对应的所有可能碱基
    first_char = sequence[0].upper()
    if first_char not in DEGENERATE_BASE_MAP:
        raise ValueError(f"未知的碱基字符: {first_char}")
    
    possible_bases = DEGENERATE_BASE_MAP[first_char]
    
    # 递归获取剩余序列的所有组合
    rest_combinations = get_all_combinations(sequence[1:])
    
    # 将当前字符的每种可能与剩余序列的所有组合相结合
    result = []
    for base in possible_bases:
        for combination in rest_combinations:
            result.append(base + combination)
    
    return result

def main():
    """主函数"""
    print("兼并碱基DNA序列展开程序")
    print("=" * 30)
    
    while True:
        try:
            sequence = input("\n请输入含有兼并碱基的DNA序列 (输入 'quit' 或 'q' 退出): ").strip()
            
            if sequence.lower() == 'quit' or sequence.lower() == 'q':
                print("程序结束。")
                break
            
            # 去除序列中的所有空格
            sequence = sequence.replace(' ', '')
            
            if not sequence:
                print("输入不能为空，请重新输入。")
                continue
                
            combinations = get_all_combinations(sequence)
            
            print(f"\n输入序列: {sequence}")
            print(f"可能的组合数: {len(combinations)}")
            print("所有可能的序列:")
            
            # 每行显示10个序列
            for i, combo in enumerate(combinations, 1):
                print(f"{combo:>10}", end=" ")
                if i % 10 == 0:
                    print()  # 换行
                    
            if len(combinations) % 10 != 0:
                print()  # 最后换行
                
        except ValueError as e:
            print(f"错误: {e}")
        except KeyboardInterrupt:
            print("\n\n程序被用户中断。")
            break
        except Exception as e:
            print(f"发生未预期的错误: {e}")

if __name__ == "__main__":
    main()