import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print(f"[{i}] ID: {voice.id}")
    print(f"    Name: {voice.name}")
    print(f"    Languages: {voice.languages}")
    print(f"    Gender: {voice.gender}")
    print(f"    Age: {voice.age}")
    print()