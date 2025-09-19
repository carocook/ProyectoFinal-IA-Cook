from generador_texto import model

def optimizar_prompt_imagen(descripcion):
    prompt = f"Eres un asistente creativo de ciberseguridad. Transforma esta descripción en un prompt detallado para generar una imagen educativa y profesional: {descripcion}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al optimizar prompt: {e}"

def generar_imagen_manual(prompt_optimizado):
    print("Usar el siguiente prompt en NightCafe o Stable Diffusion para generar la imagen:")
    print(prompt_optimizado)
