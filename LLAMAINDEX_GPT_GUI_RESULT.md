# LlamaIndex（一部LangChain） + GitLoader + Gpt3.5 + Streamlit
## 使用ソース
* [こちら](./src/llama_index_git_ui.py)
## 実行結果
### 画面構成
![a](img/image.png)
![k](img/image-10.png)
### ソースコード表示
![b](img/image-1.png)
![c](img/image-2.png)
### 処理の概要説明
![d](img/image-3.png)
### 全体リファクタリング
![e](img/image-4.png)
### クラス図
![f](img/image-5.png)

-- ここまでLlama Index --

-- ここからLlama Indexで取得したソースをGPTに投げる --

### 個別リファクタリング
![g](img/image-6.png)
![h](img/image-7.png)
![i](img/image-8.png)
![j](img/image-9.png)
### ソースコードの説明
![l](img/image-11.png)
![m](img/image-12.png)
![n](img/image-13.png)
## 評価、課題
* コスト面は同様にかかるものの、ソースコードの読み込みや吐かせる部分などはLangChainよりも精度が高くなった
* ソースコードを吐かせるプロンプトもかなり安定した
* クラス図もプロンプトによってはそれなりに詳細なものを吐くようになった
* リファクタリングなどはソースコード指定でGPTなどを利用した方が精度が高い（プロジェクト全体のリファクタリングは厳しそう）
* 個別リファクタリングや最初のGitHubからの読み込みなどが体感10秒程時間がかかる
## 参考
* https://gpt-index.readthedocs.io/en/latest/index.html
* https://llamahub.ai/l/github_repo
* https://rakuraku-engineer.com/posts/llamaIndex/
