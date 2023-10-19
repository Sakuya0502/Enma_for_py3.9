
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Literal, Optional, TypedDict, Union
from enma.domain.entities.base import Entity

@dataclass
class Image:
    uri: str
    width: int = field(default=0)
    height: int = field(default=0)

class MIME(Enum):
    J = 'jpg'
    P = 'png'
    G = 'gif'

@dataclass
class Title:
    english: str = field(default='')
    japanese: str = field(default='')
    other: str = field(default='')

class IMangaProps(TypedDict):
    id: Union[int, str]
    created_at: datetime
    updated_at: datetime
    title: Title
    pages_count: int
    pages: list[Image]

@dataclass
class Chapter:
    id: Union[str, int]
    pages: list[Image] = field(default_factory=list)

    def add_page(self, page: Image) -> None:
        self.pages.append(page)

@dataclass
class Genre:
    name: str
    id: Union[str, int] = field(default=0)

@dataclass
class Manga(Entity[IMangaProps]):

    title: Title
    authors: list[str]
    genres: list[Genre]
    chapters: list[Chapter]
    chapters_count: int
    cover: Union[Image, None]
    thumbnail: Union[Image, None]

    def __init__(self,
                 title: Title,
                 chapters: list[Chapter],
                 genres: Optional[list[Genre]] = None,
                 authors: Optional[list[str]] = None,
                 thumbnail: Optional[Image] = None,
                 cover: Optional[Image] = None,
                 id: Union[int, str, None] = None, 
                 created_at: Optional[datetime] = None, 
                 updated_at: Optional[datetime] = None):
        
        super().__init__(id=id,
                         created_at=created_at,
                         updated_at=updated_at)
        
        self.title = title
        self.chapters = chapters
        self.thumbnail = thumbnail
        self.cover = cover
        self.chapters_count = len(self.chapters if self.chapters else [])
        self.authors = authors or []
        self.genres = genres or []
        
