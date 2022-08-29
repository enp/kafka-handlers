import os, asyncio

from aiokafka import AIOKafkaConsumer
from aiokafka.helpers import create_ssl_context

async def consume():
    consumer = AIOKafkaConsumer(
        os.getenv('TOPIC','handlers'),
        bootstrap_servers=os.getenv('SERVERS', 'kafka-cluster:9092'),
        group_id=os.getenv('GROUP','handlers'),
        sasl_plain_username=os.getenv('USERNAME','kuser'),
        sasl_plain_password=os.getenv('PASSWORD','kpwd'),
        security_protocol='SASL_SSL',
        sasl_mechanism='PLAIN',
        ssl_context=create_ssl_context()
    )
    await consumer.start()
    print("connected", flush=True)
    try:
        async for msg in consumer:
            print(f"consumed = {msg.partition}:{msg.offset}:{msg.key}:{msg.value}", flush=True)
    finally:
        await consumer.stop()

asyncio.run(consume())
