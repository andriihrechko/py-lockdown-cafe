import datetime

from exceptions import (NotVaccinatedError, NotWearingMaskError,
                        OutdatedVaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
