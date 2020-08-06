# data_visualization.py

import json
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('../data/new_data.json') as json_file:
        data = json.load(json_file)

    df = pd.DataFrame(data)

    df.plot(kind="scatter",x="broadband_speed",y="internet_users",title="Hubungan antara kecepatan internet dan pengguna internet")
    plt.show()

    df.plot(kind='scatter', x='population', y='internet_users', title='Hubungan antara populasi dan pengguna internet')
    plt.show()

    df.plot(kind='scatter', x='broadband_speed', y='population', title='Hubungan antara kecepatan internet dan populasi')
    plt.show()

    df.plot(kind="scatter",x="GNI",y="population",title="Hubungan antara GNI dan populasi")
    plt.show()

    df.plot(kind="scatter",x="broadband_speed",y="GNI",title="Hubungan antara kecepatan internet dan GNI")
    plt.show()

    df.plot(kind="scatter",x="GNI",y="internet_users",title="Hubungan antara GNI dan pengguna internet")
    plt.show()

    df2 = df.groupby(['region'])['internet_users'].sum().reset_index()
    plt.title("Persentase Pengguna Internet di Dunia")
    plt.pie(df2['internet_users'], autopct='%1.2f%%')
    plt.legend(df2['region'], loc='best')
    plt.show()

    df3 = df.groupby(['region'])['population'].sum().reset_index()
    plt.title("Persentase Populasi di Dunia")
    plt.pie(df3['population'], autopct='%1.2f%%')
    plt.legend(df3['region'], loc='best')
    plt.show()

    df4 = df.groupby(['region'])['population', 'internet_users', 'facebook_subs'].sum().reset_index()
    df4.plot(kind='bar', x='region', y=['population', 'internet_users', 'facebook_subs'])
    plt.title('Perbandingan antara populasi, jumlah pengguna internet, dan jumlah pengguna facebook')
    plt.show()

    df5 = df.groupby(['region'])['GNI'].mean().reset_index()
    plt.title("Persentase GNI di Dunia")
    plt.pie(df5['GNI'], autopct='%1.2f%%')
    plt.legend(df5['region'], loc='best')
    plt.show()

    df6 = df.groupby(['region'])['broadband_speed', 'mobile_speed'].mean().reset_index()
    df6.plot(kind='bar', x='region', y=['broadband_speed', 'mobile_speed'])
    plt.title("Perbandingan Kecepatan internet di Dunia")
    plt.show()

    asia = df.loc[df['region'] == 'Asia']
    print('STD Asia')
    print(asia.std(axis=0, skipna=True))
    print()

    africa = df.loc[df['region'] == 'Africa']
    print('STD Africa')
    print(africa.std(axis=0, skipna=True))
    print()

    America = df.loc[df['region'] == 'America']
    print('STD America')
    print(America.std(axis=0, skipna=True))
    print()

    Europe = df.loc[df['region'] == 'Europe']
    print('STD Europe')
    print(Europe.std(axis=0, skipna=True))
    print()

    Oceania = df.loc[df['region'] == 'Oceania']
    print('STD Oceania')
    print(Oceania.std(axis=0, skipna=True))
    print()

    middle_east = df.loc[df['region'] == 'Middle East']
    print('STD Middle East')
    print(middle_east.std(axis=0, skipna=True))

    # df.to_excel(r'../data/data.xlsx', index=False, header=True)