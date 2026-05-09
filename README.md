
# Sistema de Gestión de Clientes, Servicios y Reservas - Software FJ

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema integral para **Software FJ**, una empresa que ofrece servicios de **reservas de salas**, **alquiler de equipos** y **asesorías especializadas**. El sistema está diseñado utilizando **Programación Orientada a Objetos (OOP)** y proporciona una gestión robusta de **clientes**, **servicios** y **reservas**.

El sistema utiliza **excepciones personalizadas** y maneja **errores** de forma eficiente, asegurando que el software sea estable incluso cuando se presentan entradas inválidas o errores durante la ejecución.

### **Características Principales**

- **Gestión de Clientes**: Registro y validación de los datos del cliente.
- **Gestión de Servicios**: Incluye diferentes tipos de servicios como reservas de salas, alquiler de equipos y asesorías.
- **Reservas**: Gestión de reservas, incluyendo confirmación, cancelación y procesamiento, con validación de datos.
- **Manejo de Excepciones**: Uso avanzado de excepciones personalizadas y bloques `try/except` para garantizar la estabilidad del sistema.
- **Automatización de Pruebas**: Integración con **GitHub Actions** para la ejecución automática de pruebas y validación continua del código.

---

## Estructura del Código

El sistema está dividido en las siguientes clases principales:

### **1. Clases Abstractas**

- **Entidad**: Clase base para todas las entidades del sistema (cliente, servicio, etc.).
- **Servicio**: Clase abstracta que es heredada por los servicios específicos como `ReservaSala`, `AlquilerEquipo`, y `AsesoriaEspecializada`.

### **2. Clases Concretas**

- **Cliente**: Representa los datos del cliente y proporciona validaciones de entrada.
- **ReservaSala**: Representa el servicio de reserva de salas, con la capacidad de calcular costos basados en la duración.
- **AlquilerEquipo**: Representa el servicio de alquiler de equipos con cálculo de costos similar al de las salas.
- **AsesoriaEspecializada**: Representa el servicio de asesoría especializada y calcula costos según la duración de la consulta.

### **3. Clase Reserva**

La clase `Reserva` integra a los clientes y servicios, permitiendo gestionar la creación, confirmación y cancelación de reservas.

---

## Uso

### **Requisitos**

- Python 3.x
- Dependencias (si las necesitas):
    - `pip install -r requirements.txt`

### **Ejecutando el Sistema**

1. **Crear un Cliente**:
   ```python
   cliente1 = Cliente("Carlos", "carlos@correo.com", "987654321")
   cliente1.registrar()
   ```

2. **Crear un Servicio**:
   ```python
   servicio1 = ReservaSala("Sala A", "Sala de reuniones con proyector")
   ```

3. **Crear una Reserva**:
   ```python
   reserva1 = Reserva(cliente1, servicio1, 2)  # 2 horas
   reserva1.confirmar_reserva()
   reserva1.procesar_reserva()
   ```

### **Ejemplo de Manejo de Excepciones**

El sistema maneja excepciones de manera robusta, asegurando que los errores no interrumpan el flujo del programa:

```python
try:
    cliente_invalido = Cliente("Juan", "juancorreo.com", "987654322")
except ValueError as e:
    print(f"Error al registrar cliente: {e}")
