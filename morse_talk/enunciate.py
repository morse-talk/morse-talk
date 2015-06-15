"""
Function to enunciate string of plain text in morse code
"""

#   Author : Sheikh Araf
#   Email : arafsheikh@gmail.com

import wave
import sys

__all__ = ['enunciate']

files = {
        'A': 'sound/A.wav',
        'B': 'sound/B.wav',
        'C': 'sound/C.wav',
        'D': 'sound/D.wav',
        'E': 'sound/E.wav',
        'F': 'sound/F.wav',
        'G': 'sound/G.wav',
        'H': 'sound/H.wav',
        'I': 'sound/I.wav',
        'J': 'sound/J.wav',
        'K': 'sound/K.wav',
        'L': 'sound/L.wav',
        'M': 'sound/M.wav',
        'N': 'sound/N.wav',
        'O': 'sound/O.wav',
        'P': 'sound/P.wav',
        'Q': 'sound/Q.wav',
        'R': 'sound/R.wav',
        'S': 'sound/S.wav',
        'T': 'sound/T.wav',
        'U': 'sound/U.wav',
        'V': 'sound/V.wav',
        'W': 'sound/W.wav',
        'X': 'sound/X.wav',
        'Y': 'sound/Y.wav',
        'Z': 'sound/Z.wav',
        ' ': 'sound/blank.wav',
        '?': 'sound/Question_Mark.wav',
        '.': 'sound/Period.wav',
        ',': 'sound/Comma.wav',
        ';': 'sound/SemiColon.wav',
        ':': 'sound/Colon.wav',
        "'": 'sound/Apostrope.wav',
        '/': 'sound/Slash.wav',
        '_': 'sound/Underscore.wav',
        ')': 'sound/Parenthesis_Close',
        '(': 'sound/Parenthesis_Open'
    }

sequence = []   # The sequence of wave files will be stored here and later merged

def enunciate(message, encoding_type='default', outfile='sys.stdout'):
    """Converts the given message in plain text to morse audio

    The raw PCM data will be written to stdout if 'outfile' parameter
    is set to sys.stdout(default). This data can then be piped to
    other programs, for example, aplay(Linux).
    
    A Wave(wav) file will be created in the current directory if
    outfile parameter is provided.

    Parameters
    ----------
    message : String
    
    encoding : Type of encoding
        Supported types are morse(default)

    outfile : Output file
        Output raw PCM data to stdout by default.
        Wave file will be created in current dir if parameter provided

    """

    if(encoding_type != 'default'):
        return ('Only morse supported at the moment')

    message = str(message.strip().upper())   # Avoid complications
    message = list(message)

    # Populate sequence(list) with sound files
    for c in message:
        sequence.append(files.get(c, '?'))    

    # Print to stdout(default)
    if(outfile == 'sys.stdout'):
        for infile in sequence:
            w = wave.open(infile, 'rb')
            sys.stdout.write(w.readframes(w.getnframes()))  # Wirte raw PCM data to stdout. Can be piped to aplay(Linux) 

    # Else create a wave file
    else:
        # Set all the necessary parameters for the output wave file
        w = wave.open(sequence[0], 'rb')
        output = wave.open(outfile, 'wb')
        output.setparams(w.getparams())
        w.close()
        
        for infile in sequence:
            w = wave.open(infile, 'rb')
            output.writeframes(w.readframes(w.getnframes()))    # Append each file's data to output file
            w.close()
        output.close()
