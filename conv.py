import pandas as pd
import os
import glob
import sys

def convert_words(directory):

    # 指定されたディレクトリ内の?03.txtファイルを取得
    files = glob.glob(os.path.join(directory, '?03.txt'))
  
    # ファイルが存在しない場合、エラーメッセージを出力して終了
    if not files:
        print("指定されたディレクトリに?03.txtファイルが存在しません。")
        return
        
    # 置換ルールを読み込む
    df = pd.read_csv('conv.csv', encoding='utf-8')

    # 各ファイルを処理
    for file in files:
        with open(file, 'r', encoding='shift_jis') as file:
            text = file.read()

        # 置換ルールに従って文字列を置換
        df = df.fillna('')
        for index, row in df.iterrows():
            text = text.replace(row['置換前'], row['置換後'])

        # 結果を新しいファイルに書き込む
        with open(file.name + '-' + os.path.basename(directory) + '.txt', 'w') as file:
            file.write(text)

# コマンドライン引数からディレクトリ名を取得、引数がなければ現在のディレクトリを使用
directory = sys.argv[1] if len(sys.argv) > 1 else "."

# 使用例
print(convert_words(directory))
