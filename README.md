# subtitlesConverter
Reformat VTT, SRT subtitle. Replace words.

PowerDirectorで字幕(.srt)を出力する
Teamsのビデオでトランスクリプト(.vtt)を出力する

ファイルを S:\rec\録音フォルダ配下のサブフォルダに配置する
├─afolder
├─anotherfolder
（中略）
├─anotherfolder
└─anotherfolder

たとえば
 S:\rec\録音\20240517_キックオフ のディレクトリ
2024/05/21  13:43       145,596,713 rec様プロジェクト_キックオフミーティング-20240517_103925-会議の録音.mp4
2024/06/17  07:00           135,734 subtitle.srt

その後、Pythonスクリプトで編集する
・python : 3の安定版を環境変数追加ありで導入
・python および pandasライブラリを利用
　pandas 追加導入：pip install pandas

全てをまとめて処理するバッチ
convall.bat
※recフォルダ直下にこれを含むプログラムを配置している前提で動作
※フォルダ名は上記bat内の環境変数で定義

それぞれのプログラムごとに実行する場合

仮に S:\rec> 配下にあるとして：

■PowerDirector字幕については

subtitle.srt を入力として出力を002.txtへリダイレクト
S:\rec>python printline3.py > 002.txt

002.txt を入力として出力を003.txtへリダイレクト
S:\rec>python removeCRLF.py > 003.txt

■トランスクリプト字幕(vtt)については

*.vtt を入力として出力を103.txtへリダイレクト
S:\rec>python printlinevtt.py > 103.txt

■AI字幕の文字化けなどを無理やり修正するには

?03.txt と conv.csv を入力として出力を ?03-conv.txtへリダイレクト
変換結果は置換文字列データ conv.csv 次第