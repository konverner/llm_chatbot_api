import logging.config
import os

from dotenv import find_dotenv, load_dotenv
from omegaconf import OmegaConf
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from .models import Base

# Load logging configuration with OmegaConf
logging_config = OmegaConf.to_container(
    OmegaConf.load("./src/llm_chatbot_api/conf/logging_config.yaml"),
    resolve=True
)
logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)

load_dotenv(find_dotenv(usecwd=True))

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    logger.error("DATABASE_URL is not set in the environment variables.")
    exit(1)

def get_enginge():
    return create_engine(
        DATABASE_URL,
        connect_args={'connect_timeout': 5, "application_name": "llm_chatbot_api"},
        poolclass=NullPool
    )

def create_tables():
    engine = get_enginge()
    Base.metadata.create_all(engine)
    logger.info("Tables created")

def get_session():
    engine = get_enginge()
    return sessionmaker(bind=engine)()
