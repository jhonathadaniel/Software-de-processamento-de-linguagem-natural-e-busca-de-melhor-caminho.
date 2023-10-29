from flask import Flask
import speech_recognition as sr
import keyboard
from gtts import gTTS
import os

app = Flask(__name__)

# Criação de um reconhecedor
r = sr.Recognizer()

# Lista para armazenar os produtos
produtos = []

@app.route('/start-speech-recognition', methods=['GET'])
def start_speech_recognition():
    global produtos

    def ouvir_e_armazenar():
        global produtos
        with sr.Microphone() as source:
            print("Fale agora. Solte o botão quando terminar.")
            audio = r.listen(source, phrase_time_limit=5)

            try:
                # Google Speech Recognition para converter a fala em texto
                produto = r.recognize_google(audio)
                print("Produto: " + produto)
                produtos.append(produto)
            except sr.UnknownValueError:
                mensagem = "Não foi possível entender o áudio"
                print(mensagem)
                tts = gTTS(text=mensagem, lang='pt')
                tts.save("mensagem.mp3")
                os.system("afplay mensagem.mp3")  # Isso funciona em sistemas macOS
                #os.system("start mensagem.mp3")  # Windows
            except sr.RequestError as e:
                mensagem = "Erro ao chamar o serviço de reconhecimento de fala"
                print(mensagem, e)
                tts = gTTS(text=mensagem, lang='pt')
                tts.save("mensagem.mp3")
                os.system("afplay mensagem.mp3") 
                #os.system("start mensagem.mp3") 

    def pressionar_tecla():
        # "lambda" argumento para o método on_press_key (gatilho)
        keyboard.on_press_key('enter', lambda _: ouvir_e_armazenar())
        keyboard.wait('esc')
        keyboard.unhook_all()

    # Pressione 'Enter' para começar a capturar a fala e 'Esc' para parar
    pressionar_tecla()

    return "Lista de produtos: " + str(produtos)

if __name__ == '__main__':
    app.run(debug=True)
