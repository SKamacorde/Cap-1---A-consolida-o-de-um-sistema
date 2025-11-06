from src.repository.base_repository import BaseRepository
from src.models.monitoramento import Monitoramento
import oracledb 

class MonitoramentoRepository(BaseRepository):
   
    def buscar_monitoramento(self, cd_monitoramento):
        query = "SELECT * FROM TBL_MONITORAMENTO WHERE cd_monitoramento = :1"
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (cd_monitoramento,))
            row = cursor.fetchone()
            return Monitoramento(*row) if row else None

    def inserir_monitoramento(self, monitoramento):
        conn =  self.get_connection()  
        cursor = conn.cursor()
        try:
            # Variável de retorno para o ID gerado
            cd_monitoramento = cursor.var(oracledb.NUMBER)
            query = "INSERT INTO TBL_MONITORAMENTO (cd_cultura_produto_sensor, vlr_medido , dt_medicao, cd_usuario_inclusao, dt_inclusao) VALUES (:1, :2, :3,:4, :5) RETURNING CD_MONITORAMENTO INTO :6"
            cursor.execute(query, [monitoramento.cd_cultura_produto_sensor, monitoramento.vlr_medido, monitoramento.dt_medicao, monitoramento.cd_usuario_inclusao, monitoramento.dt_inclusao, cd_monitoramento])
            conn.commit() 
            print("Monitoramento inserido com sucesso.")
            novo_id = int(cd_monitoramento.getvalue()[0])
            
            return novo_id            
        except Exception as e:
            print(f"Erro ao inserir monitoramento: {e}")
            conn.rollback()  # ← CORRIGIDO
        finally:
            cursor.close()
    
    def listar_todos(self):
        conn =  self.get_connection()  
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM TBL_MONITORAMENTO"
            cursor.execute(query)
            monitoramentos = [Monitoramento(*row) for row in cursor.fetchall()]
            return monitoramentos
        finally:
            cursor.close()

    def atualizar_monitoramento(self,cd_monitoramento, vlr_medido):
        conn =  self.get_connection()  
        cursor = conn.cursor()
        try:
            query = "UPDATE TBL_MONITORAMENTO  SET vlr_medido =:vlr_medido    WHERE cd_monitoramento = :cd_monitoramento "
            cursor.execute(query, {"vlr_medido": vlr_medido, "cd_monitoramento": cd_monitoramento})
            conn.commit() 
        finally:
            cursor.close()

    def deletar_monitoramento(self, cd_monitoramento):
        conn =  self.get_connection()  
        cursor = conn.cursor()
        try:
            query = "DELETE FROM TBL_MONITORAMENTO  WHERE cd_monitoramento = :1 "
            cursor.execute(query, (cd_monitoramento,))
            conn.commit() 
        finally:
            cursor.close()