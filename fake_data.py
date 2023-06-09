from faker import Faker
from random import choice, randint
from datetime import datetime, timedelta
from session import Session
from models import Category, FilmCategory, Payment, Address, Country, City, \
    Film, Language, Actor, FilmActor, Inventory, Rental, Customer, Staff, Store

session = Session()
fake = Faker()
movie_types = [
    'Action',
    'Comedy',
    'Drama',
    'Horror',
    'Sci-Fi',
    'Romance',
    'Thriller',
    'Adventure',
    'Fantasy',
    'Mystery'
]
languages = [
    'English',
    'Spanish',
    'French',
    'German',
    'Italian',
    'Japanese',
    'Chinese',
    'Russian',
    'Korean',
    'Portuguese'
]

countries = [
    'United States',
    'Canada',
    'United Kingdom',
    'Australia',
    'Germany',
    'France',
    'Japan',
    'Brazil',
    'India',
    'China'
]

cities = [
    'New York',
    'London',
    'Paris',
    'Tokyo',
    'Sydney',
    'Rome',
    'Berlin',
    'Moscow',
    'Toronto',
    'Dubai',
    'Mumbai',
    'Barcelona',
    'Amsterdam',
    'Singapore',
    'Los Angeles',
    'Istanbul',
    'Rio de Janeiro',
    'Cairo',
    'Seoul',
    'Bangkok'
]


def main():
    generate_categories()
    generate_languages()
    generate_films()
    generate_film_categories()
    generate_actors()
    generate_film_actors()
    generate_inventories()
    generate_countries()
    generate_cities()
    generate_addresses()
    generate_customers()
    generate_store()
    generate_staff()
    generate_rentals()
    generate_payments()


def generate_categories():
    for category_name in movie_types:
        actor = Category(
            name=category_name,
        )
        session.add(actor)
    session.commit()


def generate_film_categories():
    movie_id = 0
    for _ in range(200):
        movie_id += 1
        film_category = FilmCategory(
            film_id=movie_id,
            category_id=randint(1, 10)
        )
        session.add(film_category)
    session.commit()


def generate_films():
    for _ in range(200):
        film = Film(
            title=fake.word(),
            description=fake.text(max_nb_chars=255),
            release_year=randint(1900, 2023),
            language_id=randint(1, 10),
            rental_duration=randint(1, 7),
            rental_rate=round(randint(1, 20) + choice([0.99, 0.49, 0.39]), 2),
            length=randint(60, 240),
            replacement_cost=round(randint(10, 50) + choice([0.99, 0.49, 0.39]), 2),
            rating=round(randint(1, 5) + choice([0.5, 0.25, 0.75]), 1),
            special_features=fake.text(max_nb_chars=255),
            full_text=fake.text(max_nb_chars=300)
        )
        session.add(film)
    session.commit()


def generate_languages():
    for language in languages:
        language_obj = Language(
            name=language,
        )
        session.add(language_obj)
    session.commit()


def generate_film_actors():
    cat_id = 0
    for _ in range(200):
        cat_id += 1
        record = FilmActor(
            film_id=cat_id,
        )

        session.add(record)
    session.commit()


def generate_actors():
    for _ in range(200):
        actor = Actor(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(actor)
    session.commit()


def generate_inventories():
    for _ in range(1000):
        inventory = Inventory(
            film_id=randint(1, 200),
            store_id=randint(1, 3)
        )
        session.add(inventory)
    session.commit()


def generate_customers():
    ad_id = 0
    for _ in range(100):
        ad_id += 1
        customer = Customer(
            store_id=randint(1, 3),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            address_id=ad_id,
            is_active=True,
            create_date=fake.date_this_decade(),
            rental_id=randint(1, 1000)
        )
        session.add(customer)
    session.commit()


def generate_countries():
    for country in countries:
        ctr = Country(
            country=country
        )
        session.add(ctr)
    session.commit()


def generate_cities():
    for city in cities:
        cty = City(
            city=city,
            country_id=randint(1, 10)
        )
        session.add(cty)
    session.commit()


def generate_addresses():
    for _ in range(100):
        address = Address(
            address=fake.address(),
            address2=fake.secondary_address(),
            district=fake.state(),
            city_id=randint(1, 20),
            postal_code=randint(1, 10000),
            phone=randint(111111111, 999999999)
        )
        session.add(address)
    session.commit()


def generate_rentals():
    rental_date = datetime.now() - timedelta(days=365)
    for _ in range(500):
        rental = Rental(
            inventory_id=randint(1, 1000),
            rental_date=rental_date,
            customer_id=randint(1, 100),
            return_date=rental_date + timedelta(days=randint(1, 7)),
            staff_id=randint(1, 30)
        )
        session.add(rental)
        rental_date += timedelta(days=randint(1, 7))
    session.commit()


def generate_payments():
    for _ in range(500):
        payment = Payment(
            customer_id=randint(2, 100),
            staff_id=randint(1, 30),
            rental_id=randint(1, 500),
            amount=randint(5, 100) + choice([0.99, 0.49, 0.39]),
            payment_date=fake.date_this_decade()
        )
        session.add(payment)
    session.commit()


def generate_staff():
    for _ in range(30):
        staff = Staff(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address_id=randint(1, 100),
            store_id=randint(1, 3),
            active=True,
            username=fake.name(),
            password=fake.password(),
            picture_id=randint(1, 10)

        )
        session.add(staff)
    session.commit()


def generate_store():
    for _ in range(3):
        store = Store(
            manager_staff_id=randint(1, 3),
            address_id=randint(1, 100),
        )
        session.add(store)
    session.commit()

if __name__ == '__main__':
    main()
