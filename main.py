from savejson import writeAJson
from database import Database


db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

# clienteB = db.collection.aggregate([
#      {"$match": {"cliente_id": "B"}},
#      {"$unwind": "$produtos"},
#      {"$project": {"valor_total": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}},
#      {"$group": {"_id": "$_id", "total_gasto": {"$sum": "$valor_total"}}}
#  ])
#
# writeAJson(clienteB, "exercicio1")

# lesssold = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": "$produtos.nome", "vendido": {"$sum": "$produtos.quantidade"}}},
#     {"$sort": {"vendido": 1}},
#     {"$limit": 1}
# ])
#
# writeAJson(lesssold, "exericio2")

# smallestbuyout = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente_id": "$cliente_id", "compra_id": "$_id"}, "total_compra": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$group": {"_id": "$_id.cliente_id", "menor_compra": {"$min": "$total_compra"}}},
#     {"$sort": {"menor_compra": 1}},
#     {"$limit": 1}
# ])
#
# writeAJson(smallestbuyout, "exercicio3")

sold_morethan_2 = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$match": {"produtos.quantidade": {"$gt": 2}}},
    {"$group": {"_id": "$produtos.nome"}}
])

writeAJson(sold_morethan_2, "exercicio4")