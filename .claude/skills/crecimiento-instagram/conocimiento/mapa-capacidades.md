# Mapa de capacidades (conectores, plugins, skills) — revisar cada ronda
Última revisión: 2026-10-02

## Ya instalado en la cuenta de Moisés
| Herramienta | Estado | Para qué sirve en Instagram |
|---|---|---|
| **META** | instalado, **necesita reconectar** y activar en el chat | Probable acceso directo a Instagram/Meta (por verificar sus herramientas al reconectar) |
| **Windsor.ai** | instalado, conexión **incompleta** | Alcance, guardados y crecimiento de seguidores de Instagram; además YouTube, GA4, Stripe… |
| **Stripe** | instalado, necesita reconectar | Ver ventas reales de cursos → medir qué contenido vende (no solo seguidores) |
| Make | conectado (Instagram Business de otra cuenta; falta autorizar @misterelite) | Publicar Reels y leer insights |
| Canva | conectado | Portadas y carruseles |
| HeyGen / Higgsfield / HyperFrames | conectados | Vídeo, avatar, voz alternativa, motion graphics |
| Google Drive / Calendar / Notion | conectados | Guardar planes, calendario editorial |
| Gmail | necesita reconectar | Avisos / informes por correo |
| ElevenLabs | solo en el PC de Moisés | Voz de marca (vía Claude del PC) |

## Disponible en directorio (no instalado) — candidatos
- **Plugin "instagram"** (Graph API oficial): leer y responder comentarios y DMs, con "comment-to-DM" integrado → resuelve el embudo "comenta CLAVE y te mando la guía". Prioridad ALTA (comentarios = mayor hueco medido).
- **Metricool**: programar posts, métricas y mejor hora para publicar por red.
- **Supermetrics**: Instagram + YouTube + 200 fuentes de analítica.
- **Ayrshare**: publicar/analizar en 13+ redes con validación de reglas de cada plataforma.
- **Posty**: programador con calendario y subida de vídeo en calidad completa.
- **Marketing (Anthropic)**: brand-review, campaign-plan, performance-report.
- **Motion Creative Analytics**: analiza creatividades propias y de la competencia (orientado a anuncios Meta).
- Skills de terceros en GitHub (ver tecnicas-aprendidas.md): social-media-skills (106), marketingskills.

## Orden recomendado de activación (menos esfuerzo → más valor)
1. Reconectar **META** (ya instalado) → verificar si lee insights de @misterelite.
2. Completar **Windsor.ai** (ya instalado) como alternativa de métricas.
3. Reconectar **Stripe** → atribuir ventas a piezas de contenido.
4. Plugin **instagram** → comentarios + DM automáticos.
5. Autorizar Instagram en **Make** → publicación programada.

## Regla de la ronda semanal
Cada ronda: (a) volver a buscar en el registro de conectores/plugins con palabras nuevas (reels, analytics, comment automation, YouTube analytics, TikTok/Shorts cross-posting), (b) comprobar si algo de la lista cambió de estado, (c) proponer como máximo 1 mejora de integración, con su esfuerzo para Moisés (clics necesarios).

## Automatización de publicación (idea clave, 2026-10-02)
Moisés YA tiene en Make un escenario de publicación por cola (data store, 11:00 y 19:00, módulos CreateAReelPost/CreatePostPhoto) para otra cuenta (herencias-canarias). Reutilizar el patrón para @misterelite: Reels listos → cola → publicación a las 15:30/17:30 WEST. Falta autorizar Instagram de @misterelite en Make y decidir dónde viven los vídeos (URL accesible: Drive u otro).
ManyChat: palabras clave FIJAS aplicadas a "cualquier publicación" → cero activaciones por Reel.

## Competencia sin scrapers (2026-10-02)
Con la conexión de Instagram de @misterelite autorizada en Make, los módulos "List public user posts" y "Get public user info" leen métricas públicas de otras cuentas Business/Creator (API oficial). Usarlos cada ronda sobre 5-10 cuentas de táctica (a elegir; pedir a Moisés SOLO los @ que quiera vigilar, una vez) y calcular múltiplos sobre su mediana. Verificar qué campos devuelve.

# DECISIÓN DE AUTONOMÍA (ronda 6, 2026-10-03)
Objetivo: que Claude lea métricas, publique, gestione comentarios y investigue competencia con el mínimo de intervención de Moisés.
Criterios: autonomía ganada · clics/tiempo para Moisés · riesgo para la cuenta (tokens de marca) · coste · madurez.

## Hechos técnicos verificados (API oficial de Instagram)
- Publicar vía API: Reels 9:16, 5-90 s, H.264/HEVC, cuenta profesional; **el vídeo debe estar en una URL pública HTTPS** (Instagram lo descarga; no hay subida local). Límite 100 publicaciones/24 h. Flujo: crear contenedor → esperar FINISHED → publicar.
- **Trial Reels por API: no confirmado** → asumir activación manual en la app.
- **DMs por API: requieren permiso `instagram_manage_messages` y revisión de Meta (semanas)** → ManyChat sigue siendo la vía de DMs. Comentarios, insights y publicación NO requieren esa revisión.
- Hosting del vídeo: Moisés ya tiene WordPress (misterelite.es): su biblioteca de medios da URL pública HTTPS (la sube su Claude del chat con el MCP de WordPress). Alternativas: S3/Cloudflare R2.

## Opciones comparadas
| Opción | Qué da | Esfuerzo Moisés | Riesgo / madurez | Veredicto |
|---|---|---|---|---|
| **Make** (ya suyo): módulos Get user insights, Get post insights, List posts, Create reel/carousel/photo, comentarios, datos públicos de otras cuentas | Leer métricas, publicar desde cola, responder comentarios, vigilar competencia | **1 clic** (autorizar @misterelite) | Bajo: plataforma establecida, ya la usa | **1ª opción** |
| **META** (conector instalado, sin herramientas visibles) | Por descubrir | Reconectar (pocos clics) | Desconocido | Reconectar y mirar qué ofrece |
| **Windsor.ai** (instalado, conexión a medias; partner verificado) | Alcance, guardados, crecimiento (solo lectura) + YouTube/GA4/Stripe | Terminar conexión | Bajo-medio | **2ª**: métricas redundantes y multi-fuente |
| **MCP local de código abierto** (IvanBBaev/instagram-mcp: 28 herramientas, MIT, escribe solo con confirmación; Burak-cell-max/instagram-mcp-panel: 29 herramientas + panel local) | Todo lo anterior directamente desde Claude Code en el PC, incluida competencia por hashtags/perfiles públicos | Alto: crear app de Meta, token, Node ≥22 (~1 h con ayuda) | **Medio-alto**: v0.7, 2 estrellas, "ninguna herramienta probada contra una cuenta real en CI"; guarda token en archivo local | Solo si Make falla; modo vista previa (`apply:false`), sin `IG_WRITE_MODE=apply` |
| **SaaS con MCP** (Metricool, Ayrshare, Posty, SocialRobot, Maeve…) | Programar, métricas, mejor hora | Login en navegador + plan de pago | Medio: terceros guardan los tokens de la marca; la mayoría "community" | Reserva si Make no sirve; preferir Metricool/Ayrshare por madurez |
| **vidIQ** (MCP: outliers, tendencias, palabras clave YouTube/IG/TikTok) | Investigación de contenido que funciona (mejora el bucle de investigación) | Conectar cuenta (coste por comprobar) | Bajo (solo lectura) | Probar plan gratuito en una ronda |
| **Socialinsider** (partner) | Auditoría y benchmark de competidores | Cuenta de pago | Bajo | Solo si se quiere benchmark serio |
| **ManyChat** (ya suyo) | Comentario→DM con palabras clave fijas | Configuración única | Bajo | **Mantener** |

## Ruta recomendada (menor esfuerzo → mayor autonomía)
1. Moisés: autorizar Instagram de @misterelite en Make (1 clic) y reconectar META (ver herramientas).
2. Claude: escenario Make semanal → leer insights por pieza y por versión de gancho (A/B/C) y guardarlos como JSON en el repo (necesita conexión de GitHub en Make) → la rutina de la nube los lee sola.
3. Claude: escenario de cola de publicación (patrón de herencias-canarias) con vídeos alojados en WordPress.
4. Claude: escenario de competencia (datos públicos de 5-10 cuentas de táctica).
5. Más adelante: vidIQ (investigación) y, si hace falta, MCP local o Metricool.

## Reglas de seguridad para cualquier integración
- Nada con permiso de escritura sin visto bueno de Moisés (publicar, borrar, responder en público).
- No pegar tokens en el repo ni en el chat; usar el sistema de conexiones de Make/claude.ai o secretos del entorno.
- Preferir API oficial; descartar herramientas que pidan usuario y contraseña de Instagram o hagan scraping (riesgo de bloqueo de la cuenta).
- Revisar qué publicador y qué permisos pide cada plugin antes de recomendarlo.
