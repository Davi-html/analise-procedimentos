import pandas as pd
arquivo = "relatório_modificado.xlsx"
from procedimentos import (
    carregar_audiometria_tonal,
    carregar_biopsia_mama,
    carregar_biopsia_prostata,
    carregar_cirurgia_oftalmologica,
    carregar_colposcopia,
    carregar_consulta_cardio_com_eletro,
    carregar_consulta_especializadas,
    carregar_consulta_oftalmologia,
    carregar_desintometria,
    carregar_ecocardiografia_transtoracica,
    carregar_eletroencefalograma,
    carregar_eletroneuromiografia,
    carregar_endoscopias_digestivas,
    carregar_espirometria,
    carregar_exames_laboratoriais,
    carregar_fisioterapia_atendimento,
    carregar_fisioterapia_consulta,
    carregar_fornecimento_oculos,
    carregar_ginecologia_citopatologico,
    carregar_holter_24h,
    carregar_mapa,
    carregar_mamografia,
    carregar_polissonografia,
    carregar_potencial_evocado_auditivo,
    carregar_proc_oftalmologico,
    carregar_protese_dentaria,
    carregar_radiografia,
    carregar_ressonancia_magnetica,
    carregar_teste_esforco,
    carregar_tomografia,
    carregar_ultrassonografia,
    carregar_us_doppler,
    carregar_vectoeletronistagmografia,
    carregar_videohisteroscopia,
    carregar_videolaringoscopia,
    carregar_todos_procedimentos
)

coluna_procedimento = 'Nilopolis'
coluna_quantidade = 'Quantidade Nilopolis'
tabela = pd.read_excel(arquivo)
resultados = {}

def carregar_for():
  ultrassonografias = carregar_ultrassonografia()
  doppler = carregar_us_doppler()
  audiometria_tonal = carregar_audiometria_tonal()
  biopsia_mama = carregar_biopsia_mama()
  biopsia_prostata = carregar_biopsia_prostata()
  cirurgia_oftalmologica = carregar_cirurgia_oftalmologica()
  colposcopia = carregar_colposcopia()
  consulta_cardio_com_eletro = carregar_consulta_cardio_com_eletro()
  consulta_especializadas = carregar_consulta_especializadas()
  consulta_oftalmologia = carregar_consulta_oftalmologia()
  desintometria = carregar_desintometria()
  ecocardiografia_transtoracica = carregar_ecocardiografia_transtoracica()
  eletroencefalograma = carregar_eletroencefalograma()
  eletroneuromiografia = carregar_eletroneuromiografia()
  endoscopias_digestivas = carregar_endoscopias_digestivas()
  espirometria = carregar_espirometria()
  exames_laboratoriais = carregar_exames_laboratoriais()
  fisioterapia_atendimento = carregar_fisioterapia_atendimento()
  fisioterapia_consulta = carregar_fisioterapia_consulta()
  fornecimento_oculos = carregar_fornecimento_oculos()
  ginecologia_citopatologico = carregar_ginecologia_citopatologico()
  holter_24h = carregar_holter_24h()
  mapa = carregar_mapa()
  mamografia = carregar_mamografia()
  polissonografia = carregar_polissonografia()
  potencial_evocado_auditivo = carregar_potencial_evocado_auditivo()
  proc_oftalmologico = carregar_proc_oftalmologico()
  protese_dentaria = carregar_protese_dentaria()
  radiografia = carregar_radiografia()
  ressonancia_magnetica = carregar_ressonancia_magnetica()
  teste_esforco = carregar_teste_esforco()
  tomografia = carregar_tomografia()
  vectoeletronistagmografia = carregar_vectoeletronistagmografia()
  videohisteroscopia = carregar_videohisteroscopia()
  videolaringoscopia = carregar_videolaringoscopia()
  todos_procedimentos = carregar_todos_procedimentos()
  
  # Ultrassonografia
  for procedimento in ultrassonografias:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          ultrassonografia_total += quantidade

  # Doppler
  for procedimento in doppler:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          doppler_total += quantidade

  # Audiometria Tonal
  for procedimento in audiometria_tonal:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          audiometria_tonal_total += quantidade

  # Biópsia de Mama
  for procedimento in biopsia_mama:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          biopsia_mama_total += quantidade

  # Biópsia de Próstata
  for procedimento in biopsia_prostata:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          biopsia_prostata_total += quantidade

  # Cirurgia Oftalmológica
  for procedimento in cirurgia_oftalmologica:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          cirurgia_oftalmologica_total += quantidade

  # Colposcopia
  for procedimento in colposcopia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          colposcopia_total += quantidade

  # Consulta Cardio com Eletro
  for procedimento in consulta_cardio_com_eletro:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          consulta_cardio_com_eletro_total += quantidade

  # Consultas Especializadas
  for procedimento in consulta_especializadas:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          consulta_especializadas_total += quantidade

  # Consulta Oftalmologia
  for procedimento in consulta_oftalmologia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          consulta_oftalmologia_total += quantidade

  # Desintometria
  for procedimento in desintometria:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          desintometria_total += quantidade

  # Ecocardiografia Transtorácica
  for procedimento in ecocardiografia_transtoracica:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          ecocardiografia_transtoracica_total += quantidade

  # Eletroencefalograma
  for procedimento in eletroencefalograma:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          eletroencefalograma_total += quantidade

  # Eletroneuromiografia
  for procedimento in eletroneuromiografia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          eletroneuromiografia_total += quantidade

  # Endoscopias Digestivas
  for procedimento in endoscopias_digestivas:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          endoscopias_digestivas_total += quantidade

  # Espirometria
  for procedimento in espirometria:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          espirometria_total += quantidade

  # Exames Laboratoriais
  for procedimento in exames_laboratoriais:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          exames_laboratoriais_total += quantidade

  # Fisioterapia Atendimento
  for procedimento in fisioterapia_atendimento:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          fisioterapia_atendimento_total += quantidade

  # Fisioterapia Consulta
  for procedimento in fisioterapia_consulta:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          fisioterapia_consulta_total += quantidade

  # Fornecimento de Óculos
  for procedimento in fornecimento_oculos:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          fornecimento_oculos_total += quantidade

  # Ginecologia Citopatológico
  for procedimento in ginecologia_citopatologico:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          ginecologia_citopatologico_total += quantidade

  # Holter 24h
  for procedimento in holter_24h:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          holter_24h_total += quantidade

  # M.A.P.A.
  for procedimento in mapa:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          mapa_total += quantidade

  # Mamografia
  for procedimento in mamografia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          mamografia_total += quantidade

  # Polissonografia
  for procedimento in polissonografia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          polissonografia_total += quantidade

  # Potencial Evocado Auditivo
  for procedimento in potencial_evocado_auditivo:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          potencial_evocado_auditivo_total += quantidade

  # Procedimento Oftalmológico
  for procedimento in proc_oftalmologico:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          proc_oftalmologico_total += quantidade

  # Prótese Dentária
  for procedimento in protese_dentaria:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          protese_dentaria_total += quantidade

  # Radiografia
  for procedimento in radiografia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          radiografia_total += quantidade

  # Ressonância Magnética
  for procedimento in ressonancia_magnetica:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          ressonancia_magnetica_total += quantidade

  # Teste de Esforço
  for procedimento in teste_esforco:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          teste_esforco_total += quantidade

  # Tomografia
  for procedimento in tomografia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          tomografia_total += quantidade

  # Vectoeletronistagmografia
  for procedimento in vectoeletronistagmografia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          vectoeletronistagmografia_total += quantidade

  # Videohisteroscopia
  for procedimento in videohisteroscopia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          videohisteroscopia_total += quantidade

  # Videolaringoscopia
  for procedimento in videolaringoscopia:
      mask = tabela[coluna_procedimento].astype(str) == procedimento
      quantidade = tabela.loc[mask, coluna_quantidade].sum() # type: ignore
      if not pd.isna(quantidade) and quantidade > 0:
          resultados[procedimento] = quantidade
          videolaringoscopia_total += quantidade