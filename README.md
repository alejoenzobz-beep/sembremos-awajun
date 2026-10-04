# Sembremos espacios de Aprendizaje Awajún

Sitio de la campaña de construcción comunitaria de **Paisajes Educativos + Manifiesto Lab** para las comunidades awajún de Wawaín y San Rafael (Imaza, Bagua, Amazonas).

Sitio estático: no necesita instalación, compilación ni dependencias.

---

## Contenido del repositorio

```
index.html              Página principal (imágenes y logos van incrustados)
404.html                Página para enlaces rotos
netlify.toml            Configuración de Netlify: cabeceras de seguridad y caché
favicon.svg             Ícono del navegador
favicon-32.png          Ícono para navegadores antiguos
apple-touch-icon.png    Ícono al guardar en la pantalla de un iPhone
icon-192.png            Íconos del manifiesto
icon-512.png
site.webmanifest        Nombre, colores e íconos del sitio
assets/img/og-compartir.jpg  Imagen que aparece al compartir el enlace (WhatsApp, Facebook, LinkedIn)
sumate/index.html       Página de enlace para compartir: lleva la vista previa y manda a la web
robots.txt              Indicaciones para buscadores
sitemap.xml             Mapa del sitio para buscadores
assets/marca/           Logos vectorizados y QR en SVG (para uso del equipo)
```

### Cómo compartir el enlace por WhatsApp

WhatsApp guarda la vista previa de cada dirección que ya vio y no la actualiza aunque cambie la imagen. Por eso se comparte una dirección nueva, `https://sembremos-awajun.netlify.app/sumate/`, que lleva la imagen y el texto de la vista previa y manda a la persona directo a la web.

Cuando cambie la imagen de compartir: guardar la nueva con **otro nombre** en `assets/img/`, cambiar su ruta en `sumate/index.html` y en `index.html` (etiquetas `og:image`), y compartir una dirección que no se haya enviado antes (por ejemplo `/sumate/?v=2`). Para ver qué lee un rastreador: https://developers.facebook.com/tools/debug/

---

## Publicar por primera vez

### 1. Subir a GitHub

1. Crea un repositorio nuevo en GitHub (por ejemplo `sembremos-awajun`). Puede ser privado.
2. Sube **todo el contenido de esta carpeta** a la raíz del repositorio, incluido el archivo oculto `.gitignore`. Desde la web: *Add file → Upload files* y arrastra todos los archivos y la carpeta `assets`.
3. Confirma con *Commit changes*.

### 2. Conectar con Netlify

1. En Netlify: *Add new site → Import an existing project → GitHub*, y elige el repositorio.
2. En la configuración de compilación deja **todo vacío**: Netlify lee `netlify.toml`, que ya indica que no hay compilación y que se publica la raíz.
3. *Deploy*.

### 3. Nombre del sitio — importante

El sitio está preparado para la dirección **`https://sembremos-awajun.netlify.app`**.

En Netlify ve a *Site configuration → Change site name* y escribe `sembremos-awajun`.

Si ese nombre está ocupado o usan un dominio propio, reemplaza `https://sembremos-awajun.netlify.app` por la dirección real en estos tres archivos (buscar y reemplazar):

- `index.html` — aparece 3 veces en la cabecera (`canonical`, `og:url`, `og:image`)
- `robots.txt`
- `sitemap.xml`

Sin este cambio, la vista previa al compartir el enlace por WhatsApp no mostrará la imagen.

---

## Actualizaciones frecuentes

Todos los cambios se hacen editando el archivo en GitHub (ícono del lápiz) y guardando con *Commit changes*. Netlify publica solo en uno o dos minutos.

### Monto reunido

El monto se lee **de la celda A1 de la hoja de Google «Monto website campaña» (pestaña «Monto website»)**. Para actualizarlo, cambia ese número en la hoja (sin símbolos) y recarga la web: se ve en uno o dos minutos, sin tocar GitHub.

- Las tres partes donde aparece el monto (portada, la meta y la barra de abajo), las barras y los porcentajes se recalculan solos, y el número cuenta de 0 al monto al aparecer.
- La hoja debe estar compartida como **«Cualquier persona con el enlace: Lector»** y solo quien administra la campaña debe poder editarla. Si estuviera como Editor, cualquiera con el enlace podría cambiar el monto que ve el público.
- Esa pestaña debe ser la **primera** de la hoja y no debe llevar datos de personas.
- Si la hoja no responde, la web muestra el número de respaldo que está en `index.html`, en la línea `datos-campana` (`"reunido"`). Conviene ponerlo al día de vez en cuando.

### Datos bancarios

Busca `por confirmar` en `index.html`. Reemplaza cada aparición por el dato real y borra `class="vacio"` de esa etiqueta para que el texto deje de verse en cursiva.

### Número de WhatsApp

Todos los botones usan `51991312955`. Si cambia el número, busca y reemplaza ese valor en `index.html` (y el `+51 991 312 955` visible del pie).

### Enlace del brochure

Busca `docs.google.com/presentation` en `index.html` y reemplaza el enlace completo. Aparece en varios botones.

El archivo en Google Drive debe estar compartido como **«Cualquier persona con el enlace — Lector»**; si no, los visitantes verán una pantalla de solicitud de acceso.

---

## Después de publicar

- **Vista previa al compartir.** WhatsApp y Facebook guardan en caché la primera versión que ven. Antes de difundir, pega el enlace en el [Depurador de Facebook](https://developers.facebook.com/tools/debug/) y pulsa *Volver a extraer*. Eso refresca también la vista en WhatsApp.
- **Revisión en celular.** La mayoría de visitas llegará por WhatsApp desde el teléfono. Conviene revisar las cinco pestañas en un celular real antes del lanzamiento.
- **Enlaces directos a secciones.** Se puede compartir una pestaña concreta añadiendo al final `#fases`, `#participar`, `#meta` o `#confianza`. Por ejemplo, para empresas: `https://sembremos-awajun.netlify.app/#meta`.

---

## Notas técnicas

- La única dependencia externa son las tipografías de Google Fonts (Outfit y Work Sans). Si no cargan, la página usa la tipografía del sistema sin romperse.
- `netlify.toml` aplica una política de seguridad de contenido (CSP). Si en el futuro se agrega un recurso de otro dominio —un video de YouTube, un formulario externo, analítica— hay que añadir ese dominio a la línea `Content-Security-Policy`, o el navegador lo bloqueará.
- La página cumple criterios de accesibilidad WCAG 2.1 AA: contraste de texto, botones de al menos 44 px, navegación por teclado entre pestañas (flechas, Inicio, Fin), enlace «Saltar al contenido» y textos alternativos en las imágenes.
