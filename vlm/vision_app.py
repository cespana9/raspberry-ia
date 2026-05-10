import cv2
import ollama

IMG_PATH = "captura.jpg"
MODEL = "moondream"

# Capturar imagen desde webcam USB
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

# Enviar a IA
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

print("\n Descripción:")
print(response['message']['content'])

print(f"\n Tiempo: {response['total_duration']/1e9:.2f} segundos")
