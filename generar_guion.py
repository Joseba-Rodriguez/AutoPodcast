from transformers import pipeline

def generar_guion(tema):
    print(f"Generating script about: {tema}")
    generador = pipeline("text-generation", model="gpt2", pad_token_id=50256)

    # Generar el prompt automáticamente basado en el tema, con un enfoque experto pero accesible
    prompt_inicial = f"Generate a podcast introduction about {tema}, as if it were an expert explaining it in simple terms, with a deep understanding of the subject but avoiding technical jargon."

    # Generar el texto del guion, asegurándonos de que el experto tenga un enfoque claro y accesible
    prompt = generador(prompt_inicial, max_length=150, num_return_sequences=1, temperature=0.7, top_p=0.9, truncation=True)[0]['generated_text']
    
    # Asegurar que el prompt generado se vea realista
    prompt = prompt.strip().replace('\n', ' ')  # Limpiar el texto generado

    # Crear un guion más extenso y detallado sobre el tema
    prompt_completo = f"""Podcast about {tema}, featuring an expert speaking on the topic:

    {prompt}

    Let's break it down in simple terms. {tema} is something that affects our daily lives more than we realize. It might sound complicated at first, but if we take a closer look, we see that its principles are really about making things more efficient and accessible.

    Over time, {tema} has evolved, but its core purpose has remained the same: to simplify and improve the way we do things. Whether it’s in the workplace or at home, understanding {tema} can help us solve problems and make better decisions.

    So, what exactly is {tema}, and why is it so important in today's world? Let's explore that now.
    """

    # Generar un guion más largo y detallado basado en el prompt inicial
    guion = generador(prompt_completo, max_length=1024, num_return_sequences=1, temperature=0.85, top_p=0.95, top_k=50, truncation=True)

    # Guardar el guion generado en un archivo de texto
    with open("podcast_script.txt", "w", encoding="utf-8") as f:
        f.write(guion[0]['generated_text'])

    print("Script saved to 'podcast_script.txt'.")

if __name__ == "__main__":
    tema = input("Enter the topic of the podcast: ")
    generar_guion(tema)
