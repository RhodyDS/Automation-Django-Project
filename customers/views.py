from django.shortcuts import render, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.views.decorators.csrf import csrf_protect


def listar_clientes(request):
    client = MongoClient("localhost", 27017)
    db = client["Rengage"]
    collection = db["clientes"]
    clientes = collection.find()
    clientes_list = list(clientes)

    return render(
        request, "customers/listar_clientes.html", {"clientes": clientes_list}
    )


def delete_cliente(request, cliente_id):
    client = MongoClient("localhost", 27017)
    db = client["Rengage"]
    collection = db["clientes"]
    cliente_object_id = ObjectId(cliente_id)
    collection.delete_one({"_id": cliente_object_id})

    return redirect("customers")


def edit_cliente(request, cliente_id):
    if request.method == "POST":
        novo_nome = request.POST["user"]
        nova_senha = request.POST["password"]
        client = MongoClient("localhost", 27017)
        db = client["Rengage"]
        collection = db["clientes"]

        cliente_object_id = ObjectId(cliente_id)
        update_data = {"$set": {"user": novo_nome}}

        if nova_senha:
            update_data["$set"]["senha"] = nova_senha

        collection.update_one({"_id": cliente_object_id}, update_data)

        return redirect("customers")

    return redirect("customers")


def adicionar_cliente(request):
    if request.method == "POST":
        novo_nome = request.POST["user"]
        nova_senha = request.POST["password"]

        client = MongoClient("localhost", 27017)
        db = client["Rengage"]
        collection = db["clientes"]

        novo_cliente = {"user": novo_nome, "senha": nova_senha}
        collection.insert_one(novo_cliente)

        return redirect("customers")

    return redirect("customers")
