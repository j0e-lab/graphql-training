from . import user
from ..config.database import meta, engine

meta.create_all(engine)
