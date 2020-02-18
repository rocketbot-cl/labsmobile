# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import requests
import urllib.request
import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'labsmobile' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
import xmltodict
import json


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "sendsms":

    username = GetParams('username')
    password = GetParams('password')
    number_ = GetParams('number_')
    sender = GetParams('sender')
    message_ = GetParams('message_')
    var_ = GetParams('var_')

    try:

        res = requests.get(
            "http://api.labsmobile.com/get/send.php?username="+username+"&password="+password+"&msisdn="+number_+"&sender=SENDER&message="+message_+"")
        print('RES1',res.content)


        res = res.text

        code = json.dumps(xmltodict.parse(res))
        code = eval(code)
        code = code['response']
        code.pop('subid')

        SetVar(var_,code)


    except Exception as e:
        PrintException()
        raise e


