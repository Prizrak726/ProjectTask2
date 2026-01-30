from tkinter import *
from tkinter import ttk, messagebox


class SimpleSearchView:
    """Упрощенный класс для отображения результатов поиска"""

    @staticmethod
    def show_results(parent, results, search_string):
        """Показать результаты поиска"""
        if not results:
            messagebox.showinfo("Результаты поиска",
                                f"Пользователи по запросу '{search_string}' не найдены")
            return

        # Создаем окно для результатов
        window = Toplevel(parent)
        window.title(f"Результаты поиска: {search_string}")
        window.geometry("1000x600")

        # Создаем интерфейс
        SimpleSearchView._create_interface(window, results, search_string)

        return window

    @staticmethod
    def _create_interface(window, results, search_string):
        """Создание интерфейса окна поиска"""
        # Главный фрейм
        main_frame = ttk.Frame(window)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Заголовок
        title_label = ttk.Label(main_frame,
                                text=f"Результаты поиска: '{search_string}'",
                                font=("Arial", 14, "bold"))
        title_label.pack(pady=(0, 20))

        # Информация о количестве
        count_label = ttk.Label(main_frame,
                                text=f"Найдено пользователей: {len(results)}",
                                font=("Arial", 10))
        count_label.pack(pady=(0, 10))

        # Фрейм для таблицы
        table_frame = ttk.Frame(main_frame)
        table_frame.pack(fill=BOTH, expand=True)

        # Создание таблицы
        columns = ('id', 'name', 'email', 'age', 'registration_date')
        table = ttk.Treeview(table_frame,
                             columns=columns,
                             show='headings',
                             height=10)

        # Настраиваем заголовки
        headers = {
            'id': '№',
            'name': 'Имя',
            'email': 'Почта',
            'age': 'Возраст',
            'registration_date': 'Дата регистрации'
        }

        for col in columns:
            table.heading(col, text=headers[col])
            table.column(col, width=120, anchor='center')

        # Заполняем таблицу
        for result in results:
            if isinstance(result, dict):
                table.insert("", END, values=(
                    result.get('id', ''),
                    result.get('name', ''),
                    result.get('email', ''),
                    result.get('age', ''),
                    result.get('registration_date', '')
                ))
            elif isinstance(result, (tuple, list)):
                if len(result) >= 5:
                    table.insert("", END, values=result[:5])
                else:
                    # Дополняем недостающие значения
                    values = list(result)
                    while len(values) < 5:
                        values.append('')
                    table.insert("", END, values=values)

        # Скроллбар
        scrollbar = ttk.Scrollbar(table_frame,
                                  orient=VERTICAL,
                                  command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=RIGHT, fill=Y)
        table.pack(side=LEFT, fill=BOTH, expand=True)

        # Кнопка закрытия
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)

        button_close = ttk.Button(button_frame,
                                  text='Закрыть',
                                  command=window.destroy)
        button_close.pack()


# Для совместимости со старым кодом
class SearchView:
    """Обертка для совместимости"""

    def __init__(self, master, search_string):
        self.master = master
        self.search_string = search_string

    def show(self):
        """Показать результаты (пустой метод для совместимости)"""
        pass



if __name__ == "__main__":
    # # Тестовые данные
    # test_results = [
    #     {'id': 1, 'name': 'Иван Иванов', 'email': 'ivan@example.com', 'age': 25, 'registration_date': '2023-01-15'},
    #     {'id': 2, 'name': 'Мария Петрова', 'email': 'maria@example.com', 'age': 30, 'registration_date': '2023-02-20'},
    #     {'id': 3, 'name': 'Алексей Сидоров', 'email': 'alexey@example.com', 'age': 35,
    #      'registration_date': '2023-03-10'},
    # ]

    root = Tk()
    root.withdraw()  # Скрываем главное окно
    #
    # # Показываем результаты
    # SimpleSearchView.show_results(root, test_results, "тест")

    root.mainloop()