# 📚 Comandos más utilizados en Git/GitHub

---

## 🟢 1. Configuración inicial
| Nombre                | Definición                                      | Código                                           |
|------------------------|------------------------------------------------|-------------------------------------------------|
| Configurar usuario     | Define tu nombre para commits                   | `git config --global user.name "Tu Nombre"`     |
| Configurar email       | Define tu email para commits                    | `git config --global user.email "tu@email.com"` |
| Ver configuración      | Muestra la configuración actual                 | `git config --list`                             |

---

## 📂 2. Iniciar y clonar proyectos
| Nombre                | Definición                                      | Código                     |
|------------------------|------------------------------------------------|-----------------------------|
| Iniciar repo           | Crea un repositorio en carpeta actual           | `git init`                  |
| Clonar repo            | Copia un repo remoto a tu máquina               | `git clone URL`             |

---

## 📦 3. Manejo de cambios
| Nombre                | Definición                                      | Código                       |
|------------------------|------------------------------------------------|-------------------------------|
| Ver estado             | Muestra archivos modificados/no rastreados      | `git status`                  |
| Añadir archivo         | Añade un archivo específico al área de staging  | `git add archivo.txt`         |
| Añadir todos           | Añade todos los cambios al staging              | `git add .`                   |
| Hacer commit           | Guarda cambios en el historial                  | `git commit -m "mensaje"`     |
| Cambiar último commit  | Edita el último mensaje (sin modificar cambios) | `git commit --amend -m "msg"` |

---

## 🔄 4. Sincronización con remoto
| Nombre                | Definición                                      | Código                       |
|------------------------|------------------------------------------------|-------------------------------|
| Conectar remoto        | Vincula repo local con GitHub                   | `git remote add origin URL`   |
| Ver remotos            | Lista repositorios remotos vinculados           | `git remote -v`               |
| Subir cambios          | Empuja commits al remoto                        | `git push origin main`        |
| Bajar cambios          | Descarga cambios del remoto                     | `git pull origin main`        |
| Traer cambios (sin merge)| Descarga cambios sin fusionar                 | `git fetch`                   |

---

## 🌿 5. Ramas
| Nombre                | Definición                                      | Código                       |
|------------------------|------------------------------------------------|-------------------------------|
| Crear rama             | Crea nueva rama                                | `git branch nombre_rama`      |
| Cambiar rama           | Cambia a otra rama                             | `git checkout nombre_rama`    |
| Crear y cambiar rama   | Crea y cambia a nueva rama                     | `git checkout -b nueva_rama`  |
| Listar ramas           | Muestra todas las ramas                        | `git branch`                  |
| Borrar rama            | Elimina una rama                               | `git branch -d nombre_rama`   |
| Fusionar rama          | Fusiona rama en la actual                      | `git merge nombre_rama`       |

---

## 🧹 6. Otros útiles
| Nombre                | Definición                                      | Código                       |
|------------------------|------------------------------------------------|-------------------------------|
| Ver historial          | Muestra historial de commits                   | `git log --oneline --graph`   |
| Revertir archivo       | Revierte cambios no confirmados                | `git checkout -- archivo.txt` |
| Reset cambios (duro)   | Revierte commits y staging                     | `git reset --hard HEAD~1`     |
| Stash cambios          | Guarda temporalmente cambios sin commitear     | `git stash`                   |
| Aplicar stash          | Restaura los cambios guardados en stash        | `git stash pop`               |