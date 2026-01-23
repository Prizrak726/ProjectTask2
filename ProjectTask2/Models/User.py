from Models.Base import *

class User(BaseModel):
    '''
    Данный класс описывает таблицу в БД с игровыми объектами
    '''
    id  = PrimaryKeyField()
    name = CharField() # название предмета
    email = CharField(unique=True) # редкость
    age = IntegerField() # игрок
    registration_date = DateField() # дата регистрации


if __name__ == "__main__":
    mysql_db.create_tables([User])

