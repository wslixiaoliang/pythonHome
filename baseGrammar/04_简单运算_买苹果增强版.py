#!/usr/local/Cellar/python/3.7.7/bin/python3.7
# coding=utf-8
# buy Apple 增强版需求：收银员输入：苹果单价 && 苹果重量 回车后：输出总金额

# 定义提示字符串
print()
prince = float(input('输入苹果单价：'))

print()
weight = float(input('输入苹果的重量：'))

# 计算总价格
finalCost = prince * weight

# 定义输出字符串
finalTips = '您应支付的总金额为：'

# 输出拼接字符串
print()
print(finalTips, end="")
print(finalCost, end=" 元")


