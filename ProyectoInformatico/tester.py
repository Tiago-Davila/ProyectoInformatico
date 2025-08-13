import cv2
import os

def probar_dispositivos_video(max_dispositivos=5):
    print("🔍 Buscando dispositivos de cámara disponibles...")

    for i in range(max_dispositivos):
        path = f"/dev/video{i}"
        if os.path.exists(path):
            print(f"\n🎥 Probando {path} (índice {i})...")
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print(f"✅ Cámara encontrada en {path} (índice {i})")
                ret, frame = cap.read()
                if ret:
                    print(f"📸 Se pudo capturar imagen desde {path}")
                    cv2.imshow(f"Vista previa de {path}", frame)
                    cv2.waitKey(1000)  # Muestra por 1 segundo
                    cv2.destroyAllWindows()
                else:
                    print(f"⚠️ No se pudo capturar imagen desde {path}")
                cap.release()
            else:
                print(f"❌ No se pudo abrir la cámara en {path}")
        else:
            print(f"⛔ {path} no existe")

    print("\n✅ Prueba finalizada.")

probar_dispositivos_video()
