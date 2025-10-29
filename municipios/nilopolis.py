import pandas as pd
from procedimentos import carregar_ultrassonografia, carregar_us_doppler

def analisar_procedimentos_nilopolis():
    arquivo = "relatório_modificado.xlsx"
    
    try:
        
        ultrassonografias = carregar_ultrassonografia()
        doppler = carregar_us_doppler()
        tabela = pd.read_excel(arquivo)
        
        # print(f"Total de procedimentos na lista: {len(ultrassonografias)}")
        # print(f"Total de linhas no Excel: {len(tabela)}")
        
        coluna_procedimento = 'Nilopolis'
        coluna_quantidade = 'Quantidade Nilopolis'
        
        if coluna_procedimento not in tabela.columns:
            print(f"Coluna '{coluna_procedimento}' não encontrada!")
            print("Colunas disponíveis:", tabela.columns.tolist())
            return
        
        if coluna_quantidade not in tabela.columns:
            print(f"Coluna '{coluna_quantidade}' não encontrada!")
            return
        
        resultados = {}
        ultrassonografia_total = 0
        doppler_total = 0
        
        for procedimento in ultrassonografias:
            mask = tabela[coluna_procedimento].astype(str) == procedimento
            
            quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
            
            if not pd.isna(quantidade) and quantidade > 0:
                resultados[procedimento] = quantidade
                ultrassonografia_total += quantidade

        for procedimento in doppler:
            mask = tabela[coluna_procedimento].astype(str) == procedimento
            
            quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
            
            if not pd.isna(quantidade) and quantidade > 0:
                resultados[procedimento] = quantidade
                doppler_total += quantidade


        print(f"\n--- RESUMO: {coluna_procedimento} ---")
        print(f"Total de procedimentos encontrados: {len(resultados)}")
        print(f"Quantidade ultrassonografias: {ultrassonografia_total}")
        print(f"Quantidade doppler: {doppler_total}")

        return
        
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    print("="*80)