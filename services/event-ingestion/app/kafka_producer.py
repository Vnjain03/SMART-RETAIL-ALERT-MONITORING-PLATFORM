from aiokafka import AIOKafkaProducer
import json
import logging
from .config import settings

logger = logging.getLogger(__name__)


class KafkaProducerManager:
    def __init__(self):
        self.producer: AIOKafkaProducer = None
        
    async def start(self):
        """Start Kafka producer"""
        try:
            self.producer = AIOKafkaProducer(
                bootstrap_servers=settings.kafka_bootstrap_servers,
                client_id=settings.kafka_client_id,
                acks=settings.kafka_acks,
                compression_type=settings.kafka_compression_type,
                max_batch_size=settings.kafka_max_batch_size,
                linger_ms=settings.kafka_linger_ms,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            await self.producer.start()
            logger.info("Kafka producer started successfully")
        except Exception as e:
            logger.error(f"Failed to start Kafka producer: {e}")
            raise
    
    async def stop(self):
        """Stop Kafka producer"""
        if self.producer:
            await self.producer.stop()
            logger.info("Kafka producer stopped")
    
    async def send_event(self, topic: str, event: dict, key: str = None):
        """Send event to Kafka topic"""
        try:
            key_bytes = key.encode('utf-8') if key else None
            await self.producer.send_and_wait(
                topic,
                value=event,
                key=key_bytes
            )
            logger.debug(f"Event sent to topic {topic}: {event.get('id')}")
        except Exception as e:
            logger.error(f"Failed to send event to Kafka: {e}")
            raise


kafka_producer = KafkaProducerManager()
