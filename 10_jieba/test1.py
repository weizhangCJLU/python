# -*- coding: utf-8 -*-
import jieba

seg_str = "好好学习，天天向上。"

print("/".join(jieba.lcut(seg_str)))    # 精简模式，返回一个列表类型的结果
print("/".join(jieba.lcut(seg_str, cut_all=True)))      # 全模式，使用 'cut_all=True' 指定
print("/".join(jieba.lcut_for_search(seg_str)))     # 搜索引擎模式