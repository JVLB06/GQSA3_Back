from unittest.mock import MagicMock, patch
import pytest

from src.Model.ProductModel import ProductModel
from src.Helper.ProductHelper import ProductHelper

# Mock do objeto de retorno da Conexão
class MockConnection:
    def cursor(self):
        return self.mock_cursor
    def commit(self):
        pass
    def rollback(self):
        pass
    def close(self):
        pass

# Fixture para configurar o ambiente de teste do Helper
# O @pytest.fixture garante que este código rode antes de cada teste
@pytest.fixture
def product_helper_setup():
    # 1. Mock do cursor e da conexão
    mock_cursor = MagicMock()
    mock_conn = MockConnection()
    mock_conn.mock_cursor = mock_cursor
    
    # 2. Patch do ConnectionHelper para injetar nossa conexão mockada
    with patch('src.Helper.ConnectionHelper.ConnectionHelper') as MockConnectionHelper:
        MockConnectionHelper.return_value.get_connection.return_value = mock_conn
        
        # 3. Yield fornece o objeto a ser usado no teste
        helper = ProductHelper()
        yield helper, mock_cursor, mock_conn # Retorna os objetos necessários para os testes

# --- Funções de Teste ---

def test_create_product_success(product_helper_setup):
    """Testa se o produto é criado e o commit é chamado."""
    helper, mock_cursor, mock_conn = product_helper_setup
    
    test_product = ProductModel(
        causeId=101, 
        name="Produto Teste", 
        description="Descrição para teste", 
        value=50.00
    )
    
    # Simula o retorno do ID (1) após o INSERT
    mock_cursor.fetchone.return_value = (1,)
    
    new_id = helper.create_product(test_product)
    
    # Asserts Pytest (simples e diretos)
    assert mock_cursor.execute.called # Verifica se o SQL foi executado
    assert mock_conn.commit.called    # Verifica se o commit foi chamado
    assert new_id == 1                # Verifica o ID retornado

def test_update_product_success(product_helper_setup):
    """Testa se o produto é alterado e retorna True."""
    helper, mock_cursor, mock_conn = product_helper_setup
    
    test_product_update = ProductModel(
        productId=5, causeId=101, name="Produto Atualizado",
        description="Nova descrição", value=75.50
    )
    
    # Simula que 1 linha foi afetada
    mock_cursor.rowcount = 1
    
    result = helper.update_product(test_product_update)
    
    assert mock_cursor.execute.called
    assert mock_conn.commit.called
    assert result is True # Usa 'is True' em vez de self.assertTrue(result)

def test_get_product_by_id_found(product_helper_setup):
    """Testa a busca de produto quando o ID é encontrado."""
    helper, mock_cursor, mock_conn = product_helper_setup

    # Simula o registro do banco: (id, id_causa, nome, descricao, valor)
    db_record = (5, 101, "Produto X", "Detalhes X", 99.99)
    mock_cursor.fetchone.return_value = db_record
    
    product = helper.get_product_by_id(5)
    
    assert mock_cursor.execute.called
    assert isinstance(product, ProductModel)
    assert product.value == 99.99
    assert product.productId == 5