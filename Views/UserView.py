from tkinter import *
from tkinter import ttk, messagebox
from Controllers.UserControllers import UserController


class UserView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Система управления пользователями")
        self.geometry("1200x800")

        # Фрейм Добавить пользователя
        self.add_frame = ttk.Frame(self,
                                   borderwidth=1,
                                   relief=SOLID,
                                   padding=[8, 10])
        self.add_frame.pack(
            anchor=CENTER,
            fill=X,
            padx=10,
            pady=10
        )

        # Фрейм заголовка "Добавить Пользователя"
        self.add_title_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,
                                         borderwidth=1,
                                         padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER,
                                  fill=X,
                                  padx=10,
                                  pady=10)
        self.add_title = ttk.Label(self.add_title_frame, text="Добавить Пользователя")
        self.add_title.pack()

        # Фрейм ввода данных пользователя
        self.add_input_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,
                                         borderwidth=1,
                                         padding=[8, 10])
        self.add_input_frame.pack(fill=X,
                                  padx=10,
                                  pady=10)

        # Настройка grid
        for i in range(6):
            self.add_input_frame.grid_columnconfigure(i, weight=1)

        # Метки полей ввода
        labels_texts = ["Имя", "Почта", "Возраст", "Дата регистрации"]
        for i, text in enumerate(labels_texts):
            label = ttk.Label(self.add_input_frame, text=text)
            label.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)

        # Поля ввода
        self.add_name = ttk.Entry(self.add_input_frame)
        self.add_name.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.add_email = ttk.Entry(self.add_input_frame)
        self.add_email.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.add_age = ttk.Entry(self.add_input_frame)
        self.add_age.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.add_registration_date = ttk.Entry(self.add_input_frame)
        self.add_registration_date.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

        # Кнопка "Добавить"
        self.add_but = ttk.Button(self.add_input_frame, text="Добавить",
                                  padding=[30, 5], command=self.add_date)
        self.add_but.grid(row=1, column=5, sticky="nsew", padx=5, pady=5)

        # Кнопка "Обновить"
        self.refresh_but = ttk.Button(self.add_input_frame, text="Обновить",
                                      padding=[30, 5], command=self.table)
        self.refresh_but.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)

        # Фрейм для удаления пользователя (располагаем под фреймом добавления)
        self.delete_frame = ttk.Frame(self,
                                      borderwidth=1,
                                      relief=SOLID,
                                      padding=[8, 10])
        self.delete_frame.pack(fill=X, padx=10, pady=(0, 10))

        # Заголовок фрейма удаления
        delete_title = ttk.Label(self.delete_frame, text="Управление пользователями",
                                 font=("Arial", 10, "bold"))
        delete_title.pack(anchor=W, pady=(0, 10))

        # Фрейм для ввода ID и кнопок управления
        delete_input_frame = ttk.Frame(self.delete_frame)
        delete_input_frame.pack(fill=X)

        # Метка для поля ввода ID
        delete_label = ttk.Label(delete_input_frame, text="ID пользователя:")
        delete_label.pack(side=LEFT, padx=(0, 10))

        # Поле ввода для ID
        self.delete_id_entry = ttk.Entry(delete_input_frame, width=15)
        self.delete_id_entry.pack(side=LEFT, padx=(0, 20))

        # Кнопка "Удалить по ID"
        self.delete_button = ttk.Button(delete_input_frame,
                                        text="Удалить",
                                        command=self.delete_user_by_id,
                                        style="Danger.TButton")
        self.delete_button.pack(side=LEFT, padx=(0, 10))

        # Кнопка "Найти по ID" (дополнительная функция)
        self.find_by_id_button = ttk.Button(delete_input_frame,
                                            text="Найти по ID",
                                            command=self.find_user_by_id)
        self.find_by_id_button.pack(side=LEFT)

        # Создаем стиль для красной кнопки
        self.style = ttk.Style()
        self.style.configure("Danger.TButton",
                             foreground="white",
                             background="#dc3545",
                             font=("Arial", 10, "bold"))

        # При наведении меняем цвет
        self.style.map("Danger.TButton",
                       background=[('active', '#c82333')])

        # Фрейм для кнопки "Показать всех"
        self.show_all_frame = ttk.Frame(self,
                                        relief=SOLID,
                                        borderwidth=1,
                                        padding=[8, 10])
        self.show_all_frame.pack(fill=X, padx=10, pady=(0, 10))

        # Кнопка "Показать всех"
        self.show_all_button = ttk.Button(self.show_all_frame,
                                          text="Показать всех пользователей",
                                          padding=[30, 10],
                                          command=self.show_table)
        self.show_all_button.pack(expand=True, fill=X)

        # Фрейм для таблицы
        self.table_frame = ttk.Frame(
            self,
            relief="raised",
            borderwidth=3,
            padding=[5]
        )

        self.table_visible = False

        # Фрейм поиска
        self.search_frame = ttk.Frame(
            self,
            relief=SOLID,
            borderwidth=1,
            padding=[8, 10]
        )
        self.search_frame.pack(fill=X, padx=10, pady=10)

        # Элементы поиска
        self.label_search = ttk.Label(self.search_frame, text="Найти пользователя по имени или email")
        self.label_search.pack(anchor=W, pady=(0, 5))

        search_input_frame = ttk.Frame(self.search_frame)
        search_input_frame.pack(fill=X)

        self.text_search = ttk.Entry(search_input_frame, width=50)
        self.text_search.pack(side=LEFT, padx=(0, 10))

        self.button_search = ttk.Button(search_input_frame, text="Найти",
                                        command=self.search)
        self.button_search.pack(side=LEFT)

        # Загружаем всех пользователей при запуске для поиска
        self.all_users = []
        self.load_all_users()

    def delete_user_by_id(self):
        """Удаление пользователя по ID с использованием UserController.delete()"""
        # Получаем ID из поля ввода
        user_id = self.delete_id_entry.get().strip()

        # Проверяем, что ID не пустой
        if not user_id:
            messagebox.showwarning("Предупреждение", "Введите ID пользователя для удаления")
            return

        # Проверяем, что ID - число
        try:
            user_id_int = int(user_id)
            if user_id_int <= 0:
                messagebox.showwarning("Предупреждение", "ID должен быть положительным числом")
                return
        except ValueError:
            messagebox.showwarning("Предупреждение", "ID должен быть числом")
            return

        # Подтверждение удаления
        confirm = messagebox.askyesno(
            "Подтверждение удаления",
            f"Вы уверены, что хотите удалить пользователя с ID {user_id}?\n"
            "Это действие нельзя отменить."
        )

        if not confirm:
            return

        try:
            # Используем метод delete из UserController
            # Метод возвращает None (pass в реализации), но мы можем проверить, была ли ошибка
            UserController.delete(user_id_int)

            # Если выполнение дошло до этой точки без ошибок, считаем удаление успешным
            messagebox.showinfo("Успех", f"Пользователь с ID {user_id} успешно удален")

            # Обновляем список пользователей
            self.load_all_users()

            # Обновляем таблицу, если она видна
            if self.table_visible:
                self.table()

            # Очищаем поле ввода ID
            self.delete_id_entry.delete(0, END)

            # Показываем сообщение в консоли
            print(f"Пользователь с ID {user_id} удален")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при удалении пользователя: {str(e)}")
            print(f"Ошибка при удалении пользователя: {e}")

    def find_user_by_id(self):
        """Поиск пользователя по ID и отображение информации"""
        user_id = self.delete_id_entry.get().strip()

        if not user_id:
            messagebox.showwarning("Предупреждение", "Введите ID пользователя для поиска")
            return

        try:
            user_id_int = int(user_id)
            if user_id_int <= 0:
                messagebox.showwarning("Предупреждение", "ID должен быть положительным числом")
                return
        except ValueError:
            messagebox.showwarning("Предупреждение", "ID должен быть числом")
            return

        # Ищем пользователя в списке
        found_user = None
        for user in self.all_users:
            user_data = self.extract_user_data(user)
            if user_data and str(user_data.get('id', '')) == user_id:
                found_user = user_data
                break

        if found_user:
            # Показываем информацию о пользователе
            user_info = (
                f"ID: {found_user.get('id', '')}\n"
                f"Имя: {found_user.get('name', '')}\n"
                f"Email: {found_user.get('email', '')}\n"
                f"Возраст: {found_user.get('age', '')}\n"
                f"Дата регистрации: {found_user.get('registration_date', '')}"
            )

            messagebox.showinfo(f"Пользователь ID: {user_id}", user_info)
        else:
            messagebox.showinfo("Результат поиска", f"Пользователь с ID {user_id} не найден")

    def load_all_users(self):
        """Загрузка всех пользователей для локального поиска"""
        try:
            self.all_users = UserController.get()
            print(f"Загружено пользователей: {len(self.all_users)}")
        except Exception as e:
            print(f"Ошибка при загрузке пользователей: {e}")
            self.all_users = []

    def search(self):
        """Метод для поиска пользователя по имени или email"""
        search_string = self.text_search.get().strip()

        if not search_string:
            messagebox.showwarning("Предупреждение", "Введите имя или email для поиска")
            return

        try:
            # Ищем пользователей локально
            search_results = []

            for user in self.all_users:
                # Извлекаем данные пользователя
                user_data = self.extract_user_data(user)

                if user_data:
                    name = user_data.get('name', '').lower()
                    email = user_data.get('email', '').lower()

                    # Поиск по частичному совпадению
                    if (search_string.lower() in name) or (search_string.lower() in email):
                        search_results.append(user_data)

            print(f"Найдено результатов: {len(search_results)}")

            if not search_results:
                messagebox.showinfo("Результаты поиска",
                                    f"Пользователи по запросу '{search_string}' не найдены")
                return

            # Создаем окно поиска
            search_window = Toplevel(self)
            search_window.title(f"Результаты поиска: {search_string}")
            search_window.geometry("1280x800")

            # Создаем интерфейс для отображения результатов
            self.create_search_results_window(search_window, search_results, search_string)

            # Настраиваем обработчик закрытия окна
            def on_closing():
                search_window.destroy()
                if self.table_visible:
                    self.table()  # Обновляем таблицу

            search_window.protocol("WM_DELETE_WINDOW", on_closing)
            search_window.focus_set()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при поиске: {str(e)}")
            print(f"Ошибка при поиске: {e}")

    def create_search_results_window(self, parent, results, search_string):
        """Создание окна с результатами поиска"""
        # Главный фрейм
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Заголовок
        title_label = ttk.Label(main_frame,
                                text=f"Результаты поиска: '{search_string}'",
                                font=("Arial", 14, "bold"))
        title_label.pack(pady=(0, 20))

        # Фрейм для таблицы
        table_frame = ttk.Frame(main_frame)
        table_frame.pack(fill=BOTH, expand=True)

        # Создание таблицы
        columns = ('id', 'name', 'email', 'age', 'registration_date')
        table = ttk.Treeview(table_frame,
                             columns=columns,
                             show='headings',
                             height=15)

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
            table.column(col, width=150, minwidth=100, anchor='center')

        # Заполняем таблицу данными
        for user_data in results:
            table.insert("", END, values=(
                user_data.get('id', ''),
                user_data.get('name', ''),
                user_data.get('email', ''),
                user_data.get('age', ''),
                user_data.get('registration_date', '')
            ))

        # Скроллбары
        scrollbar_y = ttk.Scrollbar(table_frame,
                                    orient=VERTICAL,
                                    command=table.yview)
        table.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = ttk.Scrollbar(table_frame,
                                    orient=HORIZONTAL,
                                    command=table.xview)
        table.configure(xscrollcommand=scrollbar_x.set)

        # Упаковка элементов таблицы
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        table.pack(side=LEFT, fill=BOTH, expand=True)

        # Фрейм для кнопок
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)

        # Информация о количестве результатов
        count_label = ttk.Label(button_frame,
                                text=f"Найдено пользователей: {len(results)}",
                                font=("Arial", 10, "bold"))
        count_label.pack(pady=(0, 10))

        # Кнопка закрытия
        button_close = ttk.Button(button_frame,
                                  text='Закрыть',
                                  command=parent.destroy)
        button_close.pack()

    def extract_user_data(self, user):
        """Извлечение данных пользователя из разных форматов"""
        try:
            if isinstance(user, dict):
                return {
                    'id': user.get('id', user.get('ID', user.get('Id', ''))),
                    'name': user.get('name', user.get('Name', user.get('NAME', ''))),
                    'email': user.get('email', user.get('Email', user.get('EMAIL', ''))),
                    'age': user.get('age', user.get('Age', user.get('AGE', ''))),
                    'registration_date': user.get('registration_date',
                                                  user.get('registrationDate',
                                                           user.get('REGISTRATION_DATE', '')))
                }
            elif hasattr(user, '__dict__'):
                return {
                    'id': getattr(user, 'id', getattr(user, 'ID', getattr(user, 'Id', ''))),
                    'name': getattr(user, 'name', getattr(user, 'Name', getattr(user, 'NAME', ''))),
                    'email': getattr(user, 'email', getattr(user, 'Email', getattr(user, 'EMAIL', ''))),
                    'age': getattr(user, 'age', getattr(user, 'Age', getattr(user, 'AGE', ''))),
                    'registration_date': getattr(user, 'registration_date',
                                                 getattr(user, 'registrationDate',
                                                         getattr(user, 'registration_date', '')))
                }
            elif hasattr(user, 'id'):
                return {
                    'id': getattr(user, 'id', ''),
                    'name': getattr(user, 'name', ''),
                    'email': getattr(user, 'email', ''),
                    'age': getattr(user, 'age', ''),
                    'registration_date': getattr(user, 'registration_date', '')
                }
            elif isinstance(user, (tuple, list)) and len(user) >= 5:
                return {
                    'id': user[0] if len(user) > 0 else '',
                    'name': user[1] if len(user) > 1 else '',
                    'email': user[2] if len(user) > 2 else '',
                    'age': user[3] if len(user) > 3 else '',
                    'registration_date': user[4] if len(user) > 4 else ''
                }
            else:
                print(f"Неизвестный формат пользователя: {type(user)}")
                return None

        except Exception as e:
            print(f"Ошибка при извлечении данных пользователя: {e}")
            return None

    def show_table(self):
        """Метод для отображения/скрытия таблицы"""
        if not self.table_visible:
            self.table_frame.pack(anchor=CENTER, fill=BOTH, expand=True, padx=10, pady=10)

            if not hasattr(self, 'table_data'):
                self.create_table()

            self.table()
            self.show_all_button.config(text="Скрыть таблицу")
            self.table_visible = True
        else:
            self.table_frame.pack_forget()
            self.show_all_button.config(text="Показать всех пользователей")
            self.table_visible = False

    def create_table(self):
        """Создание таблицы"""
        self.columns = ('id', "name", 'email', 'age', 'registration_date')
        self.table_data = ttk.Treeview(self.table_frame,
                                       columns=self.columns,
                                       show='headings',
                                       height=15)

        for col in self.columns:
            text = ""
            if col == 'id':
                text = "№"
            elif col == 'name':
                text = 'Имя'
            elif col == 'email':
                text = 'Почта'
            elif col == 'age':
                text = 'Возраст'
            elif col == 'registration_date':
                text = 'Дата регистрации'
            self.table_data.heading(col, text=text)
            self.table_data.column(col, width=150, minwidth=100, anchor='center')

        # Добавляем контекстное меню для таблицы
        self.table_data.bind('<Button-3>', self.show_context_menu)

        scrollbar_y = ttk.Scrollbar(self.table_frame,
                                    orient=VERTICAL,
                                    command=self.table_data.yview)
        self.table_data.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = ttk.Scrollbar(self.table_frame,
                                    orient=HORIZONTAL,
                                    command=self.table_data.xview)
        self.table_data.configure(xscrollcommand=scrollbar_x.set)

        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        self.table_data.pack(side=LEFT, fill=BOTH, expand=True)

    def show_context_menu(self, event):
        """Показать контекстное меню для удаления записи из таблицы"""
        # Определяем, какая строка выбрана
        item = self.table_data.identify_row(event.y)
        if item:
            # Получаем данные из выбранной строки
            item_data = self.table_data.item(item, 'values')
            if item_data:
                # Создаем контекстное меню
                context_menu = Menu(self, tearoff=0)
                context_menu.add_command(
                    label=f"Удалить пользователя ID: {item_data[0]}",
                    command=lambda: self.delete_from_context_menu(item_data[0], item)
                )

                # Показываем меню
                context_menu.post(event.x_root, event.y_root)

    def delete_from_context_menu(self, user_id, item):
        """Удалить пользователя из контекстного меню"""
        try:
            user_id_int = int(user_id)

            # Подтверждение удаления
            confirm = messagebox.askyesno(
                "Подтверждение удаления",
                f"Вы уверены, что хотите удалить пользователя с ID {user_id}?\n"
                f"Имя: {self.table_data.item(item, 'values')[1]}\n"
                "Это действие нельзя отменить."
            )

            if not confirm:
                return

            # Используем метод delete из UserController
            UserController.delete(user_id_int)

            # Удаляем строку из таблицы
            self.table_data.delete(item)

            # Обновляем список пользователей
            self.load_all_users()

            messagebox.showinfo("Успех", f"Пользователь с ID {user_id} успешно удален")
            print(f"Пользователь с ID {user_id} удален через контекстное меню")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при удалении: {str(e)}")

    def table(self):
        """Загрузка данных в таблицу"""
        if not hasattr(self, 'table_data'):
            return

        # Очищаем таблицу
        for item in self.table_data.get_children():
            self.table_data.delete(item)

        try:
            # Обновляем список пользователей
            self.load_all_users()

            # Заполняем таблицу
            for user in self.all_users:
                user_data = self.extract_user_data(user)
                if user_data:
                    self.table_data.insert("", END, values=(
                        user_data.get('id', ''),
                        user_data.get('name', ''),
                        user_data.get('email', ''),
                        user_data.get('age', ''),
                        user_data.get('registration_date', '')
                    ))

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при загрузке данных: {str(e)}")
            print(f"Ошибка при загрузке данных: {e}")

    def add_date(self):
        """Добавление нового пользователя"""
        name = self.add_name.get().strip()
        email = self.add_email.get().strip()
        age = self.add_age.get().strip()
        registration_date = self.add_registration_date.get().strip()

        if not all([name, email, age, registration_date]):
            messagebox.showwarning("Предупреждение", "Все поля должны быть заполнены!")
            return

        try:
            age_int = int(age)
            if age_int <= 0 or age_int > 120:
                messagebox.showwarning("Предупреждение", "Возраст должен быть от 1 до 120 лет")
                return
        except ValueError:
            messagebox.showwarning("Предупреждение", "Возраст должен быть числом")
            return

        try:
            result = UserController.add(name, email, age, registration_date)

            if result:
                messagebox.showinfo("Успех", "Пользователь успешно добавлен")
                # Обновляем список пользователей
                self.load_all_users()
                # Обновляем таблицу, если она видна
                if self.table_visible:
                    self.table()
                self.clear()
            else:
                messagebox.showerror("Ошибка", "Не удалось добавить пользователя")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при добавлении пользователя: {str(e)}")

    def clear(self):
        """Очистка полей ввода"""
        self.add_name.delete(0, END)
        self.add_email.delete(0, END)
        self.add_age.delete(0, END)
        self.add_registration_date.delete(0, END)


if __name__ == "__main__":
    window = UserView()
    window.mainloop()