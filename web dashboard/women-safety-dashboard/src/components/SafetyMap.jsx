import { MapContainer, TileLayer, GeoJSON, Tooltip, Marker, Popup, useMap } from 'react-leaflet';
import { useEffect, useState } from 'react';
import axios from 'axios';
import L from 'leaflet';
import { ResizableBox } from 'react-resizable';
import 'react-resizable/css/styles.css';

const SafetyMap = () => {
  const [geoData, setGeoData] = useState(null);
  const [selectedGridInfo, setSelectedGridInfo] = useState(null);

  // Fetch GeoJSON data from the backend
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/grid-data')
      .then(res => setGeoData(res.data))
      .catch(err => console.error(err));
  }, []);

  // Define a color scale for the safety score (10 intervals)
  const getColor = (score) => {
    if (score > 0.9) return '#003300';
    if (score > 0.8) return '#006400';
    if (score > 0.7) return '#228B22';
    if (score > 0.6) return '#32CD32';
    if (score > 0.5) return '#FFFF00';
    if (score > 0.4) return '#FFD700';
    if (score > 0.3) return '#FF8C00';
    if (score > 0.2) return '#FF4500';
    if (score > 0.1) return '#B22222';
    return '#800000';
  };

  // Define style for each grid (polygon)
  const styleFunction = (feature) => {
    const score = feature.properties.safety_score_norm;
    return {
      fillColor: getColor(score),
      color: 'black',
      weight: 0.5,
      fillOpacity: 0.7,
      opacity: 0.6
    };
  };

  // Define the legend control
  const Legend = () => {
    const map = useMap();

    useEffect(() => {
      const legend = L.control({ position: 'topright' });

      legend.onAdd = function () {
        const div = L.DomUtil.create('div', 'info legend');
        const grades = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9];
        const labels = [
          '< 0.1', '0.1 - 0.2', '0.2 - 0.3', '0.3 - 0.4',
          '0.4 - 0.5', '0.5 - 0.6', '0.6 - 0.7', '0.7 - 0.8',
          '0.8 - 0.9', '> 0.9'
        ];

        div.innerHTML = '<strong>Safety Score</strong><br>';
        grades.forEach((grade, i) => {
          div.innerHTML += `
            <i style="background:${getColor(grade + 0.1)}; width: 20px; height: 20px; display: inline-block; margin-right: 5px;"></i>
            ${labels[i]}<br>
          `;
        });

        return div;
      };

      legend.addTo(map);
      return () => map.removeControl(legend);
    }, [map]);

    return null;
  };

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <ResizableBox
        width={window.innerWidth}
        height={window.innerHeight}
        minConstraints={[300, 300]}
        maxConstraints={[window.innerWidth, window.innerHeight]}
        axis="both"
        resizeHandles={['se']}
        style={{ display: 'block', margin: '0 auto' }}
      >
        <MapContainer center={[13.0827, 80.2707]} zoom={12} style={{ width: '100%', height: '100%' }}>
          <TileLayer
            attribution='&copy; OpenStreetMap contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />

          {geoData && (
            <GeoJSON
              data={geoData}
              style={styleFunction}
              onEachFeature={(feature, layer) => {
                const score = feature.properties.safety_score_norm;
                const cctvCount = feature.properties.cctv_count ?? 0;

                layer.on('click', () => {
                  const center = layer.getBounds().getCenter();
                  setSelectedGridInfo({
                    lat: center.lat,
                    lng: center.lng,
                    cctvCount
                  });
                });

                layer.bindTooltip(`Safety Score: ${score.toFixed(2)}`);
              }}
            />
          )}

          {/* Show CCTV count popup */}
          {selectedGridInfo && (
            <Marker position={[selectedGridInfo.lat, selectedGridInfo.lng]}>
              <Popup>
                <div style={{ textAlign: 'center' }}>
                  <strong>CCTV Count:</strong>
                  <div style={{ fontSize: '18px', margin: '5px 0' }}>
                    {selectedGridInfo.cctvCount}
                  </div>
                  <button
                    onClick={() => setSelectedGridInfo(null)}
                    style={{
                      padding: '4px 8px',
                      borderRadius: '4px',
                      border: 'none',
                      backgroundColor: '#007bff',
                      color: 'white',
                      cursor: 'pointer'
                    }}
                  >
                    Close
                  </button>
                </div>
              </Popup>
            </Marker>
          )}

          {geoData && <Legend />}
        </MapContainer>
      </ResizableBox>
    </div>
  );
};

export default SafetyMap;
