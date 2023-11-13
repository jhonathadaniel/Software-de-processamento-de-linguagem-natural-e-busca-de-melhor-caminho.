import unittest
from unittest.mock import patch, mock_open, MagicMock
import speech_recognition as sr
from appTest import listen_microfone

class TestListenMicrofone(unittest.TestCase):

    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Recognizer.recognize_google')
    @patch('builtins.open', new_callable=mock_open)
    def test_listen_microfone(self, mock_open, mock_recognize_google, mock_listen):
        # Simula a criação de um objeto AudioData válido
        fake_audio_data = MagicMock(spec=sr.AudioData)
        fake_audio_data.get_wav_data.return_value = b'fake_audio_data'
        fake_audio_data.sample_rate = 44100
        fake_audio_data.sample_width = 2

        mock_recognize_google.return_value = 'Olá, isso é um teste'
        mock_listen.return_value = fake_audio_data

        result = listen_microfone()

        mock_open.assert_called_once_with('recordings/speech.wav', 'wb')
        mock_open().write.assert_called_once_with(b'fake_audio_data')

        self.assertEqual(result, ['Olá, isso é um teste'])

if __name__ == '__main__':
    unittest.main()
