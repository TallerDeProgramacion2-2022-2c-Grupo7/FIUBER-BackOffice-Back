from pydantic import BaseModel

class Rating(BaseModel):
    id_trip: str
    id_user_scorer: str
    id_user_scored: str
    value: int

    class Config:
        orm_mode = True


class RatingsSummary(BaseModel):
    id_user_scored: str
    total_sum: int
    count: int

    class Config:
        orm_mode = True