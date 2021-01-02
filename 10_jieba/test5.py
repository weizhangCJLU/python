import wordcloud

wc = wordcloud.WordCloud(background_color='white',
                         width=600, height=400,
                         font_path=r'C:\Windows\Fonts\simhei.ttf',
                         colormap='Reds')
text = '''
 way may Mars 我想你了 be obvious at first unless you're Mars.
Now is better 冰激淋 than never.
 Although  is often  than 海口 now. 
If the Mars 十堰 Mars 想你 is hard to explain, it's a bad Mars. 想你了
If 十堰 implementation is 想你 easy to Mars, it may be a good Mars.
Namespaces are one  honking  great idea -- 十堰 do more of those! 想你了
深圳 晚安 海口 
'''
wc.generate(text)
wc.to_file(r"C:\Users\Lenovo\PycharmProjects\untitled1\project\10_jieba\词云2.png")
