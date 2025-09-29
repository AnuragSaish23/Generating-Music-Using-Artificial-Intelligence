import os
from music21 import chord, metadata, stream, environment

environment.set('musicxmlPath', r'D:/MuseScore/bin/MuseScore4.exe')     
print("Script Started")

class LSystem:
    """
    a basic l-system class that provides functionality for generating sequences based on initial axiom 
    and production rules
    """

    def __init__(self, axiom, rules):
        '''
        initialize the L-system with an axiom and production rules.

        Parameters:
        -axioms(str) : the initial symbol.
        -rules(dict) : A dictionary where keys are symbols and values are correspoinding replacement
                       strings. eg, {"A": "ABC"}
        '''
        self.axiom = axiom
        self.rules = rules
        self.output = axiom
        
    def aplphabet(self):
        """
        Get the alphabet of the L-System
        Returns:
            - set: The alphabet of the L-System.
        """

        return set(self.axiom + "".join(self.rules.values()))

    def iterate(self, n=1):
        """
        Apply the production rules to current output n times.

        Parameters:
        -n (int) : Number of times the rules are to be applied.

        Returns:
        -str: the output after apllying the rules n times.
        """

        for i in range(n):
            next_output = self._iterate_once()
            self.output = next_output
            print(f"Output after {i+1} iteration(s): {self.output}")
        final_output = self.output
        self._reset_output()
        return final_output
    
    def _iterate_once(self):
        """
        Apply the production rules to current output once.

        Returns:
        -str: The output after applying the production rules once.
        """
        symbols = [self._apply_rule(symbol) for symbol in self.output]
        return "".join(symbols)
    
    def _apply_rule(self, symbol):
        """
        Apply Production rules to a given symbol.

        Parameters: 
        -symbol (str) : The Symbol to which the rules are to be applied

        Returns:
        -str: The transformed symbol or the original symbol if no rules apply.
        """
        return self.rules.get(symbol, symbol)
    
    def _reset_output(self):
        #Resetting the output to the original axiom.
        self.output = self.axiom

def l_system_to_music21_chords(chord_sequence):
    """
    Translate the L-system generated chord sequence into a list of music21 chords.

    Parameters:
    -chord_sequence (str): The L-system generated chord sequence.

    Returns:
    -list of music21.chord.Chord : The corresponding chord progression in music 21 format.
    """
    chord_dict = {
        "C": ["C","E","G"], #Cmaj
        "D": ["D","F","A"], #Dmin
        "E": ["E","G","B"], #Emin
        "F": ["F","A","C"], #Fmaj
        "G": ["G","B","D"], #Gmaj
        "A": ["A","C","E"], #Amin
        "B": ["B","D","F"], #Bdimnished
    }
    chords =  [chord.Chord(chord_dict[chord_name]) for chord_name in chord_sequence if chord_name in chord_dict]
    print(f"Generated {len(chords)} chords.")
    return chords

def create_and_show_music21_score(music21_chords):
    """
    Create and display a music score using the music21 library.

    This function takes a list of music21 chord objects and creates a score with them. It then displays this score. 
    The score is titles "L-System Chord Progression".

    Parameters:
    - music21_chords (List): A list of music21 chord objects.
    """

    #Creating a new music21 stream.Score object
    score = stream.Score()

    #Set the metadata for the score with a title
    score.metadata = metadata.Metadata(title="L-System Chord Progression")

    #Create a new music21 stream.Part object
    part = stream.Part()

    #Loop through each chord in music21_chords list
    for ch in music21_chords:
        #append each chord to the part object
        part.append(ch)
    
    #Append the Part object containing the chords to the Score object.
    score.append(part)

    #display the score
    output_file = "l_system_output.musicxml"
    print(f"Writing score to {output_file}...")
    score.write('musicxml', fp=output_file)

    # Try displaying
    print("Attempting to show score...")
    score.show()


def main():
    """
    Main function to demonstrate the generation of chord progession using L-System
    """
    #Axiom : A
    #Production rules : A -> ABC, B -> BA, C -> E, F -> GFD

    try:
        n = int(input("Enter the number of iterations for L-System : "))
    except ValueError:
        print("Invalid input, Please enter a valid Integer.")
        return


    print("Program Started")
    axiom = "A"
    rules = {"A":"ABC", "B":"BA","C":"E", "F": "GFD"}

    l_system = LSystem(axiom, rules)

    chord_sequence = l_system.iterate(n)
    # the number of times the rules will be applied.
    print(f"Final chord sequence: {chord_sequence}")
    music21_chords = l_system_to_music21_chords(chord_sequence)

    create_and_show_music21_score(music21_chords)
    print("Program finished.")

if __name__ == "__main__":
    main()