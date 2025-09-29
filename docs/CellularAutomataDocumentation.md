# Cellular Automaton Drum Generator

## Overview
This module generates drum patterns using **Cellular Automata rules**.  
It simulates kick, snare, hi-hat, and clap patterns programmatically.

## Dependencies
- `numpy`
- `music21`

## Classes

### DrumInstruments (Enum)
Defines the four drum instruments:
- KICK
- SNARE
- HIHAT
- CLAP

### DrumStates (Enum)
Defines drum states:
- OFF = 0
- ON = 1

### CellularAutomatonDrumGenerator
Generates a drum pattern using rules:
- Syncopation resolution
- Filling gaps
- Accenting
- Mutation

**Key Methods:**
- `step()`: Advance pattern by one time step.
- `add_random_fill(fill_length=4)`: Add a random fill at the end.

### DrumPatternMusic21Converter
Converts drum patterns to a **music21 score**.

**Example Usage:**
```python
from src.cellular_automata import CellularAutomatonDrumGenerator, DrumPatternMusic21Converter

generator = CellularAutomatonDrumGenerator(pattern_length=16)
converter = DrumPatternMusic21Converter()

for _ in range(8):
    generator.step()

score = converter.to_music21_score(generator.state)
score.write('midi', fp='generated_drum_pattern.mid')
score.show()
