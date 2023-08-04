# LangChain + GitLoader + Gpt3.5 + Streamlit
## 使用ソース
* [こちら](./src/lang_chain_git_ui.py)
## 実行結果
![a](img/telegram-cloud-photo-size-5-6206292713146529012-y.jpg)
![b](img/telegram-cloud-photo-size-5-6206292713146529013-y.jpg)
![c](img/telegram-cloud-photo-size-5-6206292713146529014-y.jpg)
![d](img/telegram-cloud-photo-size-5-6206292713146529015-y.jpg)
![e](img/telegram-cloud-photo-size-5-6206292713146529016-y.jpg)
## 課題
* VectorstoreIndexCreatorで、VectorStoreにChroma、embeddingにOpenAIEmbeddingsを使用した
    * ソースコードを吐かせるためのプロンプトが安定しない
    * 吐かせたソースコードが完全じゃない（deleteやupdateが抜けている）
* クラス図なども物凄い簡略されたものしか出さず、物足りなさを感じる
* VectorstoreIndexCreatorの使い方にあまり拡張性を感じなかった（本当はもっとできるのかもしれないけど）
* Token数をMaxに近い形にして幾つかの問答を行ったところ、$1.5ほどコストがかかった
## 参考
* https://youtu.be/xEjpMTMy24Y
* https://www.youtube.com/watch?v=Cod-3ymwvsQ