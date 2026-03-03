from munajjam.core.aligner import align

def run_example():
    print("Running Simple Alignment Example...")
    audio = "test.wav"
    segments = [{"text": "الحمد لله", "start": 0.0, "end": 3.0}]
    ayahs = ["الحَمدُ لِلَّهِ"]
    
    # محاكاة عملية المحاذاة
    results = align(audio, segments, ayahs)
    print(f"Alignment completed with {len(results)} results.")
    return True

if __name__ == "__main__":
    run_example()
