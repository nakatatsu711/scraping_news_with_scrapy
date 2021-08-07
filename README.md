## 概要
Scrapyでニュースサイトをスクレイピングするプログラム

[Yahoo!ニュース](https://news.yahoo.co.jp/)と[gooニュース](https://news.goo.ne.jp/)から記事のタイトルと要約を取得します。



## システム環境
以下で動作確認済みです。  
OS：macOS 11.2.2  
Python：3.6.9



## 実行方法
### ライブラリインストール
以下の2通りの方法がありますので、どちらかでインストールしてください。
```
$ pip install scrapy
```
```
$ pip install -r requirements.txt
```


### プロジェクトの作成
newsというプロジェクトを作成します。テンプレートが作成されます。
```
$ scrapy startproject news
```

コマンドを実行する際は、基本的にこの`news`ディレクトリで実行するので、移動しておきます。
```
$ cd news
```


### ダウンロード間隔の設定
`settings.py`で設定します。

相手サイトに負荷をかけすぎないように必ず設定しておきましょう。  
今回は1秒に設定してあります。
```
DOWNLOAD_DELAY = 1
```


### Spiderの作成
Scrapyを使うのに、主に作成するのがSpiderというクラスです。  
対象のWebサイトごとにSpiderを作成し、クローリングの設定やスクレイピングの処理を記述します。  

`scrapy genspider`コマンドであらかじめ定義されているテンプレートからSpiderを作成できます。  
第1引数にSpiderの名前、第2引数にドメイン名を指定します。

例えば、以下のコマンドでは`spiders`ディレクトリ内に`news_crawl.py`というファイルが作成されます。
```
$ scrapy genspider news_crawl news.yahoo.co.jp
```

ファイルが作成されたら、これをベースに書き換えていきます。


### Itemの作成
ItemはSpiderが抜き出したデータを格納しておくためのオブジェクトです。  
`items.py`にクラスを作成することでItemを定義できます。`items.py`を好きなように書き換えてみてください。


### Pipelineの作成
ItemPipeline（以下、Pipeline）はSpiderから抽出したItemに対して任意の処理を行うためのコンポーネントです。  
`piplines.py`にクラスを作成することでPipelineを定義できます。`piplines.py`を好きなように書き換えてみてください。

作成したPipelineを使用するためには、`settings.py`に設定を追加する必要があります。  
ValidationPipelineというクラスを作成した場合は以下のように設定します。
```
ITEM_PIPELINES = {
    'news.pipelines.ValidationPipeline': 300,
}
```


### 実行
コマンドラインで実行します。  
スクレイピングしたItemは`news_crawl.jl`というファイルに保存されます。
```
$ scrapy crawl news_crawl -o news_crawl.jl
```
