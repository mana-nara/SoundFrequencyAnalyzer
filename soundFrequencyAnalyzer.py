import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Taking input from microphone
print("Welcome to the sound frequency analyzer!")
asciiart = """

   _____                       __
  / ___/____  __  ______  ____/ /
  \__ \/ __ \/ / / / __ \/ __  / 
 ___/ / /_/ / /_/ / / / / /_/ /  
/____/\____/\__,_/_/ /_/\__,_/   
                                 
"""
print(asciiart)
asciiartF  = """

    ______                                           
   / ____/_______  ____ ___  _____  ____  _______  __
  / /_  / ___/ _ \/ __ `/ / / / _ \/ __ \/ ___/ / / /
 / __/ / /  /  __/ /_/ / /_/ /  __/ / / / /__/ /_/ / 
/_/   /_/   \___/\__, /\__,_/\___/_/ /_/\___/\__, /  
                   /_/                      /____/   
"""
print(asciiartF)
asciiartA = """

    ___                __                     
   /   |  ____  ____ _/ /_  ______  ___  _____
  / /| | / __ \/ __ `/ / / / /_  / / _ \/ ___/
 / ___ |/ / / / /_/ / / /_/ / / /_/  __/ /    
/_/  |_/_/ /_/\__,_/_/\__, / /___/\___/_/     
                     /____/                   
"""
print(asciiartA)
asciiart2 = """
 ___________________________________________
|  _______________________________________  |
| / .-----------------------------------. \ |
| | | /\ :                        90 min| | |
| | |/--\:....................... NR [ ]| | |
| | `-----------------------------------' | |
| |      //-\\   |         |   //-\\      | |
| |     ||( )||  |_________|  ||( )||     | |
| |      \\-//   :....:....:   \\-//      | |
| |       _ _ ._  _ _ .__|_ _.._  _       | |
| |      (_(_)| |(_(/_|  |_(_||_)(/_      | |
| |               low noise   |           | |
| `______ ____________________ ____ ______' |
|        /    []             []    \        |
|       /  ()                   ()  \       |
!______/_____________________________\______!
Art by Simon Williams
"""
print(asciiart2)
print("Would you like to record? Type any letter when ready or 'q' to quit")
userInput = input()

while(userInput != "q"):
    fs = 44100  # sampling frequency 
    duration = 5  # seconds
    channels = 1

    print("Recording for {} seconds".format(duration))
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()

    audio = np.squeeze(audio_data)
    print(audio_data)

    wavfile.write("test.wav", fs, audio)
    print("Recording saved as test.wav")

    # Fourier Transform
    fourier = np.fft.fft(audio)

    # Plotting the data
    print("Thank you for your sound input! Here is the frequency analysis of your sound")
    print("Plotting...")
    sd.wait()  # wait for any remaining operations
    print("Give us a second..")
    
    frequencyDomain = np.linspace(0, fs, len(fourier))
    plt.plot(frequencyDomain, np.abs(fourier), color='green')
    plt.savefig("fourier.png")
    plt.show()

    print("Plot saved as fourier.png")
    print("Would you like to record again? Type any letter when ready or 'q' to quit")
    userInput = input()

print("Thank you for using the sound frequency analyzer! Goodbye!")