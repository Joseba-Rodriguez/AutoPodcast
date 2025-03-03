import edge_tts
import asyncio

async def generar_audio():
    try:
        # Leer el guion del archivo de texto
        with open("podcast_script.txt", "r", encoding="utf-8") as f:
            texto = f.read()

        # Crear el SSML para generar el audio con una sola voz más amigable
        ssml_text = f"""
        <speak>
            <voice name="en-US-JennyNeural">
                <prosody rate="5%" pitch="10%">
                    {texto}
                </prosody>
            </voice>
        </speak>
        """

        print("Generando audio con Edge-TTS...")
        tts = edge_tts.Communicate(ssml_text, voice="en-US-JennyNeural")  # Usamos una voz más amigable
        await tts.save("podcast_experto_ingles.mp3")
        print("Podcast guardado en 'podcast_experto_ingles.mp3'.")
    except edge_tts.exceptions.NoAudioReceived as e:
        print("Error: No audio received. Please check the SSML format or voice parameters.")
        print(str(e))
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    asyncio.run(generar_audio())
