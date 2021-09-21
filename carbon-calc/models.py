from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class CalculatorData(Model):
    id = Column(Integer, primary_key=True)
    team = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name