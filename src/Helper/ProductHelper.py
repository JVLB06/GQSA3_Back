from src.Helper.ConnectionHelper import ConnectionHelper
from datetime import datetime

class ProductHelper:
    def __init__(self):
        self.conn = ConnectionHelper().get_connection()
        self.cursor = self.conn.cursor()

    def create_product(self, product):
      
        try:
            
            query = """
                INSERT INTO produtos (id_causa, nome, descricao, valor, data_cadastro)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id_produto;
            """
            
            createdAt = datetime.now()
            
            
            self.cursor.execute(query, (
                product.causeId,      
                product.name,         
                product.description,  
                product.value,        
                createdAt             
            ))
            
            new_id = self.cursor.fetchone()[0]
            self.conn.commit()
            return new_id

        except Exception as e:
            self.conn.rollback()
            print(f"Error creating product: {e}")
            return None

    def update_product(self, product):
        
        try:
            
            query = """
                UPDATE produtos 
                SET nome = %s, descricao = %s, valor = %s
                WHERE id_produto = %s AND id_causa = %s;
            """
            
            self.cursor.execute(query, (
                product.name,        
                product.description, 
                product.value,       
                product.productId,   
                product.causeId      
            ))
            
            self.conn.commit()
            
            return self.cursor.rowcount > 0

        except Exception as e:
            self.conn.rollback()
            print(f"Error updating product: {e}")
            return False

    def __del__(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()