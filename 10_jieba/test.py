import wordcloud

# 创建一个词云对象，中文需要指定字体
wc = wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\simhei.ttf',
                         background_color='white',
                         width=600, height=400)
text = '''
共享单车 way may not 我想你了 be obvious at first unless you're Dutch. 新媒体 地铁
Now is better 红烧肉 than never.
程序员 Although 共享单车 is often 高铁 than 海南 now. 高铁 地铁
If the impleme 武汉 ntation 想你 is hard to explain, it's a bad idea. 想你了
If 成都 implementation is 想你 easy to explain, it may be a good idea.
Namespaces are 端午one 端午 honking 王先生 great idea -- 成都 do more of those! 想你了
深圳 晚安 海南 新媒体
'''
wc.generate(text)
wc.to_file('词云.png')