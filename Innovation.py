from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import wave
import sounddevice as sd
import pydub
from pydub.playback import play
from pydub import AudioSegment
import ffmpeg
import os
import soundfile 
import wave
import scipy.signal as signal
import numpy as np
import sounddevice as sd
import struct
import audioop
from pydub.utils import get_array_type
from pydub import AudioSegment




def lire(file_path):
    sound=AudioSegment.from_file(file_path)
    return sound
def lire_info(file_name):
    info={}
    audio=AudioSegment.from_file(file_name)
    #print(f"Type de fichier : {file_name.format}")
    #print(f"Durée du fichier : {audio.duration_seconds:.2f} secondes")
    #print(f"Fréquence d'échantillonnage : {audio.frame_rate} Hz")
    #print(f"Nombre de canaux : {audio.channels}")
    #print(f"Largeur d'échantillonnage : {audio.sample_width} octets")
    info["type de fichier"]=file_name.format
    info["Durrée du fichier"]=audio.duration_seconds
    info["Fréquence d'échantillonage"]=audio.frame_rate
    info["Nombre de canaux"]=audio.channels
    info["Largeur d'échantillonnage"]=audio.sample_width
    return info
def ecouter(file_name):
    audio=AudioSegment.from_file(file_name)
    return play(audio)
def compresser_audio(input_file, output_file, formatc):
    # Chargement du fichier audio avec pydub
    sound = AudioSegment.from_file(input_file)

    # Compression du fichier audio
    compressed_sound = sound.export(output_file, format=formatc)

    # Retour du fichier compressé
    return compressed_sound
def decompresser_audio_file(input_file,output_file,formatc):
    if formatc=="wma"or formatc=="WMA":
        audio_stream = ffmpeg.input(input_file)
        audio_stream = ffmpeg.output(audio_stream, output_file, acodec='wmav2')
        ffmpeg.run(audio_stream)
    elif formatc=="wav"or formatc=="WAV":
        sound = AudioSegment.from_file(input_file)
        compressed_sound = sound.export(output_file, format="wav")
    else:
        print("format choisie est invalide")
def calculer_taux_compression(fichier_avant, fichier_apres):
    taille_avant = os.path.getsize(fichier_avant)
    taille_apres = os.path.getsize(fichier_apres)
    taux = (taille_avant - taille_apres) / taille_avant * 100
    return taux
def calculer_nombre_bits_audio(fichier_avant):
    audio, taux_echantillonnage = soundfile.read(fichier_avant)
    nombre_bits = audio.dtype.itemsize * 8
    return nombre_bits
def obtenir_taille_fichier(fichier_audio):
    return os.path.getsize(fichier_audio)
def collecter_info_compression(fichier_avant,fichier_apres):
    info = {}
    fichier_audio=AudioSegment.from_file(fichier_avant)
    taille_fichier = obtenir_taille_fichier(fichier_avant)
    taux_compression=calculer_taux_compression(fichier_avant, fichier_apres)
    nbr_bits=calculer_nombre_bits_audio(fichier_avant)
    #print(f"Type de fichier : {fichier_avant.format}")
    #print(f"Taille de fichier : {taille_fichier}")
    #print(f"Durée du fichier : {fichier_audio.duration_seconds:.2f} secondes")
    #print(f"Fréquence d'échantillonnage : {fichier_audio.frame_rate} Hz")
    #print(f"Nombre de canaux : {fichier_audio.channels}")
    #print(f"Largeur d'échantillonnage : {fichier_audio.sample_width} octets")
    #print(f"Taux de compression : {taux_compression}")
    #print(f"nombre de bits : {nbr_bits}")
    info["Type de fichier"]=fichier_avant.format
    info["Taille de fichier"]=taille_fichier
    info["Durrée du fichier"]=fichier_audio.duration_seconds
    info["Frequence d'échantillonage"]=fichier_audio.frame_rate
    info["Nombre de cannaux"]=fichier_audio.channels
    info["Largeur d'échantillonnage"]=fichier_audio.sample_width
    info["Taux de compression"]=taux_compression
    info["Nombre de bits"]=nbr_bits
    return info



def open_file(filename):
    raw_data = AudioSegment.from_file(filename)
    return raw_data

def get_audio_data(audio):
    audio_data = np.frombuffer(audio.raw_data, dtype=f'int{audio.sample_width*8}')
    return audio_data

def audio_info(audio):
    return [audio.sample_width, audio.channels, len(audio.get_array_of_samples()), audio.frame_rate]

def lzw_encode(text):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    sequence = ""
    for char in text:
        new_sequence = sequence + char
        if new_sequence in dictionary:
            sequence = new_sequence
        else:
            result.append(dictionary[sequence])
            dictionary[new_sequence] = len(dictionary)
            sequence = char
    if sequence:
        result.append(dictionary[sequence])
    return result

def lzw_decode(encoded_text):
    dictionary = {i: chr(i) for i in range(256)}
    result = ""
    sequence = chr(encoded_text.pop(0))
    for code in encoded_text:
        if code in dictionary:
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = sequence + sequence[0]
        else:
            raise ValueError("Invalid LZW code")
        result += entry
        dictionary[len(dictionary)] = sequence + entry[0]
        sequence = entry
    return result

def adpcm_coding(filtered_audio,samp_width):
    return audioop.lin2adpcm(filtered_audio, samp_width, None)

def audio_filter(raw_data,info):
    audio_samples = get_audio_data(raw_data)
    sample_rate=info[3]
    print("sample rate = ", sample_rate)
    sample_width=info[0]
    # Define the filter parameters
    nyquist_freq = 0.5 * sample_rate
    high_cutoff_freq = 20  # Hz
    low_cutoff_freq = 20000  # Hz
    # Design the filters
    print("N channels:" , info[1])
    print("Ny = ", nyquist_freq)
    print("Hi_cutoff = ", high_cutoff_freq)
    print("Wn = ",high_cutoff_freq/nyquist_freq)
    try:
        highpass_filter = signal.butter(4, high_cutoff_freq/nyquist_freq, 'highpass')
        print("low_cutoff = ", low_cutoff_freq)
        print("Wn = ",low_cutoff_freq/nyquist_freq)
        lowpass_filter = signal.butter(4, low_cutoff_freq/nyquist_freq, 'lowpass')
        # Apply the filters
        filtered_audio = signal.filtfilt(highpass_filter[0], highpass_filter[1], audio_samples)
        filtered_audio = np.array(signal.filtfilt(lowpass_filter[0], lowpass_filter[1], filtered_audio),dtype=f'int{8*sample_width}')
    except:
        filtered_audio = audio_samples
    return filtered_audio


def reading_audio_irm(filename):
    with open(filename, "rb") as infile:
        header_data = infile.read(24)
        header_values = struct.unpack("llllll", header_data)
        audio_data = infile.read(header_values[1]*header_values[3])
    # ADPCM decoding
    retreived_compressed_adpcm = np.frombuffer(audio_data, dtype=f'int{8*header_values[5]}')
    decompressed_adpcm = lzw_decode(list(retreived_compressed_adpcm))
    char_bytes_array = bytearray()
    for char in decompressed_adpcm:
        char_bytes_array.append(ord(char))
    decoded_audio = audioop.adpcm2lin(char_bytes_array, header_values[3], None)
    recovored_audio_data = np.frombuffer(decoded_audio[0], dtype=f'int{8*header_values[3]}')
    return (recovored_audio_data, header_values[3], header_values[4], header_values[2])
    
def width(data):
    from math import log2,floor
    bit=floor(log2(max(data)))+1
    if(bit<=8):
        return 1
    elif(bit<=16):
        return 2
    elif(bit<=32):
        return 4

def writing_audio_irm(raw_data):
    info=audio_info(raw_data)
    audio_samples = get_audio_data(raw_data)
    filtered_audio=audio_filter(raw_data,info)
    adpcm_audio=adpcm_coding(filtered_audio,info[0])
    k=adpcm_audio[0]
    char_list = [chr(byte) for byte in k]
    joined_char_list = ''.join(char_list)
    compressed_adpcm =  lzw_encode(joined_char_list)
    wid=width(compressed_adpcm)
    data_size=len(audio_samples)*2
    header_size = 24
    filename = "test.irm"
    with open(filename, "wb") as outfile:
        outfile.write(struct.pack("llllll", header_size, len(audio_samples), info[3], info[0], info[1],wid))
        outfile.write(np.array(compressed_adpcm))
        
def listen(data_arr, n_channels, sample_rate):
    if(n_channels==1):
        return sd.play(data_arr, sample_rate)
    else:
        data_arr.shape=-1,n_channels
        return sd.play(data_arr, sample_rate)
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        