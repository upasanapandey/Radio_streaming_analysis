#MP3 to wav conversion
#Author: Upasana Pandey
from pydub import AudioSegment 

def mp3towav(file,directory):

  '''
  Function to convert MP3 Files to wav file format
  '''
  AudioSegment.ffmpeg = "/absolute/path/to/ffmpeg"
  audiofile=AudioSegment.from_file(file)
  audiofile.export(directory+'.wav', format="wav") 
