#!/bin/bash
# ┌──────────────────────────────────────────────────────────────┐
# │ 🔧 VSCode Snippet Generator v7                               │
# │ Crea snippets en formato JSON desde código pegado            │
# │ Pregunta descripción justo después del prefix                │
# │ Finaliza al pulsar dos ENTER seguidos (líneas vacías)        │
# │ Copia automáticamente al portapapeles (macOS)                │
# └──────────────────────────────────────────────────────────────┘

# 📛 Nombre del snippet
echo "📛 Introduce el nombre del snippet:"
read name

# 🔤 Prefijo de activación
echo "🔤 Introduce el prefix del snippet:"
read prefix

# 🗒️ Descripción del snippet
echo "🗒️ Escribe una descripción para el snippet:"
read desc

# 📝 Captura del código
echo "📝 Pega el código. Pulsa ENTER dos veces seguidas para terminar:"

lines=()
empty_line_counter=0

while true; do
  IFS= read -r line
  if [[ -z "$line" ]]; then
    ((empty_line_counter++))
    if [[ $empty_line_counter -ge 2 ]]; then
      break
    fi
  else
    empty_line_counter=0
    # Escapar comillas dobles
    lines+=("\"${line//\"/\\\"}\",")
  fi
done

# 🧩 Construcción del cuerpo
body=$(printf "%s\n" "${lines[@]}")

# 🧱 Construcción final del snippet en JSON
snippet="\"$name\": {
  \"prefix\": \"$prefix\",
  \"body\": [
$body
  ],
  \"description\": \"$desc\"
}"

# 📋 Copiar al portapapeles (solo macOS)
echo "$snippet" | pbcopy

# ✅ Confirmación
echo -e "\n✅ Snippet generado y copiado al portapapeles. ¡Pégalo en tu archivo .code-snippets de VSCode!"