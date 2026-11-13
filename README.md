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
assets/img/og-compartir.jpg  Imagen que aparece al compartir el enlace (WhatsApp, Facebook, LinkedIn); og-image.jpg es la misma
assets/img/hero/        Fotos de la portada
assets/img/galeria/     Fotos de «Así avanza Wawaín»
assets/img/aliados/     Logos de aliados (ver más abajo)
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

### Monto reunido y etapas

Las cifras se configuran en **un solo objeto, `CAMPANA`, al inicio del `<script>` de `index.html`**:

```js
var CAMPANA={
  totalFuente:'excel',        // el monto general se lee de la hoja de Google (no tocar)
  totalRespaldo:2075,         // lo que se muestra si la hoja no responde
  etapa1:{ meta:4600, estado:'cubierta' },   // etapa 1 cerrada: se muestra completa, no se borra
  etapa2:{ reunido:100, meta:2900 },         // tramo 4,600 → 7,500
  sumarEtapa2AlTotal:true,    // true mientras la hoja NO incluya la etapa 2; ponerlo en false cuando ya la incluya
  metaGeneral:15770,
  escalones:[4600,7500,10000],
  siguiente:{ nombre:'San Rafael', monto:15000 }
};
```

- **Total reunido** = monto de la hoja + etapa 2 (si `sumarEtapa2AlTotal` es `true`). Nada se resta. Hoy: 2,075 + 100 = **S/ 2,175**.
- La portada y la barra de abajo muestran la **etapa 2** (S/ 100 de S/ 2,900); la portada y «Qué significa esta meta» muestran además el total.
- Cuando las donaciones nuevas ya estén en la hoja, pon `sumarEtapa2AlTotal:false` para no contarlas dos veces.
- Todos los textos con cifras (porcentajes, barras, etiquetas de accesibilidad) salen de este objeto: no hay montos escritos a mano.

El monto general se lee **de la celda A1 de la hoja de Google «Monto website campaña» (pestaña «Monto website»)**. Para actualizarlo, cambia ese número en la hoja (sin símbolos) y recarga la web: se ve en uno o dos minutos, sin tocar GitHub.

- La hoja debe estar compartida como **«Cualquier persona con el enlace: Lector»** y solo quien administra la campaña debe poder editarla. Si estuviera como Editor, cualquiera con el enlace podría cambiar el monto que ve el público.
- Esa pestaña debe ser la **primera** de la hoja y no debe llevar datos de personas.
- Si la hoja no responde, la web usa `CAMPANA.totalRespaldo`. Conviene ponerlo al día de vez en cuando.

### Idioma (ES | EN)

El botón **ES | EN** de la cabecera (y de la pantalla de bienvenida) cambia todo el texto. El español es la base del HTML; el inglés vive en el diccionario `I18N`, dentro de `index.html` (bloque entre `I18N:inicio` y `I18N:fin`), con las mismas claves y el mismo orden por sección para revisarlos lado a lado. Cada elemento traducible lleva `data-i18n="clave"` (`data-i18n-alt`, `data-i18n-aria` para imágenes y accesibilidad; `data-wa` para los mensajes precargados de WhatsApp). La elección se recuerda en el navegador (`localStorage`).

- Para corregir una frase en inglés: buscar su clave en `en:{ … }` y editar el texto.
- Para agregar un texto nuevo: ponerle `data-i18n="seccion.nnn"` y agregar la clave en **ambos** idiomas.
- No se traducen los nombres propios, el formulario, los datos bancarios ni los montos. El brochure solo existe en español: en inglés los enlaces muestran la marca «ES».

### Fotos

- **Portada** (5 fotos que rotan cada 5 s): `assets/img/hero/hero-N-…-800.webp` (móvil, recorte vertical 4:5) y `…-1600.webp` (escritorio).
- **Así avanza Wawaín** (galería y visor): `assets/img/galeria/g-NN-640.webp` (miniatura) y `g-NN-1600.webp` (visor). El orden de las miniaturas en `index.html` (`#galeria`) es el orden del visor. Para agregar el hito «Techado», añadir sus `<button class="miniatura" data-hito="techado" data-mes="2027-01" …>` al final de `#galeria` y las claves de texto en `I18N`.
- Los originales de alta resolución no se publican: si se guardan en el repositorio, van en `fotos-origen/` (está en `.gitignore`).

### Logos de aliados

Ponerlos en `assets/img/aliados/` (SVG o PNG con fondo transparente, todos a la misma altura). Mientras no estén, el panel de transparencia muestra el nombre en texto. Para usar el logo, reemplazar el texto del `<span class="marca-apoyo">` por `<img src="assets/img/aliados/archivo.svg" alt="Nombre">`; se muestra en gris automáticamente.

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
