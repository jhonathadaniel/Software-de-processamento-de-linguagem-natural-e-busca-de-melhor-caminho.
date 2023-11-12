import speech_recognition as sr

def listen_microfone():
    microfone = sr.Recognizer()
    frases = []  # Inicializa a lista vazia para armazenar as frases

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=1.0)
        print('Ouvindo:')
        audio = microfone.listen(source)
        with open('recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
        
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse:' + frase)
        frases.append(frase)  # Adiciona a frase reconhecida à lista de frases
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    
    return frases

lista_de_frases = listen_microfone()
print("Lista de frases reconhecidas:", lista_de_frases)