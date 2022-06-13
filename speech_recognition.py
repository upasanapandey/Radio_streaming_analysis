# Speech to text conversion using Microsoft Azure streaming API
# Author : Upasana Pandey
import azure.cognitiveservices.speech as speechsdk
import time
import datetime
import os


def speech_to_text3(audio_filename, directory):
    '''
    Function to perform for speech to text conversion
    '''

    # Creates an instance of a speech config with specified subscription key and service region.
    speech_key, service_region = "a439956a58f5428c8f136179b5085e6d", "eastus"
    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=service_region)

    # Creates an audio configuration that points to an audio file.
    #audio_filename = "./WNYC AM 820 FM/wav files/WNYC AM 820 FM_ymd_2021_02_24_hms_16_19_38.wav"
    audio_input = speechsdk.audio.AudioConfig(filename=audio_filename)

    # Creates a recognizer with the given settings
    speech_config.speech_recognition_language = "en-US"
    speech_config.request_word_level_timestamps()
    speech_config.enable_dictation()
    speech_config.output_format = speechsdk.OutputFormat(1)

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_input)

    #result = speech_recognizer.recognize_once()
    all_results = []

    def handle_final_result(evt):
        all_results.append(evt.result.text)

    done = False

    def stop_cb(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    # Appends the recognized text to the all_results variable.
    speech_recognizer.recognized.connect(handle_final_result)

    # Connect callbacks to the events fired by the speech recognizer & displays the info/status
    speech_recognizer.recognizing.connect(
        lambda evt: print('RECOGNIZING: {}'.format(evt)))
    speech_recognizer.recognized.connect(
        lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(
        lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.session_stopped.connect(
        lambda evt: print('SESSION STOPPED {}'.format(evt)))
    speech_recognizer.canceled.connect(
        lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()

    while not done:
        time.sleep(.5)

    print("Writing the result in a file")
    separator = " "
    with open(directory+".txt", 'w') as f:
        f.write(separator.join(all_results))
    f.close()
    os.makedirs(directory+"/Pos/")
    pos_tagging(directory+".txt", directory+"/Pos/")
