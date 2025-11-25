class ProductModel:
    def __init__(self, causeId, name, description, value, productId=None):
        
        self.productId = productId
        self.causeId = causeId
        self.name = name
        self.description = description
        self.value = value

    def to_dict(self):
        return {
            "productId": self.productId,
            "causeId": self.causeId,
            "name": self.name,
            "description": self.description,
            "value": self.value
        }