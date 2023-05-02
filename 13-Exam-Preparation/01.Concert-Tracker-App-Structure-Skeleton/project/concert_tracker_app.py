from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if name in [m.name for m in self.musicians]:
            raise Exception(f"{name} is already a musician!")

        musician = ConcertTrackerApp.MUSICIAN_TYPES[musician_type](name, age)

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [b.name for b in self.bands]:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def __find_musician_by_name(self, name: str):
        musician = next((m for m in self.musicians if m.name == name), None)

        if musician is None:
            raise Exception(f"{name} isn't a musician!")

        return musician

    def __find_band_by_name(self, name: str):
        band = next((b for b in self.bands if b.name == name), None)

        if band is None:
            raise Exception(f"{name} isn't a band!")

        return band

    def __find_concert_by_place(self, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    @staticmethod
    def __check_musician_in_band(band, name: str):
        for musician in band.members:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a member of {band.name}!")

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)
        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        musician = self.__check_musician_in_band(band, musician_name)

        band.remove_member(musician)
        return f"{musician_name} was removed from {band_name}."

    @staticmethod
    def fulfilled_rock_concert_requirements(band: Band):
        for member in band.members:
            if member.__class__.__name__ == "Drummer":
                if "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

            if member.__class__.__name__ == "Singer":
                if "sing high pitch notes" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

            if member.__class__.__name__ == "Guitarist":
                if "play rock" not in member.skills:
                    Exception(f"The {band.name} band is not ready to play at the concert!")

        return True

    @staticmethod
    def fulfilled_metal_concert_requirements(band: Band):
        for member in band.members:
            if member.__class__.__name__ == "Drummer":
                if "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

            if member.__class__.__name__ == "Singer":
                if "sing low pitch notes" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

            if member.__class__.__name__ == "Guitarist":
                if "play metal" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

        return True

    @staticmethod
    def fulfilled_jazz_concert_requirements(band: Band):
        for member in band.members:
            if member.__class__.__name__ == "Drummer":
                if "play the drums with drum brushes" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

            elif member.__class__.__name__ == "Singer":
                if "sing high pitch notes" not in member.skills or "sing low pitch notes" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

            elif member.__class__.__name__ == "Guitarist":
                if "play jazz" not in member.skills:
                    raise Exception(f"The {band.name} band is not ready to play at the concert!")

        return True

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        concert = self.__find_concert_by_place(concert_place)

        for musician_type in ConcertTrackerApp.MUSICIAN_TYPES:
            if not any(
                filter(lambda x: x.__class__.__name__ == musician_type, band.members)
            ):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            if not self.fulfilled_rock_concert_requirements(band):
                return

        elif concert.genre == "Metal":
            if not self.fulfilled_metal_concert_requirements(band):
                return

        elif concert.genre == "Jazz":
            if not self.fulfilled_jazz_concert_requirements(band):
                return

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
