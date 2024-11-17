"""
The datamodel for the oai_ic project.
"""

from pydantic import BaseModel



class OaiIc(BaseModel):
    """
    The OaiIc class is the data model for the oai_ic project.
    """
    title: str
    creator: list[str]
    subject: list[str]
    description: list[str] # item[0] is the abstract and item[1] if exists is a comment
    date: list[str]
    t: str
    identifier: list[str]



