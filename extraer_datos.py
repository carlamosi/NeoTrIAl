import subprocess
import json

def analizar_historia_clinica(texto):
    prompt = f"""Lee el siguiente texto médico (en catalán o español) y extrae la siguiente información:
- Edad
- Diagnóstico primario
- Tiempo desde diagnóstico
- Síntomas clave (y severidad)
- Antecedentes médicos relevantes
- Tratamientos actuales
- Factores de exclusión potenciales

Devuelve la información en formato JSON como este ejemplo:
{{
  "edad": "",
  "diagnostico_primario": "",
  "tiempo_desde_diagnostico": "",
  "sintomas": "",
  "antecedentes": "",
  "tratamientos": "",
  "exclusiones": ""
}}
Texto: {texto}
"""
    result = subprocess.run(
        ["ollama", "run", "mistral:instruct", prompt],
        capture_output=True, text=True
    )
    return result.stdout

# Ejemplo de uso:
if __name__ == "__main__":
    historia = "Pacient de 63 anys diagnosticat d'insuficiència cardíaca fa 2 anys..."
    datos = analizar_historia_clinica(historia)
    print(datos)
