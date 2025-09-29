
---

## **2️⃣ `markov_chains.md`**

```markdown
# Markov Chain Melody Generator

## Overview
The **Markov Chain module** generates melodies based on **probabilities of note transitions**.  
It learns from a training set of notes and produces sequences where the next note depends on the current note.

---

## How It Works
1. **States:** Each note is represented as `(pitch, duration)`.  
2. **Initial Probabilities:** Probability of starting with each state.  
3. **Transition Matrix:** Probability of moving from one state to another, learned from training data.  
4. **Melody Generation:** The model generates sequences using the initial probabilities and transition matrix.

---

## Example Usage
```python
from src.piano_generation.markov_chain_module import MarkovChainMelodyGenerator, create_training_data, visualize_melody

training_data = create_training_data()  # Example notes for "Twinkle Twinkle Little Star"

states = [("C5",1), ("D5",1), ("E5",1), ("F5",1), ("G5",1), ("A5",1), ("C5",2)]
model = MarkovChainMelodyGenerator(states)
model.train(training_data)

generated_melody = model.generate(40)
visualize_melody(generated_melody)
