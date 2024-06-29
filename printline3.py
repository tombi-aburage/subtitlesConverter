import os
import glob
import sys

def read_and_print_subtitle(directory):
  """
  UTF-16-LE エンコーディングの subtitle.srt ファイルを4行ずつ読み込み、3の倍数に相当する行のみを、そのまま出力する関数

  引数:
    directory: 読み込むファイルがあるはずのディレクトリ名

  戻り値:
    なし
  """
  # 指定されたディレクトリ内の.srtファイルを取得
  files = glob.glob(os.path.join(directory, '*.srt'))
  
  # ファイルが存在しない場合、エラーメッセージを出力して終了
  if not files:
    print("指定されたディレクトリに.srtファイルが存在しません。")
    return
  
  # 各ファイルを処理
  for file in files:
    with open(file, 'r', encoding="utf-16-le") as f:
      # 改行コードで区切って各行をリストに格納
      lines = f.read().splitlines()

      for i in range(0, len(lines), 4):
        print(''.join(lines[i + 2]))

# コマンドライン引数からディレクトリ名を取得、引数がなければ現在のディレクトリを使用
directory = sys.argv[1] if len(sys.argv) > 1 else "."

# 使用例
read_and_print_subtitle(directory)
