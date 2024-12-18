# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões

# Imports de terceiros
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

# Imports locais

# =================================================================================================================================================================
# Classes
# =================================================================================================================================================================

class Base(DeclarativeBase):
    pass

# =================================================================================================================================================================
# Variáveis
# =================================================================================================================================================================

db = SQLAlchemy(model_class=Base)