# Ejercicios Prácticos Tema 3 - Unidad 2, Sesión 1
## Fundamentos de Prompt Engineering

---

## Ejercicio 1: Anatomía de un Prompt

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de teoría sobre componentes del prompt

### Contexto
Antes de crear buenos prompts, es importante reconocer los componentes en prompts existentes.

### Objetivo de Aprendizaje
- Identificar los componentes de un prompt (rol, contexto, tarea, formato, restricciones)
- Evaluar la completitud de un prompt

### Enunciado
Analiza los siguientes prompts e identifica sus componentes. Indica qué componentes faltan y como los mejorarías.

### Prompt A
```
Eres un experto en marketing digital especializado en startups tecnológicas.

Contexto: Nuestra startup vende software de gestión de proyectos para equipos remotos.
Acabamos de lanzar una nueva funcionalidad de videoconferencias integradas.

Tarea: Escribe 3 posts para LinkedIn anunciando esta funcionalidad.

Formato:
- Cada post debe tener entre 100-150 palabras
- Incluir un emoji relevante al inicio
- Terminar con un call-to-action

No menciones competidores ni uses jerga demasiado técnica.
```

### Prompt B
```
Dame ideas para mejorar mi aplicación
```

### Prompt C
```
Traduce este texto al inglés y hazlo más formal:

"""
Hola! Queria saber si podemos quedar mañana para hablar del proyecto.
Avisame cuando puedas.
"""
```

### Tabla de Análisis

Completa la siguiente tabla para cada prompt:

| Componente | Prompt A | Prompt B | Prompt C |
|------------|----------|----------|----------|
| Rol | Experto en marketing digital especializado en startups tecnológicas | No especificado | No especificado |
| Contexto | Startup vende software de gestión de proyectos para equipos remotos; nueva funcionalidad de videoconferencias | No especificado | Texto informal para coordinar una reunión sobre un proyecto |
| Tarea | Escribir 3 posts para LinkedIn anunciando la funcionalidad | Dar ideas para mejorar una aplicación | Traducir y formalizar un texto al inglés |
| Formato | Cada post: 100-150 palabras, emoji al inicio, call-to-action al final | No especificado | No especificado |
| Restricciones | No mencionar competidores ni usar jerga técnica | No especificado | No especificado |
| Ejemplos | No incluye ejemplos | No incluye ejemplos | Incluye ejemplo de texto a traducir |
| **Evaluación (1-10)** | 9 | 3 | 7 |

### Preguntas de Reflexión
1. ¿Cuál de los tres prompts producirá mejores resultados? ¿Por qué?

Sin duda el primer prompt va a dar los mejores resultados, porque está muy bien detallado: explica quién eres, el contexto, lo que se espera y hasta cómo debe ser la respuesta. Cuanta más información y claridad le das a la IA, más fácil es que entienda lo que necesitas y te dé justo lo que buscas.

2. ¿Qué añadirías al Prompt B para hacerlo efectivo?

Le falta casi todo: empezaría por decirle a la IA quién es (por ejemplo, "Eres un experto en desarrollo de apps"), explicaría de qué trata la aplicación y para qué quieres mejorarla, y le daría alguna pista sobre el tipo de ideas que buscas. Incluso un ejemplo ayudaría mucho. Así la respuesta será mucho más útil y concreta.

3. ¿El Prompt C necesita rol? ¿Por qué sí o por qué no?
No es estrictamente necesario, pero si le das un rol (por ejemplo, "Eres un traductor profesional" o "Eres un profesor de inglés"), la respuesta suele ser más precisa y adaptada al tono que buscas. Si solo quieres una traducción básica, puede funcionar sin rol, pero si buscas un estilo o nivel concreto, el rol ayuda mucho.

Si necesitas. Puedes decir que eres un profesor de ingles con nivel 2 en su proyecto

---

## Ejercicio 2: Zero-shot vs Few-shot

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Experimentación
- **Modalidad**: Individual
- **Dificultad**: Intermedia
- **Prerequisitos**: Acceso a ChatGPT, Claude o Gemini

### Contexto
Comparar el rendimiento de diferentes técnicas de prompting en una tarea de clasificación.

### Objetivo de Aprendizaje
- Experimentar con zero-shot y few-shot prompting
- Comparar resultados y entender cuándo usar cada técnica

### Enunciado
Vas a clasificar sentimientos de reseñas de productos usando tres enfoques diferentes.

### Parte A: Zero-shot (10 min)

Usa el siguiente prompt con 5 reseñas de prueba:

```
Clasifica el sentimiento de la siguiente reseña como: Positivo, Negativo o Neutro.

Reseña: "[INSERTAR RESEÑA]"

Sentimiento:
```

**Reseñas de prueba:**
1. "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."
2. "No funciona como esperaba. Devolución solicitada."
3. "Esta bien para el precio. Hace lo que promete, nada más."
4. "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."
5. "HORRIBLE. Peor compra de mi vida. NO COMPREN."

### Parte B: Few-shot (15 min)


Prompt few-shot:

```
Clasifica el sentimiento de reseñas de productos.

Ejemplos:
Reseña: "Me encantó el producto, llegó rápido y funciona perfecto."
Sentimiento: Positivo

Reseña: "No me gustó, vino roto y el soporte no respondió."
Sentimiento: Negativo

Reseña: "Cumple con lo que promete, nada especial."
Sentimiento: Neutro

Ahora clasifica:
Reseña: "[RESEÑA DE PRUEBA]"
Sentimiento:
```

Clasificación de las reseñas:

1. "Excelente producto, superó mis expectativas. Lo recomiendo totalmente."
	- Zero-shot: Positivo
	- Few-shot: Positivo
	- ¿Coinciden?: Sí
2. "No funciona como esperaba. Devolución solicitada."
	- Zero-shot: Negativo
	- Few-shot: Negativo
	- ¿Coinciden?: Sí
3. "Esta bien para el precio. Hace lo que promete, nada más."
	- Zero-shot: Neutro
	- Few-shot: Neutro
	- ¿Coinciden?: Sí
4. "Llegó rápido pero la caja estaba dañada. El producto funciona correctamente."
	- Zero-shot: Neutro
	- Few-shot: Neutro
	- ¿Coinciden?: Sí
5. "HORRIBLE. Peor compra de mi vida. NO COMPREN."
	- Zero-shot: Negativo
	- Few-shot: Negativo
	- ¿Coinciden?: Sí

### Parte C: Comparación (5 min)


| Reseña | Zero-shot | Few-shot | ¿Coinciden? |
|--------|-----------|----------|-------------|
| 1 | Positivo | Positivo | Sí |
| 2 | Negativo | Negativo | Sí |
| 3 | Neutro   | Neutro   | Sí |
| 4 | Neutro   | Neutro   | Sí |
| 5 | Negativo | Negativo | Sí |

### Preguntas

1. ¿Hubo diferencias en los resultados? ¿Cuáles?
En este caso, los resultados fueron iguales en ambos enfoques porque las reseñas son bastante claras y directas. Sin embargo, en casos más ambiguos, el few-shot suele ayudar a que la IA entienda mejor los matices.

2. ¿La reseña 4 fue difícil de clasificar? ¿Por qué?
Un poco, porque mezcla algo negativo (la caja dañada) con algo positivo (el producto funciona). Pero como el producto cumple su función, lo más razonable es considerarla neutra.

3. ¿Qué técnica usarías en producción? ¿Por qué?
Usaría el few-shot, porque al dar ejemplos concretos la IA suele ser más consistente y entiende mejor los criterios de clasificación, sobre todo cuando las reseñas no son tan evidentes.

---

## Ejercicio 3: Desarrollo Iterativo de Prompts

### Metadata
- **Duración estimada**: 35 minutos
- **Tipo**: Programación/Iteración
- **Modalidad**: Parejas
- **Dificultad**: Intermedia
- **Prerequisitos**: Acceso a un LLM

### Contexto
El desarrollo iterativo es la clave del Prompt Engineering profesional. Vamos a practicar el ciclo completo.

### Objetivo de Aprendizaje
- Aplicar el proceso iterativo de mejora de prompts
- Documentar cambios y su impacto

### Enunciado
Desarrolla un prompt para generar descripciones de productos para e-commerce.

### Escenario
Trabajas en una tienda online de electrónica. Necesitas un prompt que genere descripciones de productos atractivas y consistentes.

**Producto de prueba:**
```
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de bateria (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

### Iteración 1: Prompt Básico

```
Escribe una descripción para este producto:
[datos del producto]
```

- Prueba el prompt y pega la respuesta
- ¿Qué problemas identificas?

### Iteración 2: Añadir Estructura

Mejora el prompt añadiendo:
- Formato de salida específico
- Longitud deseada

Documenta:
- Tu nuevo prompt
- La respuesta obtenida
- ¿Qué mejoro?

### Iteración 3: Añadir Contexto y Tono

Mejora añadiendo:
- Audiencia objetivo
- Tono de la marca
- Elementos que debe incluir (beneficios, no solo características)

### Iteración 4: Refinamiento Final

Ajusta para:
- Incluir call-to-action
- Añadir restricciones (evitar ciertas palabras, longitud exacta)
- Optimizar para SEO (si aplica)

### Entregable

#### 1. Los 4 prompts (uno por iteración)

**Iteración 1: Prompt Básico**
```
Escribe una descripción para este producto:
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de batería (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

**Iteración 2: Añadir Estructura**
```
Escribe una descripción de máximo 80 palabras para el siguiente producto de e-commerce. Usa un párrafo breve y claro.
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de batería (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

**Iteración 3: Añadir Contexto y Tono**
```
Eres redactor de una tienda online de electrónica. Escribe una descripción atractiva y persuasiva para potenciales compradores jóvenes y techies. Usa un tono cercano y resalta beneficios, no solo características. Máximo 80 palabras.
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de batería (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

**Iteración 4: Refinamiento Final**
```
Eres redactor de una tienda online de electrónica. Escribe una descripción para el producto "EchoBuds Pro X3" dirigida a jóvenes techies. Usa un tono cercano, resalta beneficios (no solo características), incluye un call-to-action al final, evita la palabra "barato" y limita la descripción a exactamente 70 palabras. Optimiza el texto para SEO usando términos como "auriculares inalámbricos", "cancelación de ruido" y "batería de larga duración".
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de batería (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

#### 2. Las 4 respuestas obtenidas (simuladas)

**Iteración 1:**
"Los EchoBuds Pro X3 son auriculares inalámbricos con cancelación de ruido activa, 30 horas de batería, resistencia al agua IPX5 y Bluetooth 5.3. Incluyen 3 tamaños de almohadillas para mayor comodidad."

**Problemas:** Muy genérica, solo lista características, poco atractiva.

**Iteración 2:**
"Descubre los EchoBuds Pro X3: auriculares inalámbricos con cancelación de ruido activa, hasta 30 horas de batería y resistencia al agua IPX5. Disfruta de tu música sin interrupciones y con máxima comodidad gracias a sus almohadillas intercambiables."

**Mejora:** Más clara y estructurada, pero aún centrada en características.

**Iteración 3:**
"Lleva tu música a otro nivel con los EchoBuds Pro X3. Olvídate del ruido y sumérgete en un sonido puro, con batería para todo el día y resistencia al agua. Perfectos para tu ritmo de vida, se adaptan a ti con sus almohadillas personalizables."

**Mejora:** Más beneficios, tono más cercano y persuasivo.

**Iteración 4:**
"Los EchoBuds Pro X3 son los auriculares inalámbricos ideales para jóvenes techies: disfruta de cancelación de ruido, batería de larga duración y resistencia al agua. Vive tu música sin límites y con total comodidad. ¡Hazte con los tuyos y experimenta el siguiente nivel de sonido!"

**Mejora:** Incluye call-to-action, optimización SEO, tono adecuado y longitud precisa.

#### 3. Análisis de qué cambio tuvo mayor impacto

El mayor salto de calidad se da en la tercera iteración, al añadir contexto, audiencia y beneficios. El texto pasa de ser una simple lista de características a una propuesta atractiva para el cliente. La cuarta iteración pule detalles importantes para e-commerce (SEO, call-to-action, restricciones), pero la clave está en adaptar el mensaje al público y resaltar cómo el producto mejora su vida.

#### 4. Prompt final recomendado

```
Eres redactor de una tienda online de electrónica. Escribe una descripción para el producto "EchoBuds Pro X3" dirigida a jóvenes techies. Usa un tono cercano, resalta beneficios (no solo características), incluye un call-to-action al final, evita la palabra "barato" y limita la descripción a exactamente 70 palabras. Optimiza el texto para SEO usando términos como "auriculares inalámbricos", "cancelación de ruido" y "batería de larga duración".
Nombre: EchoBuds Pro X3
Tipo: Auriculares inalambricos
Precio: 149.99€
Características:
- Cancelación de ruido activa
- 30 horas de batería (con estuche)
- Resistentes al agua IPX5
- Bluetooth 5.3
- Incluye 3 tamaños de almohadillas
```

---

## Ejercicio 4: Diseño de Prompts para Casos de Uso

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Diseño
- **Modalidad**: Grupal (3-4 personas)
- **Dificultad**: Intermedia
- **Prerequisitos**: Comprensión de componentes del prompt

### Contexto
En equipos, diseñaran prompts para casos de uso empresariales reales.

### Objetivo de Aprendizaje
- Aplicar los componentes del prompt a problemas reales
- Colaborar en el diseño y crítica de prompts

### Enunciado
Cada grupo recibira un caso de uso y deberá diseñar el prompt completo.

### Caso A: Generador de Emails de Seguimiento

**Contexto del problema:**
Un equipo de ventas necesita enviar emails de seguimiento personalizados después de demos de producto.

**Input disponible:**
- Nombre del prospecto
- Empresa
- Puntos discutidos en la demo
- Objeciones mencionadas
- Siguiente paso acordado

**Output deseado:**
Email profesional, personalizado, que refuerce los puntos fuertes y aborde las objeciones.

### Caso B: Resumidor de Reuniones

**Contexto del problema:**
Un asistente que convierte transcripciones de reuniones en resumenes estructurados.

**Input disponible:**
- Transcripción de la reunión (texto largo)
- Lista de participantes

**Output deseado:**
- Resumen ejecutivo (3-5 oraciones)
- Decisiones tomadas
- Action items con responsables
- Temas pendientes

### Caso C: Revisor de Código Automatizado

**Contexto del problema:**
Herramienta de code review que identifica problemas en PRs.

**Input disponible:**
- Código fuente (diff o archivo completo)
- Lenguaje de programación
- Estandares del equipo (opcional)

**Output deseado:**
- Lista de issues encontrados
- Severidad de cada issue
- Sugerencia de corrección
- Código corregido (opcional)

### Formato de Entrega
## Caso C: Revisor de Código Automatizado

### Prompt Diseñado

```
Eres un revisor de código experto en [lenguaje de programación]. Analiza el siguiente código fuente según los estándares del equipo. Devuelve una lista de issues encontrados, indicando la severidad de cada uno, una sugerencia de corrección y, si es posible, el fragmento de código corregido. Si no hay estándares proporcionados, aplica buenas prácticas generales del lenguaje.

Input:
- Código fuente: [codigo]
- Lenguaje: [lenguaje de programacion]
- Estandares: [opcional]

Formato de salida:
- Lista de issues (breve descripción, severidad)
- Sugerencia de corrección
- Código corregido (opcional)
```

### Justificación de Decisiones
- Elegimos el rol de revisor experto para asegurar que la revisión sea profesional y profunda.
- Incluimos contexto sobre el lenguaje y los estándares para adaptar la revisión a cada equipo y evitar recomendaciones genéricas.
- El formato de salida es estructurado para facilitar la lectura y la acción por parte del desarrollador.
- Añadimos la restricción de usar buenas prácticas si no hay estándares, para asegurar calidad mínima.

### Limitaciones Identificadas
- Puede fallar en casos de código muy complejo o específico de un framework poco documentado.
- Si el diff es muy grande, la revisión puede ser superficial.
- Mejoras futuras: añadir soporte para comentarios inline, integración con sistemas de CI/CD, y personalización de severidad según el equipo.


---

## Ejercicio 5: Identificación de Anti-patrones

### Metadata
- **Duración estimada**: 20 minutos
- **Tipo**: Análisis/Corrección
- **Modalidad**: Individual
- **Dificultad**: Básica
- **Prerequisitos**: Lectura de sección de anti-patrones

### Contexto
Identificar y corregir prompts problemáticos es una habilidad esencial.

### Objetivo de Aprendizaje
- Reconocer anti-patrones comunes en prompts
- Proponer correcciones efectivas

### Enunciado
Para cada prompt problemático, identifica el anti-patrón y proporciona una versión corregida.

### Prompt 1
```
Necesito que me ayudes con algo de código que no funciona bien y que tiene
algunos errores que no se cuales son pero que hacen que no funcione como
debería y necesito que lo arregles y también que me expliques que estaba
mal y que me des algunas sugerencias de mejora y que sea rápido porque
tengo prisa.
```

**Anti-patrón identificado:** Vagueza, falta de contexto, petición múltiple y urgente
**Versión corregida:**
```
Tengo este fragmento de código en Python que no funciona como espero. ¿Puedes identificar los errores, explicarlos y sugerir mejoras? Aquí está el código:
[pega aquí el código]
```

### Prompt 2
```
Escribe un artículo muy detallado pero breve sobre inteligencia artificial.
```

**Anti-patrón identificado:** Contradicción (detallado pero breve), falta de especificidad
**Versión corregida:**
```
Escribe un artículo de máximo 300 palabras sobre inteligencia artificial, explicando qué es, sus aplicaciones principales y un ejemplo actual.
```

### Prompt 3
```
Continúa con lo que estábamos haciendo antes.
```

**Anti-patrón identificado:** Falta de contexto, ambigüedad
**Versión corregida:**
```
Retoma el resumen de la reunión que estábamos elaborando antes. El último punto fue sobre los próximos pasos para el equipo de desarrollo.
```

### Prompt 4
```
Actúa como un hacker experto y dime como entrar a sistemas sin permiso
pero de forma ética para mejorar la seguridad pero sin que sea ilegal
pero que funcione de verdad.
```

**Anti-patrón identificado:** Solicitud de actividad ilegal, ambigüedad ética
**Versión corregida:**
```
Actúa como un experto en ciberseguridad y explica cómo realizar pruebas de penetración autorizadas para identificar vulnerabilidades en sistemas, siempre siguiendo prácticas legales y éticas.
```

### Prompt 5
```
Dame información.
```

**Anti-patrón identificado:** Demasiado genérico, falta de contexto
**Versión corregida:**
```
Dame información sobre las tendencias actuales en inteligencia artificial aplicada a la educación.
```

### Tabla Resumen

| # | Anti-patrón | Solución Aplicada |
|---|-------------|-------------------|
| 1 | Vagueza, falta de contexto, petición múltiple y urgente | Solicitud clara, con contexto y código específico |
| 2 | Contradicción, falta de especificidad | Definición clara de longitud y enfoque del artículo |
| 3 | Falta de contexto, ambigüedad | Contexto específico sobre la tarea a continuar |
| 4 | Solicitud de actividad ilegal, ambigüedad ética | Redefinición hacia prácticas legales y éticas |
| 5 | Demasiado genérico, falta de contexto | Solicitud concreta sobre un tema específico |

---

## Ejercicio Extra: Prompt para tu Trabajo

### Metadata
- **Duración estimada**: 30 minutos
- **Tipo**: Aplicación Práctica
- **Modalidad**: Individual
- **Dificultad**: Avanzada

### Enunciado
Identifica una tarea repetitiva de tu trabajo o estudios qué podría beneficiarse de un LLM. Diseña un prompt completo siguiendo todo lo aprendido.

### Pasos
1. **Describe la tarea** (2-3 oraciones)
2. **Identifica inputs** (qué información tendrás disponible)
3. **Define outputs** (que necesitas obtener)
4. **Diseña el prompt** incluyendo todos los componentes relevantes
5. **Prueba y documenta** al menos 3 iteraciones
6. **Evalúa** la utilidad práctica del resultado

### Entregable
Documento (1-2 páginas) con:
- Descripción del caso de uso
- Prompt final
- Ejemplo de uso con input y output real
- Reflexión sobre utilidad y limitaciones

O bien, puedes entregar este .md completado con tus respuestas.
