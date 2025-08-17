

# 📌 Comandos principales en tmux
---

| Acción                                  | Comando (después de `Ctrl+b`) |
| --------------------------------------- | ----------------------------- |
| Dividir pantalla **vertical** (derecha) | `%`                           |
| Dividir pantalla **horizontal** (abajo) | `"`                           |
| Ir al panel de la **izquierda**         | `←` (flecha izquierda)        |
| Ir al panel de la **derecha**           | `→` (flecha derecha)          |
| Ir al panel de **arriba**               | `↑` (flecha arriba)           |
| Ir al panel de **abajo**                | `↓` (flecha abajo)            |
| Cerrar panel actual                     | `x`                           |
| Cambiar paneles (rotar disposición)     | `Ctrl+o`                      |
| Cambiar al siguiente panel              | `o`                           |
| Maximizar/Restaurar panel actual        | `z`                           |
| Salir de tmux (cerrar sesión)           | `:kill-session`               |
| Redimensionar panel hacia la izquierda  | `Ctrl+b` luego `Alt + ←`  |
| Redimensionar panel hacia la derecha   | `Ctrl+b` luego `Alt + →`  |
| Redimensionar panel hacia arriba       | `Ctrl+b` luego `Alt + ↑`  |
| Redimensionar panel hacia abajo        | `Ctrl+b` luego `Alt + ↓`  |



# 📌 Gestión de sesiones en tmux
---

| Acción                                 | Comando                              | Notas                                               |
| -------------------------------------- | ------------------------------------ | --------------------------------------------------- |
| Crear una nueva sesión                 | `tmux new -s nombre_sesion`          | Ej: `tmux new -s proyecto`                          |
| Salir de tmux (sin cerrar sesión)      | `Ctrl+b` luego `d`                   | "Detach": deja la sesión corriendo en segundo plano |
| Listar todas las sesiones activas      | `tmux ls`                            | Muestra todas las sesiones abiertas                 |
| Volver a una sesión existente          | `tmux attach -t nombre_sesion`       | Ej: `tmux attach -t proyecto`                       |
| Cambiar de sesión dentro de tmux       | `Ctrl+b` luego `s`                   | Abre menú para elegir sesión                        |
| Renombrar sesión                       | `Ctrl+b` luego `$`                   | Muy útil para organizar                             |
| Cerrar sesión actual (desde dentro)    | `exit` o `Ctrl+d`                    | Mata solo esa sesión                                |
| Cerrar sesión específica (desde fuera) | `tmux kill-session -t nombre_sesion` | Ej: `tmux kill-session -t proyecto`                 |
| Cerrar todas las sesiones              | `tmux kill-server`                   | Mata todo el servidor tmux                          |

# 🧮 Important
---
-  