#  Evaluación de un LLM en Raspberry Pi 5

Este documento recoge pruebas realizadas ejecutando el modelo **gemma4:e2b** en una **Raspberry Pi 5** mediante Ollama.

---

#  RESULTADOS COMPLETOS DE LAS PRUEBAS

##  Configuración del entorno

- Modelo: gemma4:e2b  
- Ejecución: ollama run gemma4:e2b --think=false --verbose  

---

##  1. Pregunta generalista

### Entrada
>>> a que distancia está la luna de aquí?

### Respuesta del modelo
Para poder decirte a qué distancia está la Luna de "aquí", necesito saber dónde te encuentras.
La distancia promedio desde la Tierra a la Luna es de aproximadamente 384,400 kilómetros.
Si me dices tu ciudad o ubicación, puedo darte una estimación más contextual.

### Métricas
total duration: 26.182179211s  
load duration: 698.987898ms  
prompt eval count: 18 tokens  
prompt eval duration: 7.292594169s  
prompt eval rate: 2.47 tokens/s  
eval count: 96 tokens  
eval duration: 17.499779678s  
eval rate: 5.49 tokens/s  

---

##  2. Extracción de información

### Entrada
>>> Las declaraciones de contribución del autor y los agradecimientos en los documentos de
... investigación deben indicar claramente y específicamente si, y en qué medida, los autores
... utilizaron tecnologías de inteligencia artificial como ChatGPT en la preparación de su
... manuscrito y análisis. También deben indicar qué LLMs se utilizaron. Esto alertará a los
... editores y revisores para examinar los manuscritos con más cuidado en busca de posibles
... prejuicios, inexactitudes e improperios en la atribución de fuentes. De igual manera, las
... revistas científicas deben ser transparentes sobre su uso de LLM, por ejemplo, al seleccionar
... manuscritos enviados.
... Menciona el producto basado en el modelo de lenguaje grande mencionado en el párrafo anterior:

### Respuesta del modelo
LLMs (Modelos de Lenguaje Grande)

### Métricas
total duration: 17.790315907s  
load duration: 518.167286ms  
prompt eval count: 1510 tokens  
prompt eval duration: 15.137351027s  
prompt eval rate: 99.75 tokens/s  
eval count: 11 tokens  
eval duration: 2.095825953s  
eval rate: 5.25 tokens/s  

---

##  3. QA con contexto

### Entrada
>>> Responde la pregunta basándote en el contexto que aparece a continuación. Mantén la respuesta
... corta y concisa. Responde "No estoy seguro de la respuesta" si no estás seguro de la respuesta.
... Context: Teplizumab tiene sus raíces en una empresa farmacéutica de Nueva Jersey llamada Ortho
... Pharmaceutical. Allí, los científicos generaron una versión temprana del anticuerpo, apodado OKT3.
... Originalmente obtenido de ratones, la molécula era capaz de unirse a la superficie de las células T
... y limitar su potencial de matar células. En 1986, fue aprobado para ayudar a prevenir el rechazo
... de órganos después de los trasplantes de riñón, convirtiéndose en el primer anticuerpo terapéutico
... permitido para uso humano.
... Question: ¿De dónde se obtuvo originalmente el OKT3?

### Respuesta del modelo
De ratones.

### Métricas
total duration: 44.243154021s  
load duration: 16.742377619s  
prompt eval count: 301 tokens  
prompt eval duration: 26.07988919s  
prompt eval rate: 11.54 tokens/s  
eval count: 5 tokens  
eval duration: 0.800983271s  
eval rate: 6.24 tokens/s  

---

##  4. Generación de código

### Entrada
>>> """
... Table departments, columns = [DepartmentId, DepartmentName]
... Table students, columns = [DepartmentId, StudentId, StudentName]
... Create a MySQL query for all students in the Computer Science Department
"""

### Respuesta del modelo
SELECT T1.StudentName  
FROM students AS T1  
INNER JOIN departments AS T2  
ON T1.DepartmentId = T2.DepartmentId  
WHERE T2.DepartmentName = 'Computer Science';

### Métricas
total duration: 16.219864718s  
load duration: 504.476273ms  
prompt eval count: 801 tokens  
prompt eval duration: 4.292517628s  
prompt eval rate: 186.60 tokens/s  
eval count: 53 tokens  
eval duration: 11.339767507s  
eval rate: 4.67 tokens/s  

---

##  5. Traducción multilingüe

### Español → Ruso
- No se mueva → Не двигайтесь  
- Mantenga la calma → Пожалуйста, сохраняйте спокойствие  

### Español → Chino
- No se mueva → 不要动  
- Mantenga la calma → 请保持冷静  

### Español → Árabe
- No se mueva → لا تتحرك  
- Mantenga la calma → من فضلك، اهدأ  

### Métricas
total duration: 1m7.321350102s  
load duration: 502.485546ms  
prompt eval count: 347 token(s)  
prompt eval duration: 17.383253151s  
prompt eval rate: 19.96 tokens/s  
eval count: 248 tokens  
eval duration: 49.116385814s  
eval rate: 5.05 tokens/s  

---
