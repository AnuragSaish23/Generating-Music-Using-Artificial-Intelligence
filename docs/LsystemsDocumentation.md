# L-System Chord Generator

## Overview
The **L-System module** generates chord progressions based on a formal grammar system called **Lindenmayer Systems (L-Systems)**.  
Each symbol in the sequence corresponds to a chord, and production rules define how the sequence evolves with iterations.

---

## How It Works
1. **Axiom:** The starting symbol (e.g., `"A"`).  
2. **Production Rules:** Rules mapping symbols to sequences (e.g., `{"A":"ABC", "B":"BA"}`)  
3. **Iterations:** Apply the rules repeatedly to generate a chord sequence.  
4. **Output:** A string of symbols representing chords.

---

## Example Usage
```python
from src.piano_generation.l_system_module import LSystem, l_system_to_music21_chords, create_and_show_music21_score

lsys = LSystem("A", {"A":"ABC", "B":"BA","C":"E"})
chord_sequence = lsys.iterate(n=3)  # Generate sequence after 3 iterations

music21_chords = l_system_to_music21_chords(chord_sequence)
create_and_show_music21_score(music21_chords)
