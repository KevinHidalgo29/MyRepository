# Respuestas a Preguntas Teóricas

## 1. Usos de Python en el manejo de datos
Python es un lenguaje de programación muy versátil que se utiliza en diferentes áreas relacionadas con los datos.:
- **Análisis de Datos**: Python se usa ampliamente en análisis de datos debido a bibliotecas como Pandas y NumPy, que permiten manipular y analizar grandes conjuntos de datos de manera eficiente.
- **Visualización de Datos**: Con bibliotecas como Matplotlib y Seaborn, Python permite crear gráficos y visualizaciones que ayudan a interpretar datos complejos y presentan la información de manera visual.
- **Aprendizaje Automático (Machine Learning)**: Python se utiliza para desarrollar modelos de aprendizaje automático utilizando bibliotecas como Scikit-learn y TensorFlow, permitiendo hacer predicciones y clasificaciones a partir de datos.
- **Desarrollo Web**: Python, junto con frameworks como Flask y Django, se utiliza para construir aplicaciones web que pueden manejar y procesar datos en tiempo real.
- **Automatización de Tareas**: Python se puede utilizar para automatizar tareas repetitivas relacionadas con datos, como la limpieza de datos, la recopilación de datos de diferentes fuentes, y la generación de informes.


## 2. Diferencias entre Flask y Django

Flask y Django son dos frameworks populares de Python para el desarrollo web, pero tienen diferencias significativas:

- **Estructura y Flexibilidad**: Django es un framework "baterías incluidas" que ofrece una estructura completa y muchas funcionalidades integradas, como autenticación, administración y ORM (Object-Relational Mapping). Por otro lado, Flask es más minimalista y permite al desarrollador elegir cómo quiere estructurar su aplicación y qué bibliotecas usar.
- **Facilidad de Aprendizaje**: Flask es más fácil de aprender para los principiantes debido a su simplicidad y menor cantidad de características. Django, aunque más robusto, puede ser más desafiante para quienes están comenzando.
- **Rendimiento**: En general, Flask puede ser más rápido para aplicaciones más simples, mientras que Django puede ser más lento debido a su sobrecarga de funcionalidades integradas.
- **Comunidad y Ecosistema**: Django tiene una comunidad más grande y un ecosistema más maduro, lo que significa que hay más paquetes y extensiones disponibles. Flask, aunque tiene una buena comunidad, es más pequeño en comparación.
- **Uso**: Django es ideal para aplicaciones grandes y complejas que requieren muchas funcionalidades, mientras que Flask es más adecuado para aplicaciones más pequeñas o microservicios.


## 3. ¿Qué es un API?

Una API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y protocolos que permite que diferentes aplicaciones se comuniquen entre sí. En términos simples, es una forma en que un programa puede interactuar con otro, solicitando o enviando datos. Las APIs son esenciales para integrar diferentes sistemas y permitir que trabajen juntos, facilitando el acceso a funciones y datos de una aplicación desde otra.


## 4. Diferencia principal entre REST y WebSockets

La principal diferencia entre REST y WebSockets radica en el modo de comunicación. REST es un estilo arquitectónico que utiliza solicitudes HTTP para enviar y recibir datos. Cada interacción es independiente, lo que significa que el cliente debe solicitar datos activamente. En cambio, WebSockets permite una comunicación bidireccional en tiempo real entre el cliente y el servidor, lo que significa que el servidor puede enviar datos al cliente sin que este lo solicite. Esto es útil para aplicaciones que requieren actualizaciones en tiempo real, como chats o notificaciones en vivo.

## 5. Ejemplo de API Comercial

Un ejemplo de API comercial es la API de Twilio, que permite a los desarrolladores integrar funciones de mensajería y llamadas de voz en sus aplicaciones. Twilio proporciona endpoints para enviar mensajes de texto, realizar llamadas, y recibir información sobre el estado de las comunicaciones. Por ejemplo, un desarrollador puede usar la API de Twilio para crear un sistema de alertas por SMS en su aplicación, enviando mensajes automáticamente cuando ocurren ciertos eventos, como el cambio de estado de un pedido. Twilio se encarga de toda la infraestructura de mensajería y comunicación, permitiendo a los desarrolladores centrarse en construir su aplicación.