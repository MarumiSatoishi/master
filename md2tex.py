import re
import os


## 素材をつくる

def omitlink(text): #リンクを一つ処理する
    text = re.sub(r'\[\[(.*?)\]\]', r'\1', text) #.*のあとに`?`をつけて非貪欲マッチにするのがミソ
    return text

def omitlinks(text): #すべてのリンクを処理する
    while re.serch() != '':
        omitlink(text)
        return text

def omitcomment(text): #コメントを一つ処理する
    return

def omitcomments(text):
    while re.serch() != '': #すべてのコメントを処理する
        omitcomment(text)
        return text


def quote(text): #引用
    text = re.sub(r'(?<=\n)> (.*)(?=\n)', r'\begin{quote}\n\1\n\end{quote}', text)

## コンバートする

def convert(text): #コンバート
        text = omitlinks(text)
        text = omitcomments(text)
        text = quote(text)
    return text