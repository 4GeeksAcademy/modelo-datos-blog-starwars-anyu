from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

    class Planet(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(120), nullable=False)
        climate: Mapped[str] = mapped_column(String(120), nullable=False)
        terrain: Mapped[str] = mapped_column(String(120), nullable=False)
        population: Mapped[int] = mapped_column(nullable=False)

    class Character(db.Model):
            id: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str] = mapped_column(String(120), nullable=False)
            gender: Mapped[str] = mapped_column(String(50), nullable=False)
            height: Mapped[int] = mapped_column(nullable=False)
            birth_year: Mapped[str] = mapped_column(String(50), nullable=False)

    class Favorite(db.Model):
            id: Mapped[int] = mapped_column(primary_key=True)

            user_id: Mapped[int] = mapped_column(
            ForeignKey("user.id"), nullable=False
            )

            planet_id: Mapped[int] = mapped_column(
                ForeignKey("planet.id"), nullable=True
            )

            character_id: Mapped[int] = mapped_column(
                ForeignKey("character.id"), nullable=True
            )
