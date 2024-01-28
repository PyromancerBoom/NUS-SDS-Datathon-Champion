import pandas as pd
import folium

file_path = './catA_train.csv'
df = pd.read_csv(file_path)

data = df.dropna(subset=['LATITUDE', 'LONGITUDE',
                 'Sales (Global Ultimate Total USD)', 'Sales (Domestic Ultimate Total USD)']).copy()

# Calculate the weight of each point
# data['weight'] = data['Sales (Global Ultimate Total USD)'] + \
#     data['Sales (Domestic Ultimate Total USD)']

m = folium.Map(zoom_start=2)

for idx, row in data.iterrows():
    folium.CircleMarker(
        location=[row['LATITUDE'], row['LONGITUDE']],
        radius=row['Sales (Domestic Ultimate Total USD)'] / 10000000000,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

m.save('map.html')
