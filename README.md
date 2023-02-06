# judge_story_app
judge_story_appはその名の通り、steam上に存在するゲームのストーリーの評価をレビューから推測するアプリケーションです。
使い方は、steamのゲームのURLを入力し、判定ボタンを押し、しばらく待つだけです。
レビューの取得にはSteam APIを用いて、入力されたURLのゲームから情報を取得しています。
<img width="823" alt="スクリーンショット 2023-02-06 11 59 43" src="https://user-images.githubusercontent.com/97023705/216873625-3fb3d7cf-5509-49cf-b118-3c747d85b7d8.png">

## 使用例
1. 気になるゲームをSteamから探して、URLをコピーします。今回はエルデンリングというゲームのストーリーを判定してみます。https://store.steampowered.com/app/1245620/ELDEN_RING/
2. 次にアプリの入力欄にURLをペースとして判定をボタンを押します。
<img width="792" alt="スクリーンショット 2023-02-06 12 05 27" src="https://user-images.githubusercontent.com/97023705/216874426-78928a16-7790-44af-b996-09eb9cca26b3.png">
3. しばらく待つと結果が出ます！エルデンリグは面白いゲームらしいので評価3.3というのは明らかにおかしく判定はガバガバですが一応動きます。評価はストーリーが面白い(positive)と判断した数と面白くない(negative)と判断した数の割合で算出してます。
<img width="792" alt="スクリーンショット 2023-02-06 12 06 23" src="https://user-images.githubusercontent.com/97023705/216874575-cffb075b-11ae-4894-be0c-f7b651635bf7.png">


