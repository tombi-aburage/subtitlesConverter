import os
import glob
import sys

def concatenate_lines(directory):

    # 指定されたディレクトリ内の002.txtファイルを取得
    files = glob.glob(os.path.join(directory, '002.txt'))
  
    # ファイルが存在しない場合、エラーメッセージを出力して終了
    if not files:
        print("指定されたディレクトリに002.txtファイルが存在しません。")
        return
    
    # 各ファイルを処理
    for file in files:
        with open(file, 'r', newline='') as file:
            lines = file.readlines()

        result = ''
        for line in lines:
            # 改行コードを除去
            line = line.rstrip('\r\n')

            # 行の末尾が日本語の句点「。△」ではない場合、文字列を結合
            if not line.endswith('。'):
                result += line
            else:
                result += line + '\r\n'

        return result

# コマンドライン引数からディレクトリ名を取得、引数がなければ現在のディレクトリを使用
directory = sys.argv[1] if len(sys.argv) > 1 else "."

# 使用例
print(concatenate_lines(directory))

