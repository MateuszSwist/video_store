from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Float, func, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Film(Base):
    __tablename__ = 'film'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    release_year = Column(Integer, nullable=False)
    language_id = Column(Integer, ForeignKey("language.id"), nullable=False)
    rental_duration = Column(Integer, nullable=False)
    rental_rate = Column(Float, nullable=False)
    length = Column(Integer)
    replacement_cost = Column(Float)
    rating = Column(Float)
    last_update = Column(Date, default=func.now())
    special_features = Column(String(255))
    full_text = Column(Text)

    language_films = relationship("Language", backref="films")
    film_categories = relationship("FilmCategory", backref="film")
    film_actors = relationship("FilmActor", backref="film")
    film_inv = relationship("Inventory", backref="film")


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    last_update = Column(Date, default=func.now())

    films_category = relationship("FilmCategory", backref="category")


class FilmCategory(Base):
    __tablename__ = 'film_category'

    film_id = Column(Integer, ForeignKey("film.id"), primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("category.id"), primary_key=True)
    last_update = Column(Date, default=func.now())

    film_categories = relationship("Film", backref="film_category")
    category_categories1 = relationship("Category", backref="film_category")


class Language(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_update = Column(Date, default=func.now())

    films_language = relationship("Film", backref="language")


class FilmActor(Base):
    __tablename__ = 'film_actor'

    actor_id = Column(Integer, ForeignKey("actor.actor_id"), primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey("film.id"), primary_key=True)
    last_update = Column(Date, default=func.now())

    film_actors = relationship("Film", backref="film_actor1")
    actor_actor = relationship("Actor", backref="film_actor2")


class Actor(Base):
    __tablename__ = 'actor'

    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    last_update = Column(Date, default=func.now())

    film_actor = relationship("FilmActor", backref="actor")


class Inventory(Base):
    __tablename__ = 'inventory'

    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey("film.id"), nullable=False)
    store_id = Column(Integer, nullable=False)
    last_update = Column(Date, default=func.now())

    film_inventory = relationship("Film", backref="inventory1")


class Rental(Base):
    __tablename__ = 'rental'

    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    inventory_id = Column(Integer, ForeignKey("inventory.inventory_id"), nullable=False)
    rental_date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    return_date = Column(Date, nullable=False)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"), nullable=False)
    last_update = Column(Date, default=func.now())

    inventory_rental = relationship("Inventory", backref="rental")
    customer_rental = relationship("Customer", backref="rental")
    staff_rental = relationship("Staff", backref="rental")


class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100))
    address_id = Column(Integer, ForeignKey("address.address_id"), nullable=False)
    is_active = Column(Boolean, nullable=False)
    create_date = Column(Date, nullable=False)
    last_update = Column(Date, default=func.now())
    rental_id = Column(Integer, nullable=False)

    address_customer = relationship("Address", backref="customers")


class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address_id = Column(Integer, ForeignKey("address.address_id"), nullable=False)
    store_id = Column(Integer, ForeignKey("store.store_id"), nullable=False)
    active = Column(Boolean, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    last_update = Column(Date, default=func.now())
    picture_id = Column(Integer)

    address_staff = relationship("Address", backref="staff")
    store_staff = relationship("Store", backref="staff")


class Payment(Base):
    __tablename__ = "payment"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"), nullable=False)
    rental_id = Column(Integer, ForeignKey("rental.rental_id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)

    customer_payment = relationship("Customer", backref="payments")
    staff_payment = relationship("Staff", backref="payments")
    rental_payment = relationship("Rental", backref="payments")


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(255), nullable=False)
    address2 = Column(String(255))
    district = Column(String(100))
    city_id = Column(Integer, ForeignKey("city.city_id"), nullable=False)
    postal_code = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    last_update = Column(Date, default=func.now())

    city_address = relationship("City", backref="addresses")


class Store(Base):
    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True, autoincrement=True)
    manager_staff_id = Column(Integer, nullable=False)
    address_id = Column(Integer, ForeignKey("address.address_id"), nullable=False)
    last_update = Column(Date, default=func.now())

    address_store = relationship("Address", backref="stores")


class City(Base):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey("country.country_id"), nullable=False)
    last_update = Column(Date, default=func.now())

    country_city = relationship("Country", backref="cities")


class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(50), nullable=False)
    last_update = Column(Date, default=func.now())
