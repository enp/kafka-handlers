import os, asyncio

from aiokafka import AIOKafkaProducer
from aiokafka.helpers import create_ssl_context

async def produce():
    producer = AIOKafkaProducer(
        bootstrap_servers=os.getenv('SERVERS', 'kafka-cluster:9092'),
        sasl_plain_username=os.getenv('USERNAME','kuser'),
        sasl_plain_password=os.getenv('PASSWORD','kpwd'),
        security_protocol='SASL_SSL',
        sasl_mechanism='PLAIN',
        ssl_context=create_ssl_context()
    )
    await producer.start()
    print("connected", flush=True)
    try:
        await producer.send_and_wait(os.getenv('TOPIC','handlers'), b"HELLO")
        print("sent", flush=True)
    finally:
        await producer.stop()

asyncio.run(produce())
