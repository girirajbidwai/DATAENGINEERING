def write_row_in_mongo(df, epoch_id):
    mongoURL = "mongodb+srv://Lorena:<Password>@cluster0.9psdq.mongodb.net/<database>.<collection>" \
               "?retryWrites=true&w=majority "
    df.write.format("mongo").mode("append").option("uri", mongoURL).save()
    pass
  
  
query = sentiment_tweets.writeStream.queryName("test_tweets") \
        .foreachBatch(write_row_in_mongo).start()
query.awaitTermination()
