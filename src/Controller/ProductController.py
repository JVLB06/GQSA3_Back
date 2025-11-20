from Model.ProductModel import ProductModel
from Helper.ProductHelper import ProductHelper

class ProductController:
    def __init__(self):
        self.helper = ProductHelper()

    def register_product(self, name, description, receiver_id):
        if not name:
            return {"status": "error", "message": "Nome é obrigatório"}

        new_product = ProductModel(name, description, receiver_id)
        
        if self.helper.create_product(new_product):
            return {"status": "success", "message": "Produto cadastrado!"}
        else:
            return {"status": "error", "message": "Erro no banco de dados."}

    def edit_product(self, product_id, name, description, receiver_id):
        product_to_update = ProductModel(name, description, receiver_id, product_id)

        if self.helper.update_product(product_to_update):
            return {"status": "success", "message": "Produto atualizado!"}
        else:
            return {"status": "error", "message": "Erro ao atualizar."}