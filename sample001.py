#入力用シート１の縦横変換
#処理をする前にexcelの形式をxlsxに変更しておく

import pandas as pd
import openpyxl 

df = pd.DataFrame()

df_sheet_name = pd.read_excel('C:/work/data/【完成版】ぎふの学校図書館データ調査票_令和7年度版.xlsx', sheet_name='入力用シート１', index_col=0, engine='openpyxl')

#縦横の変換
df_sheet_name = df_sheet_name.T

#　改行とタブの削除
df_sheet_name = df_sheet_name.map(lambda x: x.replace('\n', '').replace('\r', '') if isinstance(x, str) else x)
#df_sheet_name = df_sheet_name.map(lambda x: x.replace('\n', '').replace('\r', '') if isinstance(x, str) else x)

temp_df= df_sheet_name

# 列名の付与
temp_df.columns = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', 
    '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', 
    '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', 
    '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', 
    '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', 
    '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', 
    '81', '82', '83', '84', '85', '86', '87']

df = pd.concat([df, temp_df], ignore_index=True)
#print(df)

# サンプルデータ行の削除する場合
#df = df.drop(2)

# xlsx形式で出力し、シート名はstat1とする場合
#df.to_excel('C:\work/data/stat2025_1.xlsx', sheet_name='stat1')

# TSV形式でindexを出力し、なおかつindexの列名をcol0と設定する場合
df.to_csv('C:\work/data/stat2025_1.tsv', sep='\t', index=True, index_label='col0')
