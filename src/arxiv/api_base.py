"""
Base class for the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) API.

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) is a protocol developed by the Open Archives.
The protocol is used to harvest metadata records from a repository.

https://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm#ProtocolMessages

"""

from abc import ABC, abstractmethod
from typing import Union


class OaiPmhApiBase(ABC):
    """
    Base class for the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) API.
    """

    @abstractmethod
    def get_record(self, identifier: str) -> dict[str, Union[str, list[str]]]:
        """
        Retrieve a record by its identifier.

        :param identifier: The identifier of the record to retrieve.
        :return: The record.
        """

    @abstractmethod
    def list_records(self) -> list[dict[str, Union[str, list[str]]]]:
        """
        List all records.

        :return: A list of records.
        """

    @abstractmethod
    def list_sets(self) -> list[dict[str, Union[str, list[str]]]]:
        """
        List all sets.

        :return: A list of sets.
        """

    @abstractmethod
    def list_identifiers(self) -> list[dict[str, Union[str, list[str]]]]:
        """
        List all identifiers.

        e.g.: http://export.arxiv.org/oai2?verb=ListIdentifiers&metadataPrefix=oai_dc

        :return: A list of identifiers.
        """
