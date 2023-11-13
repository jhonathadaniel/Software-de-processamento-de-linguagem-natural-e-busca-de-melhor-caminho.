import speech_recognition as sr
from flask import Flask, request, jsonify

app = Flask(__name__)
microfone = sr.Recognizer()
frases = []  # Inicializa a lista fora da função para armazenar as frases

@app.route('/listen', methods=['GET'])
def start_listening():
    global frases
    frases = listen_microfone()
    if frases:
        return jsonify({'message': 'Áudio recebido com sucesso', 'frases': frases})
    else:
        return jsonify({'message': 'Não foi possível reconhecer o áudio'})

@app.route('/stop-listen', methods=['GET'])
def stop_listening():
    global frases
    frases = []  # Limpa a lista de frases
    return jsonify({'message': 'Escuta interrompida com sucesso'})

def listen_microfone():
    global frases
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse:' + frase)
        frases.extend([s.strip() for s in frase.split(',')])  # Adiciona as frases à lista sem redefinir
        return frases
    except sr.UnknownValueError:
        print('Não entendi')
        return None

if __name__ == '__main__':
    app.run(debug=True)
