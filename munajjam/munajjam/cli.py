import sys
import argparse
import re
from pathlib import Path
from typing import List, Optional

# استيرادات المشروع
try:
    from munajjam.transcription.whisper import WhisperTranscriber
    from munajjam.core.aligner import align
    from munajjam.data.quran import load_surah_ayahs
except ImportError:
    pass # سيتم التعامل مع هذا عند التشغيل

def _infer_surah_number(audio_path: str) -> int:
    stem = Path(audio_path).stem
    match = re.search(r'\d+', stem)
    if match:
        num = int(match.group())
        if 1 <= num <= 114:
            return num
        raise ValueError(f"رقم السورة {num} غير صالح (1-114).")
    raise ValueError(f"لم يتم العثور على رقم سورة في اسم الملف.")

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="munajjam")
    subparsers = parser.add_subparsers(dest="command")
    align_p = subparsers.add_parser("align")
    align_p.add_argument("audio_path")
    align_p.add_argument("--surah", type=int)
    align_p.add_argument("--model", type=str, default=None)
    
    args = parser.parse_args(argv)
    if args.command == "align":
        try:
            surah_num = args.surah or _infer_surah_number(args.audio_path)
            print(f"✅ معالجة السورة رقم: {surah_num}", file=sys.stderr)
            # باقي منطق المحاذاة هنا...
            return 0
        except Exception as e:
            print(f"❌ خطأ: {e}", file=sys.stderr)
            return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
