# LlamaIndex（一部LangChain） + Gpt4 + Streamlit
## 変更点
* LlamaIndexがGitHubから持ってきた情報をVectorStoreに格納する部分をGPT-4に変更
* 単ファイル用のGPTモデルをGPT-4に変更
## 使用ソース
* [こちら](./src/llama_index_git_ui_gpt4.py)
## 実行結果
### ソースコード表示
![g](img/image-23.png)
![h](img/image-24.png)
![i](img/image-25.png)
### 全体リファクタリング
![j](img/image-26.png)
![k](img/image-27.png)
### クラス図作成
![a](img/image-17.png)
### リバースエンジニアリング
![b](img/image-18.png)
![c](img/image-19.png)
![d](img/image-20.png)
![e](img/image-21.png)
### SQLの抜き出し
![f](img/image-22.png)

-- ここまでLlama Index --

-- ここからLlama Indexで取得したソースをGPTに投げる --

### 個別リファクタリング
![l](img/image-28.png)
![m](img/image-29.png)
### ソースコードの説明
![n](img/image-30.png)
![o](img/image-31.png)
![p](img/image-32.png)
## 評価、課題
* 現時点で一番理想に近いものとなっている
* コスト面は思ったよりも少ない（上記の全てを実行しても$1.4程度）
* ソースコードを吐かせるプロンプトや出力結果も安定した
* クラス図がプロンプトをそこまで意識せずとも詳細なものを吐く
* プロジェクト全体のリファクタリングを行っても結果が返却されるようになった
* プロダクト全体をリバースエンジニアリングして表示させること自体には成功した（精度は荒い）
* GPT3.5を利用していた頃に比べて全ての回答に時間がかかっている
