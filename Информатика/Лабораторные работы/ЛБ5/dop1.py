import pandas as pd
import warnings
from IPython.display import display, HTML

style = """
<style>
.target-table {
    text-align: center;
    border-collapse: collapse;
    width: 100%;
}
.target-table th {
    font-weight: bold;
    padding: 8px;
    text-align: center;
    border: 1px solid #ddd;
}
.target-table td {
    padding: 8px;
    text-align: center;
    border: 1px solid #ddd;
}
.target-table thead tr th {
    text-align: center;
}
.no-header-table {
    border: none !important;
    border-collapse: collapse;
    width: 15%;
}
.no-header-table th {
    display: none !important; 
}
.no-header-table td {
    border: none !important;
    padding: 8px;
    text-align: center;
}
</style>
"""

warnings.filterwarnings('ignore', category=FutureWarning)
sheet = pd.read_excel("C:\\Users\\user\\Desktop\\итмо\\Информатика\\Лабораторные работы\\ЛБ5\\main.xlsx")

input_num = sheet.iloc[2:4, 2:4].copy()

x_data = sheet.iloc[7:19, 1:4].copy()
bin_letter = sheet.iloc[7:19, 7].copy()
bin_number = sheet.iloc[7:19, 9:28].copy()

for index, row in bin_number.iterrows():
    for column in bin_number.columns:
        if bin_number.loc[index,column] != ".":
            bin_number.loc[index,column] = str(bin_number.loc[index,column]).replace(".0","")

whole_bin_number = bin_number.agg("".join, axis=1)

for index, value in whole_bin_number.items():
    if "nan" in value or abs(int(x_data.loc[index][2]))>=2**16:
        whole_bin_number.loc[index] = "-"

target = pd.concat([x_data, bin_letter, whole_bin_number], axis=1)
target.columns = ["Переменная", "Выражение", "Значение выражения", "Двоичная переменная", "Двоичное представление"]

for index, row in target.iterrows():
    for column in target.columns:
        if "=" in str(target.loc[index,column]):
            target.loc[index,column] = str(target.loc[index,column]).replace(" =", "")


display(HTML(style))

display(HTML(input_num.to_html(classes="no-header-table")))
display(HTML(target.to_html(classes='target-table')))

warnings.filterwarnings('default', category=FutureWarning)      