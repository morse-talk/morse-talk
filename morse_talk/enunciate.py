"""
Function to enunciate string of plain text in morse code
"""

#   Author : Sheikh Araf
#   Email : arafsheikh@gmail.com

import wave
import sys, os
import tempfile
import platform

OS = platform.system()  # Get the operating system name
if OS == 'Windows':
    import winsound

pt = os.path.dirname(os.path.realpath(__file__))

__all__ = ['enunciate']

files = {
        'A': os.path.join(pt, 'sound/A.wav'),
        'B': os.path.join(pt, 'sound/B.wav'),
        'C': os.path.join(pt, 'sound/C.wav'),
        'D': os.path.join(pt, 'sound/D.wav'),
        'E': os.path.join(pt, 'sound/E.wav'),
        'F': os.path.join(pt, 'sound/F.wav'),
        'G': os.path.join(pt, 'sound/G.wav'),
        'H': os.path.join(pt, 'sound/H.wav'),
        'I': os.path.join(pt, 'sound/I.wav'),
        'J': os.path.join(pt, 'sound/J.wav'),
        'K': os.path.join(pt, 'sound/K.wav'),
        'L': os.path.join(pt, 'sound/L.wav'),
        'M': os.path.join(pt, 'sound/M.wav'),
        'N': os.path.join(pt, 'sound/N.wav'),
        'O': os.path.join(pt, 'sound/O.wav'),
        'P': os.path.join(pt, 'sound/P.wav'),
        'Q': os.path.join(pt, 'sound/Q.wav'),
        'R': os.path.join(pt, 'sound/R.wav'),
        'S': os.path.join(pt, 'sound/S.wav'),
        'T': os.path.join(pt, 'sound/T.wav'),
        'U': os.path.join(pt, 'sound/U.wav'),
        'V': os.path.join(pt, 'sound/V.wav'),
        'W': os.path.join(pt, 'sound/W.wav'),
        'X': os.path.join(pt, 'sound/X.wav'),
        'Y': os.path.join(pt, 'sound/Y.wav'),
        'Z': os.path.join(pt, 'sound/Z.wav'),
        ' ': os.path.join(pt, 'sound/blank.wav'),
        '?': os.path.join(pt, 'sound/Question_Mark.wav'),
        '.': os.path.join(pt, 'sound/Period.wav'),
        ',': os.path.join(pt, 'sound/Comma.wav'),
        ';': os.path.join(pt, 'sound/SemiColon.wav'),
        ':': os.path.join(pt, 'sound/Colon.wav'),
        "'": os.path.join(pt, 'sound/Apostrope.wav'),
        '/': os.path.join(pt, 'sound/Slash.wav'),
        '_': os.path.join(pt, 'sound/Underscore.wav'),
        ')': os.path.join(pt, 'sound/Parenthesis_Close'),
        '(': os.path.join(pt, 'sound/Parenthesis_Open')
    }


def play(path):
    """Plays the referenced wave file

    Parameters
    ----------
    path : Absolute path to the wave file
    
    """
    if OS == 'Windows':
        winsound.PlaySound(path, winsound.SND_FILENAME)
        
    elif OS == 'Linux':
        os.system("aplay -q " + path)   # quiet mode to supress output


def enunciate(message, encoding_type='default'):
    """Converts the given message in plain text to morse audio

    A wave(.wav) file will be created in the operating system's
    temporary directory; then will be played and deleted.

    Parameters
    ----------
    message : String
    
    encoding : Type of encoding
        Supported types are morse(default)

    """

    if(encoding_type != 'default'):
        return ('Only morse supported at the moment')

    sequence = []   # The sequence of wave files will be stored here and later merged
    
    message = str(message.strip().upper())   # Avoid complications
    message = list(message)

    # Populate sequence(list) with sound files
    for c in message:
        sequence.append(files.get(c, '?'))    
    
    # Create a temporary output wave file
    outfile, outfile_path = tempfile.mkstemp(suffix = '.wav')
    
    # Set all the necessary parameters for the output wave file
    w = wave.open(sequence[0], 'rb')
    output = wave.open(outfile_path, 'wb')
    output.setparams(w.getparams())
    w.close()
        
    for infile in sequence:
        w = wave.open(infile, 'rb')
        output.writeframes(w.readframes(w.getnframes()))    # Append each file's data to output file
        w.close()
   
    output.close()  # Close file opened with wave module's open function
    os.close(outfile)   # Close the temporary file
    
    play(outfile_path)
    os.remove(outfile_path)
