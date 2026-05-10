#  Evaluación de un VLM en Raspberry Pi 5

Este documento recoge una prueba de un modelo Vision-Language Model (VLM) ejecutado en una Raspberry Pi 5 utilizando Python y Ollama.

---

##  Configuración del entorno

- Dispositivo: Raspberry Pi 5  
- Lenguaje: Python 3  
- Entorno: venv  
- Librerías: opencv-python, ollama  
- Modelo VLM: moondream  

---

##  Script utilizado

```python
import cv2
import ollama

IMG_PATH = "captura.jpg"
MODEL = "moondream"

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se puede abrir la cámara")
    exit()
ret, frame = cap.read()

if ret:
    frame = cv2.resize(frame, (224, 224))
    cv2.imwrite(IMG_PATH, frame)
    print("Imagen capturada:", IMG_PATH)
else:
    print("Error al capturar imagen")
    cap.release()
    exit()

cap.release()

with open(IMG_PATH, 'rb') as f:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                'role': 'user',
                'content': 'Describe lo que ves de forma breve',
                'images': [f.read()],
            }
        ],
        options={
            'temperature': 0,
            'num_predict': 25
        }
    )

print("\nDescripción:")
print(response['message']['content'])
print(f"\nTiempo: {response['total_duration']/1e9:.2f} segundos")
```

---

##  Resultado de ejecución

###  Captura
Imagen capturada: captura.jpg

---

###  Respuesta del modelo
The image shows a laptop screen displaying an illustration of a police car. The computer monitor is turned on, and the screen

---

###  Métrica de rendimiento
Tiempo total: 72.17 segundos

---

##  Observaciones

- [X] Procesamiento de imagen desde webcam funcional  
- [X] Descripción coherente del contenido visual  
- [] Salida truncada por límite de tokens  
- [] Latencia elevada en Raspberry Pi  

---

##  Conclusiones

- El modelo moondream es viable en Raspberry Pi 5  
- Útil para prototipos de visión + lenguaje  
- Limitado por rendimiento y tiempo de respuesta  

---

##  Recomendaciones

- Aumentar num_predict para mejorar descripciones  
- Optimizar resolución de entrada  
- Evaluar modelos más ligeros o cuantizados

