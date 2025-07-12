import json

def cargar_ensayos(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def evaluar_paciente(paciente, ensayos):
    resultados = []
    edad = int(paciente["edad"]) if paciente["edad"] else None
    for ensayo in ensayos:
        status = "ELIGIBLE"
        motivos = []
        faltante = []

        if edad is None:
            status = "POTENTIALLY ELIGIBLE"
            faltante.append("Edad")
        elif not (ensayo["edad_min"] <= edad <= ensayo["edad_max"]):
            status = "NOT ELIGIBLE"
            motivos.append("Edad fuera de rango")

        if ensayo["diagnostico_requerido"] not in paciente["diagnostico_primario"].lower():
            status = "NOT ELIGIBLE"
            motivos.append("Diagnóstico incompatible")

        # Repite para otros criterios...

        resultados.append({
            "nombre": ensayo["nombre"],
            "estado": status,
            "motivos": motivos,
            "faltante": faltante
        })
    return resultados

# Ejemplo de uso:
if __name__ == "__main__":
    paciente = json.loads(open("paciente_extraido.json").read())
    ensayos = cargar_ensayos("ensayos.json")
    elegibilidad = evaluar_paciente(paciente, ensayos)
    print(json.dumps(elegibilidad, indent=2, ensure_ascii=False))
