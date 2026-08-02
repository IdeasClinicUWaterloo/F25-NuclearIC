# 🚚 Nuclear Transport Route Optimization Challenge

Welcome to the Nuclear Transport Route Optimization Challenge!

This challenge is presented by Canadian Nuclear Laboratories (CNL). Your objective is to design a route optimization system that safely transports spent nuclear fuel while considering environmental hazards and essential resources such as refuelling stations.

---

# Accessibility

This README has been designed to be accessible to a wide range of users. It uses descriptive headings, plain language, and organized sections to improve navigation for keyboard users and screen readers.

When images, screenshots, or diagrams are included:

- Provide concise and descriptive alternative (alt) text.
- Mark decorative images as decorative so they are ignored by assistive technologies.
- Do not rely solely on images to communicate important information.
- Provide all code examples as selectable text instead of screenshots whenever possible.

---

# Table of Contents

- [Challenge Overview](#challenge-overview)
- [Your Mission](#your-mission)
- [Challenge Resources](#challenge-resources)
- [Tutorial Overview](#tutorial-overview)
- [Project Setup](#project-setup)
- [Creating the Nuclear Location File](#creating-the-nuclear-location-file)
- [Route Optimization](#route-optimization)
- [Hazard Detection](#hazard-detection)
- [Refuelling Optimization](#refuelling-optimization)

---
# Quick Links

> **Navigation Tip:** Screen reader users can navigate this document using heading levels. Keyboard users can use the Table of Contents above to quickly move between sections.

### Documentation

- Python Downloads
- Visual Studio Code Downloads
- Visual Studio Code Getting Started Guide
- GeoJSON.io

### Challenge Resources

- Ontario Road Network Data
- Nuclear Site Coordinates
- Hazard Location Data
- Refuelling Station Coordinates

---

# Challenge Overview

Spent nuclear fuel must be transported safely from nuclear facilities across Ontario to the long-term nuclear waste repository located in Ignace, Ontario.

During transportation, trucks may encounter environmental hazards that affect the safest available route. These hazards can include:

- Forest fires
- Flooding
- Snow and ice
- Road closures
- Other environmental obstacles

Transport vehicles must also stop at refuelling stations when necessary. For this challenge, assume each truck can travel a maximum of **1,200 kilometres** before refuelling.

Your routing system should determine the safest and most efficient path while avoiding hazards and ensuring the vehicle reaches its destination successfully.

# Your Mission

Design a route optimization system that safely transports spent nuclear fuel between nuclear facilities and the storage repository.

Your solution should:

- Calculate efficient transportation routes.
- Avoid hazardous environmental areas.
- Determine when refuelling is required.
- Select appropriate refuelling stations.
- Safely guide the truck to its destination.

# Challenge Resources

The following resources are provided to help you complete this challenge.

| Resource | Purpose |
|----------|---------|
| Ontario Road Network Graph | Road network used for routing calculations. |
| Nuclear Site Coordinates | Starting and destination locations. |
| Hazard Coordinates | Environmental hazards to avoid during routing. |
| Refuelling Station Coordinates | Available truck stops for refuelling. |

These resources are available through the course materials.

---

## Tutorial

The following is a guide to an example of one of the many potential solutions.

This particular solution uses the haversine formula to calculate the great circle distance between two points on Earth as a heuristic for the A* search algorithm. It provides a "straight line" approximation of the shortest path over the curvature of the Earth's surface to determine the optimal route.

We will walk through the process of defining our heuristic, finding the nearest nodes to sites, calculating routes, creating a map, populating the map, and navigating the hazards and refuelling stations.

<img src="/Route_Optimization_Subproblem/images/Optimized_Route_Map.png" alt="Optimized nuclear route map from example solution">

## Image Accessibility

If screenshots, maps, or diagrams are added to this README, each image should include descriptive alternative text.

Examples include:

✔ Map showing an optimized truck route between a nuclear facility and Ignace.

✔ Screenshot of the completed route displayed in a web browser.

✔ Diagram illustrating the routing process with hazard avoidance.

Decorative images should be marked as decorative so they are ignored by screen readers.

## Setup

Before starting, make sure you have Python installed:
-   You can download Python here: https://www.python.org/downloads/
-   You can download VSCode here: https://code.visualstudio.com/download
-   And here is a link to a tutorial on how to use VSCode if needed: https://code.visualstudio.com/docs/getstarted/getting-started

### Creating a Virtual Environment
A Python virtual environment (venv) is a self-contained directory that allows you to install packages and dependencies for a specific project without affecting the global Python installation or other projects.

1. Open a terminal in VS Code and use `cd [insert absolute path to your project locally]` to navigate to the directory where you want to store your project files.
2. Create a venv:
    - Enter `python -m venv [name-of-your-venv]` in the same terminal. 
    This should create a new folder with the name of your venv under your directory
3. Activate the venv:
    - For Mac/Linux users: `source ./name-of-your-venv/bin/activate `
    - For Windows users: `.\name-of-your-venv\Scripts\activate`
    - When prompted, type R and then enter to run once
    - You should now see `(name-of-your-venv)` being appended to your input prompt, indicating that you have activated your venv

### Install Python Libraries

-   **OSMnx**: To download, model, analyze, and visualize street networks and other geospatial features from OpenStreetMap
-   **NetworkX**: For the creation, manipulation, and study of the structure, dynamics, and functions of complex networks
-   **GeoPandas**: For working with geospatial data
-   **Folium**: For creating interactive web maps
-   **Scikit-Learn**: For statistical modeling

You can download the above Python libraries in your virtual environment by entering this one-line command in your terminal (Command Prompt on Mac or PowerShell on Windows):
```
pip install osmnx networkx geopandas folium scikit-learn
```

## Walkthrough

We have supplied the map data on Learn to be used to create your maps and routes. It is called "ontario_drive_network.graphml". Download it. 
Make sure to keep all the files used in this project in the same folder. 

### Create Nuclear Location File
First, we will need a .geojson file to hold site names and coordinates.
A CSV file of the nuclear sites and their coordinates has been provided. Open this file in [GeoJSON.io](https://geojson.io/#map=2/0/20) and save it as a GeoJSON file. You can find more detailed instructions [here](https://support.planet.com/hc/en-us/articles/360016337117-Creating-a-GeoJSON-file).

<!-- <img src="/Route_Optimization_Subproblem/images/geojson.png" alt="GeoJSON file" height="250"> -->
```
{
  "type": "FeatureCollection",
  "features": [
    { "type": "Feature", "properties": { "Name": "Bruce Power" }, "geometry": { "type": "Point", "coordinates": [-81.57483, 44.318372] } },
    { "type": "Feature", "properties": { "Name": "Pickering" }, "geometry": { "type": "Point", "coordinates": [-79.061188, 43.815166] } },
    { "type": "Feature", "properties": { "Name": "Darlington" }, "geometry": { "type": "Point", "coordinates": [-78.724706, 43.869439] } },
    { "type": "Feature", "properties": { "Name": "Chalk River" }, "geometry": { "type": "Point", "coordinates": [-77.43291206, 46.02255149] } },
    { "type": "Feature", "properties": { "Name": "CNL Pinawa" }, "geometry": { "type": "Point", "coordinates": [-96.060923, 50.177626] } },
    { "type": "Feature", "properties": { "Name": "Ignace" }, "geometry": { "type": "Point", "coordinates": [-91.988974, 49.448361] } }
  ]
}
```
Ensure that this new file is also in your project folder.

From here, we can open our folder in VS Code and create a new file for our main code. We need to import some libraries.
```
import osmnx as ox      
import networkx as nx 
import geopandas as gpd
import folium       
from shapely.geometry import Point      
from math import radians, cos, sin, sqrt, atan2     
from shapely.ops import unary_union     
import pandas as pd     
```
<!-- <img src="/Route_Optimization_Subproblem/images/import_libraries.png" alt="Import code" height="150"> -->

| Import code         | Purpose                                                  |
| ------------- | -------------------------------------------------------- |
| **import osmnx as ox**     | Downloads Ontario's real road network from OpenStreetMap |
| **import networkx as nx**  | Calculates the shortest route using A\* search algorithm |
| **import geopandas as gpd** | Reads the nuclear site locations from a GeoJSON file     |
| **import folium**    | Draws an interactive map you can view in your browser    |
| **from shapely.geometry import Point** |Used to create our fire source and discourage routing through it|
| **from math import radians, cos, sin, sqrt, atan2**|For dist calculations|
|**from shapely.ops import unary_union** | Combines multiple geometric objects|
  |**import pandas as pd** | Reads CSV file|

### Load Nuclear Location File
This line reads the GeoJSON file we created and confirms for us that the coordinates are in the correct format:
```
sites = gpd.read_file("nuclear_sites.geojson").to_crs(epsg=4326)
```
<!-- <img src="/Route_Optimization_Subproblem/images/load_nuclear_location.png" alt="Load relavent sites from GeoJSON" height="25"> -->

We also want to include the saved file "ON_MB_Road_Data.graphml" to load our map:
```
G = ox.load_graphml("ON_MB_Road_Data.graphml")
```
<!-- <img src="/Route_Optimization_Subproblem/images/load_map.png" alt="Load map file" height="25"> -->

### Defining our Heuristic
We can create a function to calculate the direct distance from a node to a site, which will be used when finding the fastest route. It will take three inputs: the first node, the second node, and the road network.
```
def haversine(n1, n2, G):
    lon1, lat1 = G.nodes[n1]['x'], G.nodes[n1]['y']
    lon2, lat2 = G.nodes[n2]['x'], G.nodes[n2]['y']
    R = 6371  # Earth radius in km
    dlon, dlat = radians(lon2 - lon1), radians(lat2 - lat1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))
```
<!-- <img src="/Route_Optimization_Subproblem/images/def_haversine.png" alt="def_haversine" height="25"> -->

In this function, we first find the longitude and latitude of the nodes from graph G:
```
    lon1, lat1 = G.nodes[n1]['x'], G.nodes[n1]['y']
    lon2, lat2 = G.nodes[n2]['x'], G.nodes[n2]['y']
```
<!-- <img src="/Route_Optimization_Subproblem/images/haversine1.png" alt="Find longitude and latitude" height="50"> -->

Then, we calculate the difference in longitude and latitude. We want to convert this to radians so that we can estimate the distance on the curve of the Earth, as this uses trig functions:
```
    dlon, dlat = radians(lon2 - lon1), radians(lat2 - lat1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
```
<!-- <img src="/Route_Optimization_Subproblem/images/haversine3.png" alt="Distance calculation" height="50"> -->

Finally, we calculate the distance and convert it to kilometres:
```
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))
```
<!-- <img src="/Route_Optimization_Subproblem/images/haversine4.png" alt="Return line" height="25"> -->

### Find Nearest Nodes to Sites
This function specifically locates the nodes for Bruce Power:
```
bruce = ox.distance.nearest_nodes(G, sites[sites["Name"] == "Bruce Power"].geometry.iloc[0].x,
                                     sites[sites["Name"] == "Bruce Power"].geometry.iloc[0].y)
```
<!-- <img src="/Route_Optimization_Subproblem/images/bruce_nearestnode.png" alt="Nearest node to Bruce" height="50"> -->

Repeat this for the other sites of interest (Ignace, Darlington, Chalk River Labs, etc.)

### Map Creation
Now, we have to make some way of actually showing the route we've found, and for that, we have folium. This will create an empty map centred around Ontario:
```
m = folium.Map(location=[sites.geometry.y.mean(), sites.geometry.x.mean()], zoom_start=5)
```
<!-- <img src="/Route_Optimization_Subproblem/images/map_code.png" alt="Map creation" height="25"> -->

### Finding our Routes
We can use a built-in A* algorithm with our haversine heuristic to calculate the most optimal route between sites.
```
route = nx.astar_path(G, start, end, heuristic=lambda a, b: haversine(a,b,G), weight="length")
route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]
folium.PolyLine(route_coords, color="blue", weight=5, tooltip=f"{start_name} to Ignace").add_to(m)
```
<!-- <img src="/Route_Optimization_Subproblem/images/bruce_route.png" alt="Bruce route calculation" height="75"> -->
Again, repeat this for the other sites routing to Ignace.

Now we need to populate it with route data! We can turn each node into a pair of coordinates, then use folium to create a line between them and add it to the map:
```
route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]
folium.PolyLine(route_coords, color="green", weight=5).add_to(m)
```
<!-- <img src="/Route_Optimization_Subproblem/images/route_coords_ex.png" alt="Route Data" height="50"> -->

We want to highlight our sites with special markers for easy reading, which can be done easily by looping through each site with the following code:
```
for name in sites["Name"]:
    row = sites[sites["Name"] == name]
    folium.Marker(
        location=[row.geometry.y.values[0], row.geometry.x.values[0]],
        popup=name,
        icon=folium.Icon(color="purple" if name == "Ignace" else "blue")
    ).add_to(m)
```
<!-- <img src="/Route_Optimization_Subproblem/images/add_markers.png" alt="Add markers manually" height="175"> -->

Finally, we have to save the map so that we can open it in our browser and print out a message confirming that we have saved successfully:
```
m.save("Optimized_Nuclear_Route.html")
print("Map saved as Optimized_Nuclear_Route.html")
```
<!-- <img src="/Route_Optimization_Subproblem/images/save_map.png" alt="Save map" height="50"> -->

### Identify Hazard Location and Radius
<!-- Now that we have functioning code, consider the limitless possible additions to make this solution more realistic. For example, we can add hazards, such as fires. -->
Now that we have functioning code, we can consider other elements such as fires.
You may refer to the provided list of hazardous areas to avoid.

For example, we can set the midpoint of a fire and the size of the area around it:
```
fire_location = Point(-82.7569, 47.5939)
fire_range_deg = 0.1
```
<!-- <img src="/Route_Optimization_Subproblem/images/fire_location.png" alt="Fire location" height="50"> -->

Now that we have set an area for the fire, we have to let the algorithm know that routing through it would be less optimal. To do this, we increase the weighting of the nodes within the specified area.
```
for u, v, key, data in G.edges(keys=True, data=True):
    x = (G.nodes[u]['x'] + G.nodes[v]['x']) / 2
    y = (G.nodes[u]['y'] + G.nodes[v]['y']) / 2
    midpoint = Point(x, y)
    if fire_location.buffer(fire_range_deg).contains(midpoint):
        data["length"] *= 10000
```
<!-- <img src="/Route_Optimization_Subproblem/images/fire_penalty.png" alt="Hazard zone penalty" height="150"> -->

### Refuelling
To tackle the refuelling problem, we first have to load the CSV file of available gas station locations:
```
gas_stations_df = pd.read_csv("Refuelling_Truck_Stops.csv")
```

This converts the latitude and longitude for each gas station into graph nodes, similar to what we did for the nuclear sites. Then we want to save the gas station nodes back into the dataframe for reference:
```
gas_station_nodes = [
    ox.distance.nearest_nodes(G, row["Longitude"], row["Latitude"])
    for _, row in gas_stations_df.iterrows()
]

gas_stations_df["graph_node"] = gas_station_nodes
```

### Calculate route with refuelling in mind
The following checks whether the shortest truck route between our starting point and our destination would require refuelling, then calculates the shortest truck route to each gas station. If the route is shorter than our max distance, 1200 km, it saves that station in an array.
```
max_distance_m = 1_200_000  # 1200 km
reachable_stations = []

if nx.shortest_path_length(G, start, end, weight="length") >= max_distance_m:   
    for _, row in gas_stations_df.iterrows():
        station_node = row["graph_node"]
        try:
            dist_to_station = nx.shortest_path_length(G, start, station_node, weight="length")
            if dist_to_station <= max_distance_m:
                reachable_stations.append((row["Truck stop"], station_node, dist_to_station))
        except nx.NetworkXNoPath:
            continue    # Skip if there's no valid path

else:
    print(f"{start_name} - Destination within 1200 km, no refuelling necessary.")
```                

Within that array, we can look for the route with the maximum distance because we want to refuel as few times as possible:
```
if reachable_stations:
    refuelling_station = max(reachable_stations, key=lambda x: x[2])
    refuelling_station_node = refuelling_station[1]

    print(f"{start_name} - Chosen gas station: {refuelling_station[0]} at {refuelling_station[2]/1000:.2f} km")

else:
    print(f"{start_name} - No gas stations found within 1200 km.")
```
Now that we've identified which gas station we want to stop at, we can use the A* algorithm as mentioned earlier to calculate the path we want to take. We can treat this as two separate paths: from the starting location to the gas station, and from the gas station to the destination.

Okay, let's get on to (in my opinion) the fun part. Remember how we mentioned earlier that we could put in markers for our map? 
You can customize the appearance of these markers. You can choose from a list of [colours](https://www.kaggle.com/code/aungdev/colors-available-for-marker-icons-in-folium), and you can also add [icons](https://fontawesome.com/search?f=classic&s=solid&o=r).
```            
for _, row in gas_stations_df.iterrows():
    station_node = row["graph_node"]
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"⛽ Chosen Gas Station: {row["Truck stop"]}",
        icon=folium.Icon(color="green", icon="gas-pump", prefix="fa")
    ).add_to(m)
```

Well, that's it for now! Remember, you don't have to follow these steps exactly. This guide just helps you get started and provides some building blocks to one of the many possible solutions. We cannot wait to see what unique ideas you come up with. Good luck!
