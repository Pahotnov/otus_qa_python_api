from pydantic import BaseModel


class BreweryModelResponse(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: str
    address_2: str | None
    address_3: str | None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: str | None
    latitude: str | None
    phone: str | None
    website_url: str | None
    state: str
    street: str
