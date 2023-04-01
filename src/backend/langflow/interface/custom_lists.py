## LLM
from typing import Any, Dict, Type

from langchain import llms
from langchain import vectorstores
from langchain.llms.openai import OpenAIChat

llm_type_to_cls_dict = llms.type_to_cls_dict
llm_type_to_cls_dict["openai-chat"] = OpenAIChat





### VectorStores
from langchain.vectorstores.atlas import AtlasDB
from langchain.vectorstores.base import VectorStore
from langchain.vectorstores.chroma import Chroma
from langchain.vectorstores.deeplake import DeepLake
from langchain.vectorstores.elastic_vector_search import ElasticVectorSearch
from langchain.vectorstores.faiss import FAISS
from langchain.vectorstores.milvus import Milvus
from langchain.vectorstores.opensearch_vector_search import OpenSearchVectorSearch
from langchain.vectorstores.pinecone import Pinecone
from langchain.vectorstores.qdrant import Qdrant
from langchain.vectorstores.weaviate import Weaviate

vectorstore_type_to_cls_dict: Dict[str, Type[VectorStore]] = {
    "ElasticVectorSearch": ElasticVectorSearch,
    "FAISS": FAISS,
    "Pinecone": Pinecone,
    "Weaviate": Weaviate,
    "Qdrant": Qdrant,
    "Milvus": Milvus,
    "Chroma": Chroma,
    "OpenSearchVectorSearch": OpenSearchVectorSearch,
    "AtlasDB": AtlasDB,
    "DeepLake": DeepLake,
}




## Memory

from langchain.memory import ConversationBufferMemory
# from langchain.memory.chat_memory import ChatMessageHistory
# from langchain.memory.combined import CombinedMemory
# from langchain.memory.entity import ConversationEntityMemory
# from langchain.memory.kg import ConversationKGMemory
# from langchain.memory.readonly import ReadOnlySharedMemory
# from langchain.memory.simple import SimpleMemory
# from langchain.memory.summary import ConversationSummaryMemory
# from langchain.memory.summary_buffer import ConversationSummaryBufferMemory

memory_type_to_cls_dict: dict[str, Any] = {
    # "CombinedMemory": CombinedMemory,
    # "ConversationBufferWindowMemory": ConversationBufferWindowMemory,
    "ConversationBufferMemory": ConversationBufferMemory,
    # "SimpleMemory": SimpleMemory,
    # "ConversationSummaryBufferMemory": ConversationSummaryBufferMemory,
    # "ConversationKGMemory": ConversationKGMemory,
    # "ConversationEntityMemory": ConversationEntityMemory,
    # "ConversationSummaryMemory": ConversationSummaryMemory,
    # "ChatMessageHistory": ChatMessageHistory,
    # "ConversationStringBufferMemory": ConversationStringBufferMemory,
    # "ReadOnlySharedMemory": ReadOnlySharedMemory,
}


## Chain
# from langchain.chains.loading import type_to_loader_dict
# from langchain.chains.conversation.base import ConversationChain

# chain_type_to_cls_dict = type_to_loader_dict
# chain_type_to_cls_dict["conversation_chain"] = ConversationChain
