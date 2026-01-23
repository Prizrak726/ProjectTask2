from Models.User import *

class UserController:
    '''
    методы:
        добавить,
        показать всех,
        найти по email,
        удалить

    '''
    @classmethod
    def add(cls,name,email,age,registration_date):
        # добавить предмет в Таблицу


        try:
            User.create(
            name = name,
            email = email,
            age = age,
            registration_date = registration_date
            )
        except:
            print("Ошибка создания пользователя")
    @classmethod
    def get(cls):
        # Выводит список записей из таблицы БД
        return User.select()

    @classmethod
    def delete(cls, id):
        pass
        # Обновить запись по id
        User.delete().where(User.id == id).execute()
    @classmethod
    def search_email(cls,email):
        pass
        # Метод выводит список записей, если встречается характеристика stats
        list = [] # создание пустого списка
        query = User.select().where(User.email == email) # переменной передаём список записей у которых в поле email есть email из аргумента метода
        for item in query:
            list.append(item.name)
        return list


if __name__ == "__main__":
    pass
