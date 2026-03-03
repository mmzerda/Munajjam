import pytest
from munajjam.cli import _infer_surah_number

def test_infer_surah_number_valid():
    assert _infer_surah_number("surah_001.mp3") == 1
    assert _infer_surah_number("011.mp3") == 11
    assert _infer_surah_number("recitation_114_v2.mp3") == 114

def test_infer_surah_number_invalid():
    with pytest.raises(ValueError, match="لم يتم العثور على رقم سورة"):
        _infer_surah_number("no_numbers.mp3")
    
    with pytest.raises(ValueError, match="غير صالح"):
        _infer_surah_number("surah_115.mp3")
