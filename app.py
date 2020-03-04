import connexion
from pykafka import KafkaClient
from pykafka.common import OffsetType
import yaml
import json
import datetime

with open('app_conf.yaml', 'r') as f:
    app_config = yaml.safe_load(f.read())
    kafka_server = app_config['kafka-conf']['kafka-server']
    kafka_port = app_config['kafka-conf']['kafka-port']
    kafka_topic = app_config['kafka-conf']['kafka-topic']


def event1(offset=None):

    offset = offset

    if offset is None:
        return 'Please supply an offset value (integer)'

    client = KafkaClient(hosts='{}:{}'.format(kafka_server, kafka_port))
    topic = client.topics['{}'.format(kafka_topic)]
    consumer = topic.get_simple_consumer(
        consumer_group="my_group",
        auto_offset_reset=OffsetType.EARLIEST,
        reset_offset_on_start=False)

    #consumer.commit_offsets(partition_offsets=offset)
    data = consumer.consume()

    return data


def event2(offset=None):

    offset = offset

    if offset is None:
        return 'Please supply an offset value (integer)'


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='')
    app.add_api('openapi.yaml')
    app.run(port=8110)
