import datetime

from errors import (NotVaccinatedError, NotWearingMaskError,
                    OutdatedVaccineError, VaccineError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError
        if "expiration_date" in visitor["vaccine"]:
            expiration_date = visitor["vaccine"]["expiration_date"]
            if expiration_date < datetime.date.today():
                raise OutdatedVaccineError
        if "wearing_a_mask" in visitor and not visitor["wearing_a_mask"]:
            raise NotWearingMaskError
        return f"Welcome to {self.name}"


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except VaccineError:
                raise
            except NotWearingMaskError:
                masks_to_buy += 1
    except VaccineError:
        return "All friends should be vaccinated"
    else:
        if masks_to_buy:
            return f"Friends should buy {masks_to_buy} masks"
        return f"Friends can go to {cafe.name}"
