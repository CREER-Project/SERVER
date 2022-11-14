# CRÉER API

## "/"
属性: <code>GET</code>  

投稿されたライブ配信データを取得することができます。  
  
## "/lives/:id"
属性: <code>GET</code>  

指定された id のライブ配信データを取得することができます。  
  

## "/post"　
属性: <code>POST</code>  

新規でライブ配信枠を作成することができます。

### クエリパラメータ
- userName=(string)
- title=(string)
- videoDetail=(string)


## "/delete"
属性: <code>POST</code>  

ライブ配信枠を削除することができます。  

### クエリパラメータ
- id=(int)
