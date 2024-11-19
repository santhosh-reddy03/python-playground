from config import get_config
from sqlalchemy import create_engine
from models.users import Base
app_config = get_config()

engine = create_engine(app_config.database_uri, echo=True)

Base.metadata.create_all(engine)
