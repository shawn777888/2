# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:12:13 2024

@author: chenbailun
"""

def truth_table():
    # 定義變數P和Q的可能值
    variables = [False, True]

    # 列印表頭
    print("| P | Q | P ∧ Q | P ∨ Q | P ∧ Q | P ∨ Q | P → Q | P ← Q | P ↔ Q |")
    print("|---|---|-------|-------|-------|-------|-------|-------|-------|")

    # 遍歷所有可能的組合
    for p in variables:
        for q in variables:
            # 計算邏輯運算的結果
            conjunction = p and q
            disjunction = p or q
            nand = not (p and q)
            nor = not (p or q)
            implies = (not p) or q
            left_implies = p or (not q)
            iff = (p and q) or (not p and not q)

            # 列印結果
            print(f"| {p} | {q} |   {conjunction}   |   {disjunction}   |   {nand}   |   {nor}   |   {implies}   |   {left_implies}   |   {iff}   |")

# 呼叫函數生成並印出真值表
truth_table()
