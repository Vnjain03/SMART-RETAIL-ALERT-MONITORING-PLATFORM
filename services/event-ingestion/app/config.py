from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App Configuration
    app_name: str = "Event Ingestion Service"
    environment: str = "development"
    debug: bool = True
    log_level: str = "info"
    port: int = 8001
    
    # Kafka Configuration
    kafka_bootstrap_servers: str = "localhost:9092"
    kafka_topic_events: str = "service-events"
    kafka_topic_metrics: str = "aggregated-metrics"
    kafka_client_id: str = "event-ingestion-service"
    kafka_acks: str = "all"
    kafka_compression_type: str = "gzip"
    kafka_max_batch_size: int = 16384
    kafka_linger_ms: int = 10
    
    # OpenTelemetry
    jaeger_agent_host: str = "localhost"
    jaeger_agent_port: int = 6831
    otel_service_name: str = "event-ingestion"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
