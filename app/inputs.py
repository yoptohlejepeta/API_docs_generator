from pydantic import BaseModel, field_validator
from datetime import datetime
import streamlit as st

class Title(BaseModel):
    title: str | None = "API Documentation"
    author: str | None = None
    date: str
    
    @field_validator("*")
    def normalize_none(cls, v):
        if v is "":
            return None
        return v
    
    @field_validator("date", mode="before")
    def validate_date(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            st.warning("Incorrect data format, should be YYYY-MM-DD")
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return v