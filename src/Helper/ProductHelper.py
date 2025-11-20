from Helper.ConnectionHelper import ConnectionHelper

class ProductHelper:
    def __init__(self):
        # Conecta ao banco
        self.connection = ConnectionHelper().get_connection() 
        self.cursor = self.connection.cursor()

    def create_product(self, product):
        query = """
        INSERT INTO products (name, description, receiver_id)
        VALUES (%s, %s, %s)
        """
        values = (product.name, product.description, product.receiver_id)
        
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            return False

    def update_product(self, product):
        query = """
        UPDATE products 
        SET name = %s, description = %s
        WHERE id = %s AND receiver_id = %s
        """
        values = (product.name, product.description, product.id, product.receiver_id)

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            return False