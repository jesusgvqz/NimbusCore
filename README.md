# NimbusCore
App web para registrar servidores Linux y gestionar los servicios instalados en ellos, levantarlos, administrarlos (reiniciar/dar de baja) y monitorizarlos en tiempo real.

## Estructura
---
Frontend: Aplicación Flutter (Web y Móvil)

Backend: API Flask con PostgreSQL, JWT y Swagger

# Instalación

## 🔄 1. Clonar el repositorio
```bash
git clone https://github.com/jesusgvqz/NimbusCore.git
cd NimbusCore
```

---

## 🐍 2. Configurar el backend (Flask)

### A. Ir a la carpeta del backend
```bash
cd backend
```

### B. Crear entorno virtual de Python
```bash
python3 -m venv venv
source venv/bin/activate     # En Windows: venv\Scripts\activate
```

### C. Instalar dependencias
```bash
pip install -r requirements.txt
```

### D. Ejecutar el servidor Flask
Con python:
```bash
python run.py
```
Mediante .flaskenv:
```bash
flask run
```

La API estará disponible en:
```
http://localhost:5000
http://localhost:5000/apidocs (Swagger UI)
```

---

## 🎯 3. Configurar el frontend (Flutter)

### A. Ir a la carpeta del frontend
```bash
cd ../frontend
```

### B. Instalar Flutter SDK (si no lo tienes)
- Ir a: https://docs.flutter.dev/get-started/install
- Descargar el SDK según el sistema operativo.
Flutter recomienda crear el directorio `development`:
```bash
mkdir ~/development
cd ~/development
```
```bash
tar -xf ~/Downloads/flutter_linux_3.29.3-stable.tar.xz -C ~/development/
```

- Agregar Flutter al PATH:
```bash
# En Linux/macOS (~/.bashrc o ~/.zshrc)
echo 'export PATH="$HOME/development/flutter/bin:$PATH"' >> ~/.bash_profile

# En Windows: agregar ruta a flutter\bin en variables de entorno
```

### C. Verificar instalación
```bash
flutter doctor
```

### D. Instalar extensiones en VS Code:
- **Flutter** (by Dart Code)
- **Dart** (by Dart Code)
- Opcional: Flutter Stylizer, Pubspec Assist, Flutter Snippets

### E. Ejecutar la app Flutter
```bash
flutter run -d chrome    # Para compilar en web
flutter run              # Detecta dispositivos móviles/emuladores
```

---
