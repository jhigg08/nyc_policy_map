# NYC Policy Map 🗺️

An interactive, browser-based map that displays all 51 NYC City Council districts, along with sample policy highlights and elected official information for each district.

Built using HTML, CSS, JavaScript, and Leaflet.js. Fully functional with dummy data for demonstration.

---

## 🔍 Project Overview

This project visualizes NYC Council districts using real geographic boundary data and displays policy-related information for each district. Users can:

- Click on any district to view information in a sidebar
- Search by district number
- Filter districts by policy categories like housing or education

The project runs entirely in the browser using static files — no backend required.

---

## 💻 Tech Stack

- **HTML** / **CSS** / **JavaScript** – Core web technologies
- **[Leaflet.js](https://leafletjs.com/)** – JavaScript library for interactive maps
- **GeoJSON** – for district boundary data
- **JSON** – for elected officials and policy highlights

---

## ✅ Features

- 🗺️ Interactive map of all 51 NYC Council districts  
- 🎨 Districts color-coded by borough  
- 📌 Sidebar with council member, term start, and 3 sample policies  
- ✏️ Click-to-highlight the selected district  
- 🔎 Search bar for jumping to a specific district  
- 🧠 Filter by policy keywords (e.g., "housing", "education")  
- 🧪 Dummy data for all 51 districts for demo purposes

---

## 🚀 Running the Project Locally

1. Clone or download this repository
2. Make sure you have Python installed
3. In your terminal:

   ```bash
   cd nyc_policy_map
   python -m http.server 8000
