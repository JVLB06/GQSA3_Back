class ProductModel:
    def __init__(self, name, description, receiver_id, product_id=None):
        self.id = product_id
        self.name = name
        self.description = description
        self.receiver_id = receiver_id 

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "receiver_id": self.receiver_id
        }