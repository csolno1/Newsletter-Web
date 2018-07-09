# -*- encoding: utf8 -*-
import html2text
source = "captured/"
dst = "capturedMd/"
file = "*.out"

import glob
for file in glob.glob(source + file):
    t = file.rsplit('\\', 1)
    dir = t[0]
    name = t[1]
    savename = name.rsplit('.', 1)[0] + '.md'
    i = open(file, 'r', encoding='utf-8')
    o = open(dst + savename, 'w', encoding='utf-8')
    c = i.read()
    c = html2text.html2text(c)
    from regex import sub
    #c = sub(r'\*\*\s*(.*)\*\*', '**\1**  ', c)
    c = sub(r'\*\*\s*', '**', c)
    #c = sub(u'\*\*([\u4e00-\u9fa5]+)', '**\1fuck', c)
    #c = sub(u'\*\*(.+)\*\*', u'**\1**\n', c)
    c = sub(r'!\[(.*)\]\((.*)\n(.*)\)', r'![\1](\2\3)', c)
    c = sub('原标题：', '# ', c)
    o.write(c)
    i.close()
    o.close()



