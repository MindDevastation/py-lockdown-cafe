import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{visitor.get("name", "Visitor")} "
                                     f"is not vaccinated.")

        vaccine_info = visitor["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")

        if not expiration_date:
            raise OutdatedVaccineError(f'{visitor.get("name", "Visitor")}\'s '
                                       f"vaccine information is incomplete.")

        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(f'{visitor.get("name", "Visitor")}\'s '
                                       f"vaccine is expired.")

        # Check mask-wearing status
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(f'{visitor.get("name", "Visitor")} '
                                      f"is not wearing a mask.")

        return f"Welcome to {self.name}"
