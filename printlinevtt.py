# 引数で指定されたフォルダに格納されている拡張子が .vtt であるファイルを開く。
# もしファイルが無かった場合、その旨のエラーを標準出力に出力して終了する。
# ファイルがあった場合には、一行ずつ、次の処理を行う。
# ・文字列を格納する変数 strSpeech を空文字列で初期化する。
# ・読み込んだ行の文字列が WEBVTT であった場合には、何もしない。
# ・読み込んだ行の文字列に - が5個含まれる場合には、何もしない。
# ・読み込んだ行の文字列に --> が1個含まれる場合には、何もしない。
# ・それ以外の場合には、変数 strSpeech の末尾に、読み込んだ文字列を追加する。
# ・読み込んだ行の文字列が空文字列の場合、変数 strSpeech を標準出力に出力し、その後に初期化する。
#・ファイル終端 EOF に到達した場合は、処理を終了する。到達していない場合には、次の行の処理を行う。
# というプログラムを出力

#strSpeech を出力するさいに、末尾に改行コードを追加してください

# encoding="utf-8" を追加

# ディレクトリ名をコマンドライン引数で与えるように変更してください

# コマンドライン引数が与えられなかった場合には、初期値として . を directory に設定してください

import os
import glob
import sys

def process_vtt_files(directory):
    # 指定されたディレクトリ内の.vttファイルを取得
    files = glob.glob(os.path.join(directory, '*.vtt'))

    # ファイルが存在しない場合、エラーメッセージを出力して終了
    if not files:
        print("指定されたディレクトリに.vttファイルが存在しません。")
        return

    # 各ファイルを処理
    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            strSpeech = ""
            for line in f:
                line = line.strip()  # 行の前後の空白を削除
                if line == "WEBVTT" or line.count('-') == 5:    # or 
                    continue
                elif "-->" in line:
                    print(line)
                elif line == "":
                    print(strSpeech + "\n")  # 末尾に改行コードを追加
                    strSpeech = ""
                else:
                    strSpeech += line

            # ファイルの終端に達した場合、最後のstrSpeechを出力
            if strSpeech != "":
                print(strSpeech + "\n")  # 末尾に改行コードを追加

# コマンドライン引数からディレクトリ名を取得、引数がなければ現在のディレクトリを使用
directory = sys.argv[1] if len(sys.argv) > 1 else "."

# 使用例
process_vtt_files(directory)

