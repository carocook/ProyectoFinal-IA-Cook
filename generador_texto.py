import google.generativeai as genai

# Configurar la API Key
genai.configure(api_key="AIzaSyApWIUOfP0MSYAoVw4KB8Ded23uZ2X8TOg")
model = genai.GenerativeModel('gemini-1.5-flash')

# Contexto
context = "Eres un experto en ciberseguridad que explica ataques y defensas, genera escenarios educativos y evalúa la comprensión del usuario."

def generar_escenario_ataque(descripcion_ataque):
    prompt = f"Eres un experto en ciberseguridad. Describe un ataque de {descripcion_ataque} paso a paso y cómo detectarlo."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al generar escenario: {e}"

def explicar_defensa(tecnica):
    prompt = f"Eres un experto en ciberseguridad. Explica cómo funciona la defensa: {tecnica}. Incluye pasos prácticos y buenas prácticas."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al explicar defensa: {e}"

def evaluar_respuesta_usuario(respuesta_usuario):
    prompt = f"Eres un experto en ciberseguridad. Evalúa la siguiente respuesta de un usuario: '{respuesta_usuario}'. Indica aciertos, errores y cómo mejorar con ejemplos prácticos."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al evaluar respuesta: {e}"
