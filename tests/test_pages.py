import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from NHentai.nhentai import NHentai
from NHentai.nhentai_async import NHentaiAsync

def test_standard_payload_integrity_home_page():
    pages = NHentai().get_pages()

    doujins = pages.doujins

    for doujin in doujins:
        assert doujin.id is not None 
        assert doujin.title is not None 
        assert doujin.lang is not None 
        assert doujin.cover is not None 
        assert doujin.data_tags is not None 

def test_standard_payload_integrity_characters_page():
    chars = NHentai().get_characters()
    assert chars.page is not None and isinstance(chars.page, int)
    assert chars.total_pages is not None and isinstance(chars.total_pages, int)
    assert chars.characters is not None and isinstance(chars.characters, list)
    for char in chars.characters:
        assert char.section is not None and isinstance(char.section, str)
        assert char.title is not None and isinstance(char.title, str)
        assert char.url is not None and isinstance(char.url, str)
        assert char.total_entries is not None and isinstance(char.total_entries, int)

@pytest.mark.asyncio
async def test_async_payload_integrity_home_page():
    pages = await NHentaiAsync().get_pages()

    doujins = pages.doujins

    for doujin in doujins:
        assert doujin.id is not None 
        assert doujin.title is not None 
        assert doujin.lang is not None 
        assert doujin.cover is not None 
        assert doujin.data_tags is not None 

@pytest.mark.asyncio
async def test_async_payload_integrity_characters_page():
    chars = await NHentaiAsync().get_characters()
    assert chars.page is not None and isinstance(chars.page, int)
    assert chars.total_pages is not None and isinstance(chars.total_pages, int)
    assert chars.characters is not None and isinstance(chars.characters, list)
    for char in chars.characters:
        assert char.section is not None and isinstance(char.section, str)
        assert char.title is not None and isinstance(char.title, str)
        assert char.url is not None and isinstance(char.url, str)
        assert char.total_entries is not None and isinstance(char.total_entries, int)