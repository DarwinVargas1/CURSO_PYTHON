import pyautogui
import time

def mover_mouse(intervalo=20, distancia=100):
    """
    Mueve el mouse automáticamente cada 'intervalo' segundos.
    :param intervalo: Tiempo en segundos entre movimientos.
    :param distancia: Distancia en píxeles a mover.
    """
    try:
        print("Presiona Ctrl+C para detener el script.")
        while True:
            x, y = pyautogui.position()  # Posición actual
            pyautogui.moveTo(x + distancia, y, duration=0.3)
            pyautogui.moveTo(x, y, duration=0.3)
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nScript detenido por el usuario.")

if __name__ == "__main__":
    mover_mouse(intervalo=20, distancia=100)
    