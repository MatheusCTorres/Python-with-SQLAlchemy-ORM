from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker
import sys


engine = create_engine('mysql+mysqlconnector://root:@localhost/classicmodels')

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Customer(Base):
    __tablename__ = "customers"
    customerNumber = Column(Integer, primary_key = True)
    customerName = Column(String(50))
    contactLastName = Column(String(50))
    contactFirstName = Column(String(50))
    phone = Column(String(50))
    addressLine1 = Column(String(50))
    addressLine2 = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    postalCode = Column(String(15))
    country = Column(String(50))

    salesRepEmployeeNumber = Column(Integer)
    creditLimit = Column(Numeric(10, 2))


session = Session()

result = session.query(Customer.customerName,
                       Customer.phone,
                       Customer.postalCode,
                       Customer.country).filter(Customer.customerName == sys.argv[1])

for row in result:
  print(row)