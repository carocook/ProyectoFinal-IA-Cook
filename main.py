from generador_texto import generar_escenario_ataque, explicar_defensa, evaluar_respuesta_usuario
from generador_imagen import optimizar_prompt_imagen, generar_imagen_manual
import os

# Crear carpetas si no existen
os.makedirs("resultados", exist_ok=True)
os.makedirs("imagenes_generadas", exist_ok=True)

# Ejemplo de uso
if __name__ == "__main__":
    ataque = "phishing targeting corporate emails"
    defensa = "uso de filtros de correo y educación al usuario"
    respuesta_usuario = "Creo que bloquear el correo es suficiente para evitar phishing"

    # Generar escenario de ataque
    escenario = generar_escenario_ataque(ataque)
    print("ESCENARIO DE ATAQUE:\n", escenario, "\n")
    with open("resultados/escenario_phishing.txt", "w", encoding="utf-8") as f:
        f.write(escenario)

    # Explicar técnica de defensa
    explicacion = explicar_defensa(defensa)
    print("EXPLICACIÓN DE DEFENSA:\n", explicacion, "\n")
    with open("resultados/defensa_filtros.txt", "w", encoding="utf-8") as f:
        f.write(explicacion)

    # Evaluar respuesta del usuario
    evaluacion = evaluar_respuesta_usuario(respuesta_usuario)
    print("EVALUACIÓN DE RESPUESTA DEL USUARIO:\n", evaluacion, "\n")
    with open("resultados/evaluacion_usuario.txt", "w", encoding="utf-8") as f:
        f.write(evaluacion)

    # Optimizar prompt de imagen
    descripcion_imagen = "Ilustración de un ataque de phishing con computadora y alerta de seguridad"
    prompt_optimizado = optimizar_prompt_imagen(descripcion_imagen)
    print("\nUsa este prompt en NightCafe o Stable Diffusion:")
    print(prompt_optimizado)

    
    # Guardar prompt optimizado
with open("resultados/prompt_imagen_phishing.txt", "w", encoding="utf-8") as f:
    f.write(prompt_optimizado)
