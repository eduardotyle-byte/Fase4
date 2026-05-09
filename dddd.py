from abc import ABC, abstractmethod

# -----------------------------------------
# 1. Clase abstracta 'Entidad' (base para otras clases)
# -----------------------------------------
class Entidad(ABC):
    @abstractmethod
    def registrar(self):
        """Método abstracto para registrar la entidad."""
        pass
    
    @abstractmethod
    def mostrar_info(self):
        """Método abstracto para mostrar información de la entidad."""
        pass


# -----------------------------------------
# 2. Clase 'Cliente' con validaciones y manejo de excepciones
# -----------------------------------------
class Cliente(Entidad):
    def __init__(self, nombre, correo, telefono):
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono
        self.validar_datos()

    def validar_datos(self):
        """Valida que los datos del cliente sean correctos."""
        if not self._nombre or not self._correo or not self._telefono:
            raise ValueError("Datos del cliente incompletos.")
        if "@" not in self._correo:
            raise ValueError("Correo inválido.")
    
    def registrar(self):
        """Registra al cliente (imprime la información en consola)."""
        print(f"Cliente registrado: {self._nombre}, {self._correo}, {self._telefono}")

    def mostrar_info(self):
        """Muestra la información del cliente."""
        return f"Cliente: {self._nombre}, Correo: {self._correo}, Teléfono: {self._telefono}"


# -----------------------------------------
# 3. Clase abstracta 'Servicio' y subclases especializadas
# -----------------------------------------
class Servicio(ABC):
    def __init__(self, nombre, descripcion):
        self._nombre = nombre
        self._descripcion = descripcion

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        """Método abstracto para calcular el costo del servicio."""
        pass

    def mostrar_info(self):
        """Devuelve una cadena con la información del servicio."""
        return f"Servicio: {self._nombre}, Descripción: {self._descripcion}"


# Servicios específicos
class ReservaSala(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        costo_base = 100  # Costo por hora de la sala
        return costo_base * duracion * (1 - descuento)


class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        costo_base = 50  # Costo por hora de alquiler de equipo
        return costo_base * duracion * (1 - descuento)


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        costo_base = 200  # Costo por hora de asesoría
        return costo_base * duracion * (1 - descuento)


# -----------------------------------------
# 4. Clase 'Reserva' que integra Cliente y Servicio
# -----------------------------------------
class Reserva:
    def __init__(self, cliente, servicio, duracion, estado='pendiente'):
        if servicio is None:
            raise ValueError("El servicio no puede ser creado.")
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = estado

    def confirmar_reserva(self):
        """Confirma la reserva."""
        if self._estado != 'pendiente':
            raise ValueError("La reserva ya ha sido procesada.")
        self._estado = 'confirmada'
        print(f"Reserva confirmada: {self._cliente.mostrar_info()} para {self._servicio.mostrar_info()}")

    def cancelar_reserva(self):
        """Cancela la reserva."""
        if self._estado != 'pendiente':
            raise ValueError("No se puede cancelar una reserva que ya ha sido procesada.")
        self._estado = 'cancelada'
        print(f"Reserva cancelada: {self._cliente.mostrar_info()}")

    def procesar_reserva(self):
        """Procesa la reserva, calculando el costo."""
        try:
            costo = self._servicio.calcular_costo(self._duracion)
            print(f"Reserva procesada. Costo: {costo}")
        except ValueError as e:
            print(f"Error al procesar la reserva: {e}")
            self.registrar_error(str(e))

    def registrar_error(self, mensaje):
        """Registra errores en un archivo de log."""
        with open("logs.txt", "a") as log_file:
            log_file.write(f"Error: {mensaje}\n")


# -----------------------------------------
# 5. Manejo de excepciones personalizadas
# -----------------------------------------
class ErrorSistema(Exception):
    """Excepción personalizada para errores graves del sistema."""
    def __init__(self, mensaje):
        super().__init__(mensaje)


# -----------------------------------------
# 6. Simulación de operaciones completas (10 operaciones)
# -----------------------------------------
def simular_operaciones():
    operaciones = []
    try:
        # 1. Operación: Crear cliente válido
        cliente1 = Cliente("Carlos", "carlos@correo.com", "987654321")
        cliente1.registrar()
        operaciones.append("Cliente Carlos registrado correctamente.")
        
        # 2. Operación: Crear cliente con datos inválidos (correo)
        try:
            cliente_invalido = Cliente("Juan", "juancorreo.com", "987654322")
        except ValueError as e:
            operaciones.append(f"Error al registrar cliente Juan: {e}")
        
        # 3. Operación: Crear servicio válido (ReservaSala)
        servicio1 = ReservaSala("Sala A", "Sala de reuniones con proyector")
        operaciones.append(f"Servicio {servicio1.mostrar_info()} creado correctamente.")
        
        # 4. Operación: Crear servicio inválido (sin nombre ni descripción)
        try:
            servicio_invalido = AsesoriaEspecializada("", "")
            operaciones.append(f"Servicio {servicio_invalido.mostrar_info()} creado.")
        except Exception as e:
            operaciones.append(f"Error al crear servicio de asesoría: {e}")
        
        # 5. Operación: Crear reserva válida
        reserva1 = Reserva(cliente1, servicio1, 2)  # 2 horas
        reserva1.confirmar_reserva()
        reserva1.procesar_reserva()
        operaciones.append("Reserva 1 procesada correctamente.")
        
        # 6. Operación: Intentar confirmar una reserva ya confirmada
        try:
            reserva1.confirmar_reserva()
        except ValueError as e:
            operaciones.append(f"Error al confirmar reserva: {e}")
        
        # 7. Operación: Crear segunda reserva válida
        cliente2 = Cliente("Ana", "ana@correo.com", "123456789")
        servicio2 = AlquilerEquipo("Proyector", "Alquiler de proyector")
        reserva2 = Reserva(cliente2, servicio2, 3)  # 3 horas
        reserva2.confirmar_reserva()
        reserva2.procesar_reserva()
        operaciones.append("Reserva 2 procesada correctamente.")
        
        # 8. Operación: Intentar cancelar una reserva ya procesada
        try:
            reserva2.cancelar_reserva()
        except ValueError as e:
            operaciones.append(f"Error al cancelar reserva: {e}")
        
        # 9. Operación: Reserva con parámetros faltantes
        try:
            reserva_incompleta = Reserva(cliente1, None, 0)  # Servicio None
            reserva_incompleta.procesar_reserva()
        except Exception as e:
            operaciones.append(f"Error al procesar reserva incompleta: {e}")
        
        # 10. Operación: Cliente con datos faltantes
        try:
            cliente_faltante = Cliente("", "", "")
        except ValueError as e:
            operaciones.append(f"Error al registrar cliente faltante: {e}")
        
    except Exception as e:
        print(f"Error en la simulación: {e}")
    
    # Mostrar resultados de la simulación
    for operacion in operaciones:
        print(operacion)


# -----------------------------------------
# 7. Ejecutar simulaciones
# -----------------------------------------
simular_operaciones()