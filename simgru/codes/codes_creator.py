import json

def get_ae():
    file = open("simgru/codes/ae.json")
    data = json.load(file)
    aes = []

    for atr in data["atributos"]:
        aes.append({
            "id": atr["id"],
            "descripcion": atr["descripcion"]
        })

    file.close

    return {"atributos" : aes}

def get_ae_crit(ae_id: int):
    file = open("simgru/codes/ae.json")
    data = json.load(file)
    crits = []

    for crit in data["atributos"][ae_id]["cd"]:
        crits.append({
            "id": crit["id"],
            "descripcion": crit["descripcion"]
        })

    file.close

    return {
        "atributo": {
            "id": data["atributos"][ae_id]["id"],
            "descripcion": data["atributos"][ae_id]["descripcion"]
        },
        "criterios" : crits
    }

def get_ae_crit_ind(ae_id: int, crit_id: int):
    file = open("simgru/codes/ae.json")
    data = json.load(file)
    inds = []

    for ind in data["atributos"][ae_id]["cd"][crit_id]["indicadores"]:
        inds.append({
            "id": ind["id"],
            "descripcion": ind["descripcion"]
        })

    file.close

    return {
        "atributo": {
            "id": data["atributos"][ae_id]["id"],
            "descripcion": data["atributos"][ae_id]["descripcion"]
        },
        "criterio" : {
            "id": data["atributos"][ae_id]["cd"][crit_id]["id"],
            "descripcion": data["atributos"][ae_id]["cd"][crit_id]["descripcion"]
        },
        "indicadores": inds
    }

def create_code(ae:int, cd: int, i: int) -> dict:
    return {
        "code": f'<AE{ae}CD{cd}I{i}>'
    }

if __name__ == "__main__":
    print(get_ae())