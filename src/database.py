from databases import Database
from sqlalchemy import (
    Boolean,
    Column,
    Float,
    DateTime,
    ForeignKey,
    Identity,
    Integer,
    LargeBinary,
    MetaData,
    String,
    Table,
    create_engine,
    func,
    
)
from urllib.parse import quote_plus
from src.config import settings
from src.constants import DB_NAMING_CONVENTION

# DATABASE_URL = settings.DATABASE_URL

# engine = create_engine(DATABASE_URL)
# metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)

# database = Database(DATABASE_URL, force_rollback=settings.ENVIRONMENT.is_testing)
    
# withdraw_request = Table(
#     "withdraw_request",
#     metadata,
#     Column("id", Integer, Identity(), primary_key=True),
#     Column("created_at", DateTime, server_default=func.now(), nullable=False),
#     Column("updated_at", DateTime, server_default=func.now(), nullable=False),
#     Column("order_id", Integer, nullable=False),
#     Column("cypto_code", String, nullable=False),
#     Column("to_address", String, nullable=False),
#     Column("amount", Float, nullable=False),
#     Column("signature", String, nullable=False),
#     Column("fireblock_withdraw_id", String, nullable=False),
#     Column("status", String, nullable=False)
# )

# crypto_currency = Table(
#     "crypto_currency",
#     metadata,
#     Column("id", Integer, Identity(), primary_key=True),
#     Column("code", String, nullable=False),
#     Column("created_at", DateTime, server_default=func.now(), nullable=False),
#     Column("enable_withdraw", Boolean, nullable=False),
#     Column("max_withdraw", Float, nullable=False),
#     Column("min_withdraw", Float, nullable=False),
#     Column("name", String, nullable=False),
#     Column("network_fee", Float, nullable=False),
#     Column("status", Float,nullable=False)
# )