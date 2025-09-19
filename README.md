# Asistente de Ciberseguridad Interactivo

## Resumen

El Asistente de Ciberseguridad Interactivo es un proyecto orientado a la ciberseguridad que utiliza modelos de inteligencia artificial para generar escenarios educativos sobre ataques y defensas informáticas. El objetivo es facilitar la comprensión de amenazas complejas mediante la combinación de texto y visualizaciones generadas automáticamente a partir de prompts optimizados.

El proyecto permite crear escenarios de ataques como phishing o ransomware, explicar técnicas de defensa, evaluar respuestas de usuarios y generar prompts visuales para ilustrar los ataques, usando herramientas de Fast Prompting.

## Introducción

**Nombre del proyecto:** Asistente de Ciberseguridad Interactivo

### Presentación del problema a abordar

En ciberseguridad, muchas veces los equipos técnicos necesitan explicar de manera clara y visual los ataques y vulnerabilidades a usuarios o directivos que no poseen conocimientos técnicos. La falta de herramientas educativas precisas dificulta la comunicación, aumentando riesgos de errores y retrasos en la toma de decisiones frente a incidentes reales.

Este proyecto aborda esa problemática generando escenarios educativos y visualizaciones a partir de texto descriptivo, ayudando a comprender mejor los ataques y las defensas asociadas.

### Desarrollo de la propuesta de solución

El Asistente de Ciberseguridad Interactivo utiliza modelos de inteligencia artificial (Gemini) para optimizar prompts y generar contenido textual y visual. Los pasos principales incluyen:

1. **Generación de escenarios de ataque:** Se crea un escenario detallando paso a paso un ataque y su detección.
2. **Explicación de técnicas de defensa:** Se generan descripciones claras de cómo implementar medidas de protección.
3. **Evaluación de respuestas de usuarios:** Se analiza si las respuestas a preguntas de ciberseguridad son correctas y se sugieren mejoras.
4. **Optimización de prompts para imágenes:** Se transforma la descripción textual en un prompt listo para herramientas como NightCafe o Stable Diffusion, generando imágenes educativas de los ataques.

### Justificación de la viabilidad del proyecto

El proyecto es técnicamente viable porque:

- Se basa en modelos de IA accesibles mediante API o herramientas gratuitas.
- Requiere recursos computacionales mínimos, ya que la generación de imágenes se realiza externamente.
- El tiempo de desarrollo es acotado y se ajusta al alcance de una POC educativa.
- Las funciones de generación y evaluación de prompts se pueden automatizar fácilmente en Python.

---

## Objetivos

- Generar escenarios educativos de ataques y defensas en ciberseguridad.
- Optimizar prompts para crear imágenes representativas de los ataques.
- Evaluar respuestas de usuarios y sugerir mejoras.
- Integrar todo en un flujo de trabajo reproducible y documentado.

---

## Metodología

1. **Diseño de funciones en Python:** Se crean funciones para generar escenarios, explicar defensas, evaluar respuestas y optimizar prompts.
2. **Uso de Fast Prompting:** Se generan prompts detallados y optimizados para la creación de imágenes y texto educativo.
3. **Prueba y validación:** Cada función se prueba con ejemplos de ataques reales o simulados, verificando la claridad y utilidad de los resultados.
4. **Registro de resultados:** Textos y prompts se guardan en archivos `.txt` y las imágenes generadas se almacenan en la carpeta `imagenes_generadas/`.

---

## Herramientas y tecnologías

- **Python 3.13** como lenguaje principal.
- **Google Gemini** para generación de texto y optimización de prompts.
- **NightCafe o Stable Diffusion** para la creación de imágenes educativas a partir de prompts optimizados.
- **Fast Prompting:** técnica utilizada para refinar los prompts y obtener contenido preciso y educativo de manera eficiente.

---

Las funciones en Python se ejecutan en Visual Studio, generando:

- Escenarios de ataque en texto (`resultados/escenario_phishing.txt`).
- Explicaciones de defensas (`resultados/defensa_filtros.txt`).
- Evaluación de respuestas (`resultados/evaluacion_usuario.txt`).
- Prompts optimizados para imágenes (`resultados/prompt_imagen_phishing.txt`).

Las imágenes se descargan de NightCafe o Stable Diffusion y se guardan en `imagenes_generadas/`.

---

## Resultados

- La implementación genera escenarios claros y detallados sobre ataques de ciberseguridad.
- Los prompts optimizados permiten producir imágenes educativas que representan los ataques.
- La evaluación de respuestas de usuarios proporciona retroalimentación útil y ejemplos prácticos.
- Se logra cumplir con los objetivos de explicar, visualizar y evaluar conocimientos en ciberseguridad de manera automatizada.

---

## Conclusiones

- El Asistente de Ciberseguridad Interactivo facilita la comprensión de ataques y defensas, combinando texto e imágenes generadas por IA.
- Se lograron los objetivos propuestos: generación de escenarios, optimización de prompts y evaluación de respuestas.
- La solución es escalable y puede ampliarse a más tipos de ataques o integrarse en plataformas educativas.
- El proyecto demuestra cómo Fast Prompting y herramientas de IA pueden apoyar la enseñanza y comunicación en ciberseguridad.
