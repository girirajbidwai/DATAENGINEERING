#### Establishing connection with EC2 using  GIT BASH FROM LOCAL MACHINE

###### 1.ssh -i Downloads/<key-pair.pem>{OS}@Public IPv4 address
###### 2.sudo -su (switching to root user)

#### Installing Docker and Docker-compose on EC2 Instance

###### 1.yum install docker -y
###### 2.curl -SL https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
###### 3.sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

#### Confluent on Docker

###### 1.mkdir docker-compose.yml
###### 2.docker-compose -f docker-compose.yml up (This will install all the required images from docker hub of confluent)
###### 3.Make sure everything is up and running
              $ docker-compose ps
                   Name                  Command               State                    Ports
              ---------------------------------------------------------------------------------------------
              broker            /etc/confluent/docker/run   Up             0.0.0.0:9092->9092/tcp
              kafka-connect     bash -c #                   Up (healthy)   0.0.0.0:8083->8083/tcp, 9092/tcp
                                echo "Installing ...
              ksqldb            /usr/bin/docker/run         Up             0.0.0.0:8088->8088/tcp
              schema-registry   /etc/confluent/docker/run   Up             0.0.0.0:8081->8081/tcp
              zookeeper         /etc/confluent/docker/run   Up             2181/tcp, 2888/tcp, 3888/tcp


#### Streaming data from Kafka to S3 using Kafka Connect
##### This uses Docker Compose to run the Kafka Connect worker.
###### 1.Create the S3 bucket, make a note of the region
###### 2.Obtain your access key pair
###### 3.Update aws_credentials
###### 4.Alternatively, uncomment the environment lines for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and set the values here instead
###### 5.Create the Sink connector

              curl -i -X PUT -H "Accept:application/json" \
                  -H  "Content-Type:application/json" http://localhost:8083/connectors/sink-s3-voluble/config \
                  -d '
               {
                  "connector.class": "io.confluent.connect.s3.S3SinkConnector",
                  "key.converter":"org.apache.kafka.connect.storage.StringConverter",
                  "tasks.max": "1",
                  "topics": "cats",
                  "s3.region": "us-east-1",
                  "s3.bucket.name": "rmoff-voluble-test",
                  "flush.size": "65536",
                  "storage.class": "io.confluent.connect.s3.storage.S3Storage",
                  "format.class": "io.confluent.connect.s3.format.avro.AvroFormat",
                  "schema.generator.class": "io.confluent.connect.storage.hive.schema.DefaultSchemaGenerator",
                  "schema.compatibility": "NONE",
                      "partitioner.class": "io.confluent.connect.storage.partitioner.DefaultPartitioner",
                      "transforms": "AddMetadata",
                      "transforms.AddMetadata.type": "org.apache.kafka.connect.transforms.InsertField$Value",
                      "transforms.AddMetadata.offset.field": "_offset",
                      "transforms.AddMetadata.partition.field": "_partition"
                }



                    Things to customise for your environment:

                    topics : the source topic(s) you want to send to S3

                    key.converter : match the serialisation of your source data (see here)

                    value.converter : match the serialisation of your source data (see here)

                    transforms : remove this if you don’t want partition and offset added to each message
                    
                    
                  CREATE SOURCE CONNECTOR s WITH (
                  'connector.class' = 'io.mdrogalis.voluble.VolubleSourceConnector',

                  'genkp.owners.with' = '#{Internet.uuid}',
                  'genv.owners.name.with' = '#{Name.full_name}',
                  'genv.owners.creditCardNumber.with' = '#{Finance.credit_card}',

                  'genk.cats.name.with' = '#{FunnyName.name}',
                  'genv.cats.owner.matching' = 'owners.key',

                  'genk.diets.catName.matching' = 'cats.key.name',
                  'genv.diets.dish.with' = '#{Food.vegetables}',
                  'genv.diets.measurement.with' = '#{Food.measurements}',
                  'genv.diets.size.with' = '#{Food.measurement_sizes}',

                  'genk.adopters.name.sometimes.with' = '#{Name.full_name}',
                  'genk.adopters.name.sometimes.matching' = 'adopters.key.name',
                  'genv.adopters.jobTitle.with' = '#{Job.title}',
                  'attrk.adopters.name.matching.rate' = '0.05',
                  'topic.adopters.tombstone.rate' = '0.10',

                  'global.history.records.max' = '100000'
                );
                
                
SHOW TOPICS;
PRINT cats;
