# Function to create Spectrogram & waveform for a wav file
# Author : Upasana Pandey
# The frequencies of the audio or the pitch are identified with the brighter yellow columns present in the spectrum.
import matplotlib.pyplot as plot
from scipy.io import wavfile
import wave


def spectrogram(file, directory):
    '''
    Function to perform spectrogram analysis
    '''

    obj = wave.open(file, 'r')
    channels = obj.getnchannels()
    Sample_width = obj.getsampwidth()
    Frame_rate = obj.getframerate()
    Number_of_frames = obj.getnframes()
     parameters = obj.getparams()
      obj.close()

       if(channels == 1):

            # Read the wav file (mono)

            samplingFrequency, signalData = wavfile.read(file)

            # Plot the signal read from wav file

            plot.subplot(211)  # nrows=2, ncols=1, plot_number=1

            plot.title('Spectrogram of wav file')

            plot.plot(signalData)

            plot.xlabel('Sample')

            plot.ylabel('Amplitude[dB]')

            plot.subplot(212)  # nrows=2, ncols=1, plot_number=2

            plot.specgram(signalData, Fs=samplingFrequency)

            plot.xlabel('Time[sec]')

            plot.ylabel('Frequency[Hz]')

            plot.savefig(directory+'.png', bbox_inches='tight')

            plot.show()

        elif(channels == 2):
            # Read the wav file (stereo)

            samplingFrequency, signalData = wavfile.read(file)

        # Plot the signal read from wav file

            plot.subplot(211)

            plot.title('Spectrogram of a wav file with piano music')

            plot.plot(signalData[:, 1])

            plot.xlabel('Sample')

            plot.ylabel('Amplitude')

            plot.subplot(212)

            plot.specgram(signalData[:, 1], Fs=samplingFrequency)

            plot.xlabel('Time')

            plot.ylabel('Frequency')

            plot.savefig(directory+'.png', bbox_inches='tight')

            plot.show()
