# Capture radio streaming in mp3 files.
# Author: Upasana Pandey
import time
import requests
from datetime import datetime
import os


def RadioCapture(stream_url, directory, minutes):

  '''
  Function to capture radio streaming in real time

  '''
    r = requests.get(stream_url, stream=True)
    now = datetime.now()
    cur = now.strftime("ymd_%Y_%m_%d_hms_%H_%M_%S")
    cur1 = str(cur)
    file = directory+'_'+cur1
    with open(file+'.mp3', 'wb') as f:
        start_time = time.time()
        print("Record the radio streaming......")
        for block in r.iter_content(1024):
            f.write(block)
            time_diff = time.time()-start_time
            time_elapse = time_diff/60
            # print(time_elapse) #for Testing the recording
            if(time_elapse >= minutes):
                break
    f.close()
    if not os.path.exists('./WNYC_AM_820/wav_files/'):
        os.makedirs('./WNYC_AM_820/wav_files/')
    print("Converting from MP3 to wav format")
    mp3towav(file+'.mp3', './WNYC_AM_820/wav_files/WNYC_AM_820_'+cur1)

    if not os.path.exists('./WNYC_AM_820/speech_to_text_output/'):
        os.makedirs('./WNYC_AM_820/speech_to_text_output/')
    print("Speech recognition")
    speech_to_text3('./WNYC_AM_820/wav_files/WNYC_AM_820_'+cur1+'.wav',
                    "./WNYC_AM_820/speech_to_text_output/speech_to_text_output_"+cur1)

    if not os.path.exists('./WNYC_AM_820/wav_files/spectrogram/'):
        os.makedirs('./WNYC_AM_820/wav_files/spectrogram/')
    print("Spectogram analysis")
    spectrogram('./WNYC_AM_820/wav_files/WNYC_AM_820_'+cur1+'.wav',
                './WNYC_AM_820/wav_files/spectrogram/spectrogram_'+cur1)

    if not os.path.exists('./WNYC_AM_820/Geo_location/'):
        os.makedirs('./WNYC_AM_820/Geo_location/')
    print("Finding geo location data")
    geo_location('http://radio.garden/listen/wnyc-am-820/xdwC-TvT',
                 './WNYC_AM_820/Geo_location/')


if __name__ == "__main__":
    streaming_url = 'https://am820.wnyc.org/wnycam-web?listening-from-radio-garden=1614158564622'
    if not os.path.exists('./WNYC_AM_820/mp3_files/'):
        os.makedirs('./WNYC_AM_820/mp3_files/')
    for i in range(0, 10):
        RadioCapture(streaming_url, './WNYC_AM_820/mp3_files/WNYC_AM_820_', i)
