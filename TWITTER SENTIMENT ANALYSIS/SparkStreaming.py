from pyspark.sql import functions as F
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.types import StringType, StructType, StructField, FloatType
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, udf
from pyspark.ml.feature import RegexTokenizer
import re
from textblob import TextBlob


#Spark session and start reading stream which came from Kafka. This implies that the connection with Kafka has to be done.

spark = SparkSession \
        .builder \
        .appName("TwitterSentimentAnalysis") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
        .getOrCreate()

df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "twitter") \
        .load()

#Here we just get the "text". As the data is coming from Kafka, this data is in a JSON form with multiple information such as the created date of the tweet, 
#the username… And, "text" is the one that has the tweet text.
mySchema = StructType([StructField("text", StringType(), True)])
    # Get only the "text" from the information we receive from Kafka. The text is the tweet produce by a user
    values = df.select(from_json(df.value.cast("string"), mySchema).alias("tweet"))
    
  
