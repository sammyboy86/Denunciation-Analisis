    

import recordlinkage as rl
from recordlinkage.preprocessing import clean
import numpy as np    


def estandarizacion(dataframe, colonias, alcaldias):

    def estandarizar_numeros(df, columna):


        df[columna] = " " + df[columna] + " "

        letras = [' once ', ' doce ', ' trece ', ' catorce ', ' quince ', ' dieciseis ', ' diecisiete ', ' dieciocho ', \
            ' diecinueve ', ' veinte ' , ' veintuno ', ' veintidos ', ' veintitres ', ' veinticuatro ', ' veinticinco ',\
                ' veintiseis ', ' veintisiete ', ' veintiocho ', ' veintinueve ', ' treinta ', ' treinta y uno ']

        
        romanos = [ (' xiii ',' 13 '), (' xviii ',' 18 '), (' xvii ', ' 17 '), (' xvi ', ' 16 '),\
            (' viii ', ' 8 '), (' vii ', ' 7 '), (' iii ', ' 3 '), (' xii ', ' 12 '), (' ii ', ' 2 '),\
            (' vi ', ' 6 '), (' xiv ', ' 14 '),(' iv ', ' 4 '), (' xv ', ' 15 '), (' v ', ' 5 '),\
                (' xix ', ' 19 '), (' xi ', ' 11 '), (' xx ', ' 20 '), (' ix ', ' 9 '),\
                (' i ', ' 1 '),(' x ', ' 10 ')]


        df[columna].replace(' uno | 1(ro|ra|o|a|er|°|$)* | primer(a|o)* ' , ' 1 ', regex=True, inplace=True)
        df[columna].replace(' dos | 2(do|da|o|a|°|$)* | segund(a|o)' , ' 2 ', regex=True, inplace=True)
        df[columna].replace(' tres | 3(ro|ra|o|a|er|°|$)* | tercer(a|o) * ', ' 3 ', regex=True, inplace=True)
        df[columna].replace(' cuatro | 4(to|ta|o|a|°|$)* | cuart(a|o) ', ' 4 ', regex=True, inplace=True)
        df[columna].replace(' cinco | 5(to|ta|o|a|°|$)* | quint(a|o) ', ' 5 ', regex=True, inplace=True)
        df[columna].replace(' seis | 6(to|ta|o|a|°|$)* | sext(a|o) ', ' 6 ', regex=True, inplace=True)
        df[columna].replace(' siete | 7(mo|ma|o|a|°|$)* | septim(a|o) ', ' 7 ', regex=True, inplace=True)
        df[columna].replace(' ocho | 8(vo|va|o|a|°|$)* | octav(a|o) ', ' 8 ', regex=True, inplace=True)
        df[columna].replace(' nueve | 9(no|na|o|a|°|$)* | noven(a|o) ', ' 9 ', regex=True, inplace=True)
        df[columna].replace(' diez | 10(mo|ma|o|a|°|$)* | decim(a|o) ', ' 10 ', regex=True, inplace=True)
        
        for letra, numero in zip(letras, range(11, 32)):
            df[columna].replace(letra, " " + str(numero) + " ", regex=True, inplace=True)
        
        for romano in romanos:
            df[columna].replace(romano[0], romano[1], regex=True, inplace=True)
        
        df[columna].replace("  ", " ", regex=True, inplace=True)
        df[columna] = df[columna].str[1:-1]

        

    def limpiar_colonias(df, columna):
        """
        Limpieza la columna columna: quita (pblo) y números

        Recibe: 
        - df: DataFrame al que pertenece la columna que se limpiará.
        - columna: Columna del DataFrame a la que se aplicará la limpieza.
        
        """
        estandarizar_numeros(df, columna)
        df[columna] = df[columna].replace(" \(pblo\)", "", regex=True)
        df[columna] = df[columna].replace(" \(ampl\)", " amp ", regex=True)
        df[columna] = df[columna].replace(" \(u hab\)", "", regex=True)
        df[columna] = df[columna].replace(" \(rcnda\)", "", regex=True)
        df[columna] = df[columna].replace(" \(fracc\)", "", regex=True)
        df[columna] = df[columna].replace(" \(barr\)", "", regex=True)
        df[columna] = df[columna].replace(" \(conj hab\)", "", regex=True)
        df[columna] = df[columna].replace("-", " ", regex=True)
        df[columna] = df[columna].replace(" sta ", " santa ", regex=True)
        df[columna] = df[columna].replace(" sto ", " santo ", regex=True)

    dataframe[colonias]= rl.preprocessing.clean(dataframe[colonias], strip_accents='ascii', remove_brackets=False)
    dataframe[alcaldias] = rl.preprocessing.clean(dataframe[alcaldias], strip_accents='ascii', remove_brackets=False)

    limpiar_colonias(dataframe, colonias)
    limpiar_colonias(dataframe, alcaldias)

def actualizar_colonias_paot(df_paot, colonias_matched):
    for index in range(colonias_matched.shape[0]):
        df_paot.loc[(df_paot['colonia']==colonias_matched.iloc[index, 2]) & (df_paot['alcaldia']==colonias_matched.iloc[index, 1]), 'cve_col'] =  colonias_matched.iloc[index, 4]
        df_paot.loc[(df_paot['colonia']==colonias_matched.iloc[index, 2]) & (df_paot['alcaldia']==colonias_matched.iloc[index, 1]), 'colonia'] = colonias_matched.iloc[index, 3]
       
       



def limpiar_encabezados(df):
    """
    Limpieza de encabezados de columnas: cambia a minúsculas, quita acentos y cambia espacios por _ 

    Recibe: 
      - df: DataFrame al que se le hará limpieza de columnas.   

    """
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('ó', 'o')
    df.columns = df.columns.str.replace('í', 'i')
    df.columns = df.columns.str.replace('é', 'e')
    df.columns = df.columns.str.replace('á', 'a')

def preparacion_enriquecimiento(df_og, alcaldias_og, colonias_og,  id_denuncia_og):
    df_a_enriquecer = df_og.groupby([alcaldias_og,colonias_og]).count().loc[:,[id_denuncia_og]]

    df_a_enriquecer= df_a_enriquecer.rename(columns={id_denuncia_og:'num_denuncias'})
    return df_a_enriquecer

def enriquecimiento(df_a_enriquecer, df_externo, alcaldias_externo, colonias_externo, columnas_de_interes,nombre,tipo):

    if(tipo=='conteo'):
        df_externo_gb = df_externo.groupby([alcaldias_externo, colonias_externo]).count()
    elif(tipo=='suma'):
        df_externo_gb = df_externo.groupby([alcaldias_externo, colonias_externo]).sum()
    else:
        df_externo_gb = df_externo.groupby([alcaldias_externo,colonias_externo]).mean()

    index = 0        

    for columna in columnas_de_interes:

        df_a_enriquecer[nombre[index]] = np.nan

        for i in df_a_enriquecer.index:
            
            datos_externos_temp = df_externo_gb[df_externo_gb.index==i]
            
            if(not datos_externos_temp.empty):    
                df_a_enriquecer.loc[i[0]].loc[i[1], nombre[index]] = datos_externos_temp.iloc[0][columna]
    
        df_a_enriquecer[nombre[index]] = df_a_enriquecer[nombre[index]].astype('float64')
    
        index = index +1
