#入力用シート2の縦横変換
#処理をする前にexcelの形式をxlsxに変更しておく

import pandas as pd
import openpyxl 

df = pd.DataFrame()

#処理するEXCLEファイルは、c:/work/dataのフォルダーに保存しておく
♯フォルダー名を変更する場合は、以下の行のxlsxの保存先を修正する
df_sheet_name = pd.read_excel('C:/work/data/【完成版】ぎふの学校図書館データ調査票_令和7年度版.xlsx', sheet_name='入力用シート2', index_col=0, engine='openpyxl')

df_sheet_name = df_sheet_name.T
df_sheet_name = df_sheet_name.map(lambda x: x.replace('\n', '').replace('\r', '') if isinstance(x, str) else x)
#df_sheet_name = df_sheet_name.map(lambda x: x.replace('\n', '').replace('\r', '') if isinstance(x, str) else x)

temp_df= df_sheet_name
temp_df.columns = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 
    '31', '32', '33', '34']

df = pd.concat([df, temp_df], ignore_index=True)

# 1行目を削除する場合
df = df.drop(0)
#print(df)

# xlsx形式で出力し、シート名はstat2とする場合
#df.to_excel('C:\work/data/stat2025_2.xlsx', sheet_name='stat2')

# TSV形式でindexを出力し、なおかつindexの列名をcol0と設定する場合
df.to_csv('C:\work/data/stat2025_2.tsv', sep='\t', index=True, index_label='col0')
sa
