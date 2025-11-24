from src.Helper.ConnectionHelper import ConnectionHelper
from fastapi import HTTPException
from src.Model.DonationModel import DonationModel
from src.Model.ViewDonationModel import ViewDonationModel

class DonationsHelper(ConnectionHelper):
    def list_donations_by_user(self, user_id):
        connection = self.Connection()
        try:
            cursor = connection.cursor()

            query = "SELECT * FROM donations WHERE user_id = %s"
            params = (user_id,)
            
            cursor.execute(query, params)
            results: list[ViewDonationModel] = []

            for row in cursor.fetchall():
                donation = ViewDonationModel(
                    DonorName=row[0],
                    ReceiverName=row[1],
                    Amount=row[2],
                    Date=row[3],
                    ProductName=row[4]
                )
                results.append(donation)
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            connection.close()

    
    def list_donations_received(self, receiver_id):
        connection = self.Connection()
        try:
            cursor = connection.cursor()

            query = "SELECT * FROM donations WHERE user_id = %s"
            params = (receiver_id,)
            
            cursor.execute(query, params)
            results: list[ViewDonationModel] = []

            for row in cursor.fetchall():
                donation = ViewDonationModel(
                    DonorName=row[0],
                    ReceiverName=row[1],
                    Amount=row[2],
                    Date=row[3],
                    ProductName=row[4]
                )
                results.append(donation)
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            connection.close()
    
    def add_donations(self, donation_info: DonationModel):
        connection = self.Connection()

        try:
            query = "INSERT INTO doacoes (id_doador, id_causa, valor_doacao, mensagem, data_doacao) VALUES (%s, %s, %s, %s, %s)"
            params = (donation_info.DonorId, donation_info.ReceiverId, donation_info.Amount, donation_info.Message, donation_info.Date)

            cursor = connection.cursor()
            cursor.execute(query, params)

            connection.commit()
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            connection.close()
        