from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users_llm_chatbot'

    id = Column(Integer, unique=True, primary_key=True, index=True)
    name = Column(String, index=True)

class Chat(Base):
    __tablename__ = 'chats_llm_chatbot'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users_llm_chatbot.id"))
    name = Column(String)
    timestamp = Column(DateTime)

class Message(Base):
    __tablename__ = 'messages_llm_chatbot'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey("chats_llm_chatbot.id"))
    role = Column(String)
    content = Column(String)
    timestamp = Column(DateTime)
