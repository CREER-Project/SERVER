# CRÉER API

## "/"
属性: <code>GET</code>  

投稿された全てのライブ配信データを取得することができます。  
  
## "/lives/:id"
属性: <code>GET</code>  

指定された id (int) のライブ配信データを取得することができます。  
  
## "/search/:videoTextHex"
属性: <code>GET</code>  

指定された id (string) のライブ配信データを取得することができます。  
  

## "/post"　
属性: <code>POST</code>  

新規でライブ配信枠を作成することができます。

### クエリパラメータ
- tag=(string)
- title=(string)
- videoDetail=(string)


## "/delete"
属性: <code>POST</code>  

ライブ配信枠を削除することができます。  

### クエリパラメータ
- id=(int)

