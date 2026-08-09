# EcoTrack (GesConSof)

Un proyecto académico de desarrollo web enfocado en la contenerización y automatización de despliegues. Este repositorio demuestra la implementación práctica de infraestructura como código utilizando **Docker** y flujos de integración y despliegue continuo (CI/CD).

## Características Principales

*   **Contenerización (Docker):** La aplicación está completamente empaquetada con su propio `Dockerfile` y orquestada mediante `docker-compose.yml`, lo que garantiza un entorno de desarrollo y producción 100% consistente.
*   **CI/CD Automatizado:** Cuenta con flujos de trabajo en GitHub Actions (`.github/workflows`) para validar y asegurar el código antes de cada paso a producción.
*   **Infraestructura en la Nube:** Configuración nativa para despliegue automatizado en Render utilizando `render.yaml` y scripts de construcción personalizados (`build.sh`).

## Stack Tecnológico

*   **Backend & Framework:** Python / Django
*   **Infraestructura:** Docker, Docker Compose
*   **Automatización:** GitHub Actions
*   **Despliegue:** Render

## Levantar el proyecto en local

Gracias a Docker, no necesitas instalar dependencias de Python manualmente en tu equipo. Para ejecutar este proyecto, asegúrate de tener Docker y Docker Compose instalados, y ejecuta el siguiente comando en tu terminal:

```bash
docker-compose up --build
