# Técnicas aprendidas de otros expertos (mi "formación" como herramienta)
Cada técnica lleva fuente y estado. Se adapta a MISTER ÉLITE; no se copia código ajeno.

## 1. Ganchos (hooks) — Jakeschincariol/instagram-agent-skill [confirmado]
- Probar 3 ganchos por Reel y puntuarlos en 5 ejes: **frontload** (lo fuerte en <3 s), **stakes** (qué se pierde), **specificity** (número/nombre concreto), **address** (habla al problema real del míster), **vocabulario fresco**.
- Descartes automáticos: abrir con saludo ("Hola chicos...") = no has ganado la atención.
- Límite honesto: un texto no predice cuál de dos ganchos buenos gana (decide cara, edición, audio). Solo sirve para eliminar los malos y exigir concreción (la especificidad fue lo único que separó buenos/malos). → **Conclusión: testear en real, no fiarse del "score".**
- Fórmulas útiles → versión fútbol:
  - *Nadie te cuenta*: "Nadie te cuenta por qué tu 4-3-3 se rompe por dentro."
  - *El robo*: "Roba este rondo de 4 minutos que usa [equipo]."
  - *Giro contrario*: "Dejar de hacer rondos de 4v2 mejoró mi presión."
  - *Estadística*: "El 70% de los goles de [sistema] salen de esta zona."
  - *Resultado ajeno*: "Cómo un equipo de [categoría] pasó de X a Y con 1 ajuste."
  - *Superlativo*: "El error nº1 del lateral en línea de 4."

## 2. Estructura de Reel — Jakeschincariol + brainbytes-dev [confirmado]
- Gancho 0-3 s → contexto 1-3 s → valor 3-15 s → remate/CTA hasta 30 s → **cierre que conecta con el inicio (loop)**.
- Ritmo ~165 palabras/min. Ningún plano estático >4 s. Subtítulos siempre (se ve sin sonido).
- Largo: 7-15 s para completar; 30-60 s para profundidad. Nunca >3 min.

## 3. Captions — sergebulaev/instagram-skills [confirmado]
- Lo que decide está en los **primeros 125 caracteres** (antes de "más"). Un solo CTA. Cifras en vez de adjetivos.
- Hashtags: 3-5 (Instagram redujo el máximo a 5 en dic-2025 según Jakeschincariol) → mezclar nicho/medio/amplio ajustados a tamaño de cuenta. [verificar límite vigente]
- Palabras clave de búsqueda en nombre de perfil, 1ª línea del caption y alt text (SEO de Instagram).
- Humanizador: quitar muletillas de IA ("desbloquea", "sumérgete", "eleva", "la clave es"), guiones largos en exceso, listas de emojis, tríadas; variar longitud de frases; meta humanness ≥75/100.

## 4. Carruseles — sergebulaev + brainbytes-dev [confirmado]
- Portada autónoma (titular grande, alto contraste) → 1 idea por diapositiva (30-50 palabras) → penúltima/última: cierre con CTA a GUARDAR/ENVIAR. Formato 4:5 (1080x1350), hasta 10 diapositivas.
- Para MISTER ÉLITE: 1 tarea de campo = 1 carrusel (pizarra → organización → variantes → errores).

## 5. Perfil — Jakeschincariol (/ig-profile 12 criterios) + sergebulaev [confirmado]
- Auditar: foto, **nombre buscable**, bio ≤150 car., enlace, categoría, destacados (nombres/portadas/orden), primeros 9 posts del grid y hasta 3 fijados.
- 5-7 destacados, revisar cada trimestre.

## 6. Interacción y embudo — Jakeschincariol (/ig-comment, /ig-reply, /ig-dm) [plausible, a probar]
- Embudo por **palabra clave por DM** ("comenta SISTEMA y te mando la guía") → primer mensaje → 2 seguimientos. Ideal para llevar a los cursos.
- Responder comentarios por tipo (keyword, lead, duda, apoyo, ruido).

## 7. Reciclaje de contenido (repurpose) [confirmado]
- 1 curso/tarea → N piezas nativas (Reel, carrusel, Stories, caption). Re-enganchar antes del pliegue; nunca copiar-pegar.

## 8. Medición — Jakeschincariol (/ig-audit, swipe) + brainbytes-dev [confirmado]
- Evaluar cada pieza por **múltiplo sobre tu mediana** de alcance (no por visualizaciones absolutas). Identificar "outliers" y reproducir su fórmula.
- Benchmarks de referencia (brainbytes-dev, orientativos): guardados 2-5 % del alcance, envíos 1-3 %, crecimiento mensual 2-5 %, Reels 2-10x seguidores en visualizaciones, Stories 60-80 % completadas.
- Tu cuenta: crecimiento mensual ≈4,3 % y visualizaciones ≈5,7x seguidores → dentro/arriba de benchmark.

## 9. Investigación viral sin trampas [confirmado]
- Capturar a mano 10-12 Reels de ~10 cuentas del nicho; ranking por múltiplo sobre su mediana; nombrar la fórmula de gancho de cada outlier. Sin scrapers con login (riesgo para tu cuenta).

## Ronda 4 (2026-10-02) — nuevas técnicas
Fuentes: github.com/social-media-skills/skills · zebracat/retensis/opus.pro (retención 2026) · manychat.com/blog (comment automation) · setsmart.io / learnybox.com (embudos de cursos) · inro.social / socialchamp.com (Trial Reels).

10. **Trial Reels** [confirmado, varias fuentes]: se muestran SOLO a no seguidores hasta 72 h; si superan el umbral, pasan a seguidores y al grid. Requiere cuenta profesional pública ≥1.000 seguidores (la tuya cumple). → **Sustituye al "score de ganchos": publicar 2-3 variantes del gancho como Trial y quedarse con la que gane.** (Activación manual en la app al publicar; no sé si la API de Make lo soporta.)
11. **Benchmarks de retención** [plausible, fuentes de herramientas]: abandono en los primeros 3 s <20 % sano, 20-30 % normal, >40 % el gancho falla; completado >50 % = sigue distribuyéndose; retención a 3 s >70 % activa más alcance. Subtítulos ≈ +38 % de retención; cara en los 3 primeros segundos ≈ +35 %. → Subtítulos quemados ya incluidos en `montar_reel.py`.
12. **Tipos de gancho con mejor conversión** [plausible, estudio de anuncios]: resultado concreto > POV realista > opinión impopular. Encaja con "X es una trampa" (opinión impopular) y "en 4 minutos mejoras Y" (resultado concreto).
13. **Límites reales de comentario→DM (API de Instagram)** [confirmado en varias guías; verificar en ManyChat]: máx. 200 DMs/hora; **1 DM automático por usuario cada 24 h** desde comentario/Story; 1 mensaje privado por comentario y dentro de 7 días; **el primer mensaje = un solo bloque, sin esperas ni pasos extra**. Recomendado: 3-5 variantes de DM y de respuesta pública, personalizar con el nombre. Conversión típica comentario→lead 15-25 % si el CTA es claro y específico.
14. **Embudo de cursos**: la mayoría de ventas se cierran en el DM: contenido que abre conversación → flujo que cualifica → derivación al curso adecuado. El pack social-media-skills lo estructura con: brand-profile, voice-builder, audience-research, goals-and-kpis (bases) + lead-magnets-and-funnels + link-in-bio.

## Ronda 5 (2026-10-02)
Fuentes: github.com/coreyhaines31/marketingskills · posteverywhere.ai / adpicto.com / carouselli.com (carruseles) · inro.social / later.com (SEO de Instagram) · metricool.com (estudio 2026) · creatorflow.so (métricas).

15. **Carruseles 2026** [plausible; datos de herramientas, ojo con contradicciones]: óptimo 7-10 diapositivas (el límite ya es 20); la portada decide ~80 % del resultado; guardados +35 % frente a imagen única. **Carrusel mixto (imágenes + vídeo) 2,33 % de engagement y solo el 7 % de las cuentas lo usa** → oportunidad directa: pizarras estáticas + 1 clip animado de la jugada como diapositiva.
16. **SEO de Instagram** [confirmado en varias guías]: desde julio-2025 los posts públicos de cuentas profesionales se indexan en Google por defecto; la búsqueda es semántica (entiende intención), pero prioriza palabras clave en nombre de usuario, **campo nombre**, bio, primera línea del caption y **alt text (hasta 100 car.)**. Poner alt text a cada Reel/imagen.
17. **5 métricas que importan** [plausible]: engagement por alcance, envíos/alcance, retención de Reels, velocidad de crecimiento de seguidores, finalización de Stories. (Ignorar likes sueltos y seguidores totales.)
18. **Diseño de experimentos** (skill `ab-testing` de marketingskills) [adoptado]: 1 variable por test, hipótesis escrita antes, no declarar ganador con diferencias pequeñas o muestra baja. → Aplicado a ganchos A/B (umbral de victoria).
19. **Skill base compartida** (`product-marketing` en marketingskills: todas las skills leen primero el contexto de marca) → ya equivale a `marca-y-voz.md`; las skills deben leerlo siempre primero.
20. **Investigación de competencia sin scrapers**: la API oficial de Instagram permite leer métricas públicas (likes, comentarios) de cuentas Business/Creator ajenas (en Make: "List public user posts / Get public user info"). Cuando esté autorizada la conexión de @misterelite, analizar cuentas de táctica sin tocar sus datos privados ni violar normas. [verificar alcance de campos]

### Contradicciones detectadas (no tomar nada como ley)
- **Duración óptima del Reel**: unas fuentes dicen 7-15 s (más completado), otras 30-60 s (más engagement/vistas medianas). → Probar duración como variable propia (un Reel corto y uno de 40-50 s del mismo tema) y decidir con tus datos.
- **Engagement de carruseles**: 0,55 % (ronda 1) frente a 1,92 % (ronda 5): muestras y definiciones distintas. Usar solo tu propia mediana.
- **Tendencia general**: el estudio de Metricool 2026 reporta caída de alcance de Reels (-35 %) y posts (-31 %) interanual: la saturación del vídeo corto es real → la diferenciación (series, marca, análisis propio) pesa más que el volumen. Otro dato (vendor): 4+ Reels/semana crecen 2,8x más rápido que 1-2.
- **Búsqueda de cuentas de táctica en español**: sin resultados útiles con buscadores; no inventar referentes. Alternativa: la API de competencia (técnica 20).

## Pendiente de estudiar (próximas rondas)
- github.com/social-media-skills/skills (106 skills: vídeo, diseño, analítica, publicación).
- github.com/coreyhaines31/marketingskills (copy, CRO, analítica).
- YouTube: canales de growth y análisis de Reels (buscar por título, ver transcripciones).
- Cuentas top de fútbol/entrenadores en ES (patrones de gancho/serie).
- Herramientas de publicación/programación vía Make (ya conectado) y Canva (ya conectado) para producir carruseles.
