## 使用ソース
* [こちら](./src/lang_chain_git.py)
## 実行結果
```
@Ms-Mac SampleAI % python3 lang_chain_git.py
GitHubのURLを入力してください：https://github.com/MarthurGalarsy/SampleProduct
プログラムの種類を入力してください（ex：.kt）：.kt
ブランチを入力してください：main
質問を入力してください (終了するには 'exit' と入力してください)：ControllerとServiceを列挙してください
回答：  MemberControllerとMemberService
質問を入力してください (終了するには 'exit' と入力してください)：Member Controllerの処理内容を教えてください
回答：  Member Controllerでは、GET、POST、PUT、DELETEの4つのHTTPメソッドを使用して、Member Serviceを介してMember Mapperを使用してデータベースからメンバー情報を取得、作成、更新、削除する処理を行います。
質問を入力してください (終了するには 'exit' と入力してください)：MemberServiceの処理内容を教えてください
回答：  MemberServiceは、MemberMapperを使用して、メンバーを取得、作成、更新、削除するためのサービスです。
質問を入力してください (終了するには 'exit' と入力してください)：MemberMapperに存在するSQLのうち、Selectするものを教えてください
回答：  SELECT * FROM member AND status = 1
質問を入力してください (終了するには 'exit' と入力してください)：Memberのデータクラスに含まれる要素を教えてください
回答：  Memberデータクラスには、id、name、mailAddress、password、statusの5つの要素が含まれています。
質問を入力してください (終了するには 'exit' と入力してください)：Member Controller、MemberServiceの関係をクラス図を用いてmermaid記法で説明してください
回答： 

classDiagram
    MemberController --> MemberService
end
質問を入力してください (終了するには 'exit' と入力してください)：えexit
```

## 評価、課題
* 思っていたよりは精度の高い回答が得られた（もっとチグハグかと思った）
    * →精度がAPI頼みで返ってきた回答に対する拡張性などに乏しい
* 一方でこちらが目指しているレベルよりは低い
    * →リファクタリングや機能追加の提案をさせるようなプロンプトは回答を得られなかった
    * →回答が得られないと加工のしようもない
* かなり小さいリポジトリに対して幾つかの問答を行った結果
    * 約0.5$かかっているので、大規模リポジトリに対しての価格が心配
    * 精度が下がるのではないかと危惧している
