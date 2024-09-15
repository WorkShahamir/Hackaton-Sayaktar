import flet as ft

class Listing:
    def __init__(self, title, description, price, contact_info):
        self.title = title
        self.description = description
        self.price = price
        self.contact_info = contact_info

class Roommate:
    def __init__(self, name, age, gender, contact_info):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info

class RentApp:
    def __init__(self):
        self.listings = []
        self.roommates = []

    def add_listing(self, title, description, price, contact_info):
        listing = Listing(title, description, price, contact_info)
        self.listings.append(listing)

    def add_roommate(self, name, age, gender, contact_info):
        roommate = Roommate(name, age, gender, contact_info)
        self.roommates.append(roommate)

def main(page: ft.Page):
    app = RentApp()

    # Функции для добавления объявлений и сожителей
    def add_listing(e):
        app.add_listing(title.value, description.value, price.value, contact_info.value)
        update_listing_view()
        title.value = description.value = price.value = contact_info.value = ""
        page.update()

    def add_roommate(e):
        app.add_roommate(name.value, age.value, gender.value, contact_info_r.value)
        update_roommate_view()
        name.value = age.value = gender.value = contact_info_r.value = ""
        page.update()

    def update_listing_view():
        listings_container.controls.clear()
        for listing in app.listings:
            listings_container.controls.append(
                ft.ListTile(
                    title=ft.Text(listing.title),
                    subtitle=ft.Text(f"{listing.description}\nЦена: {listing.price}\nКонтакты: {listing.contact_info}"),
                )
            )
        page.update()

    def update_roommate_view():
        roommates_container.controls.clear()
        for roommate in app.roommates:
            roommates_container.controls.append(
                ft.ListTile(
                    title=ft.Text(f"{roommate.name}, {roommate.age} лет, {roommate.gender}"),
                    subtitle=ft.Text(f"Контакты: {roommate.contact_info}"),
                )
            )
        page.update()

    # Элементы интерфейса для объявлений
    title = ft.TextField(label="Заголовок")
    description = ft.TextField(label="Описание")
    price = ft.TextField(label="Цена")
    contact_info = ft.TextField(label="Контактная информация")
    add_listing_button = ft.ElevatedButton(text="Добавить объявление", on_click=add_listing)

    # Элементы интерфейса для сожителей
    name = ft.TextField(label="Имя")
    age = ft.TextField(label="Возраст")
    gender = ft.TextField(label="Пол")
    contact_info_r = ft.TextField(label="Контактная информация")
    add_roommate_button = ft.ElevatedButton(text="Добавить сожителя", on_click=add_roommate)

    listings_container = ft.Column()
    roommates_container = ft.Column()

    # Добавление элементов на страницу
    page.add(
        ft.Text("Объявления о квартирах", size=20),
        title, description, price, contact_info, add_listing_button, listings_container,
        ft.Divider(),
        ft.Text("Сожители", size=20),
        name, age, gender, contact_info_r, add_roommate_button, roommates_container,
    )

# Запуск приложения
ft.app(target=main)
