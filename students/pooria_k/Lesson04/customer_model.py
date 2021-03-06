"""
customer database, to store required data for each customer
"""
import peewee

DB = peewee.SqliteDatabase(None)
# db.execute_sql('PRAGMA foreign_keys = ON;')

class BaseModel(peewee.Model):
    """Create a base model class which specifies our database."""
    class Meta:
        """Create a base model class which specifies our database."""
        database = DB

class Customer(BaseModel):
    """
    This class defines Customer, which maintains details of
    a customer
     """
    name = peewee.CharField(max_length=20, unique=True)
    lastname = peewee.CharField(max_length=30)
    home_address = peewee.CharField(max_length=50)
    phone_number = peewee.IntegerField()
    email_address = peewee.CharField(max_length=40)
    status = peewee.BooleanField()
    credit_limit = peewee.DecimalField()
