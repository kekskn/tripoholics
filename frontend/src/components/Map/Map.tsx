import React, { useRef, useEffect, useState } from "react";
import mapboxgl from "mapbox-gl";

import Markerr from "./Markerr";
import "./Map.scss";
import { usePosition } from "../hooks/usePosition";
import ReactDOM from "react-dom";
import Popup from "./Popup/Popup";

mapboxgl.accessToken =
  "pk.eyJ1Ijoia2Vrc2tuIiwiYSI6ImNsYmo5M3o0czEwdWIzcHEzOG1oZTZ4enUifQ.fxi2SRHRvtqBeUyPlEjc4A";

function Map() {
  const position = usePosition();
  console.log("POSS:", position);
  const mapContainer = useRef(null);
  const map = useRef(null);
  // @ts-ignore
  const [lng, setLng] = useState(37.7442273);
  // @ts-ignore
  const [lat, setLat] = useState(55.6703166);
  const [zoom, setZoom] = useState(9);

  useEffect(() => {
    if (map.current) return; // initialize map only once
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/streets-v12",
      center: [lng, lat],
      zoom: zoom,
    });
    map.current.on("move", () => {
      setLng(map.current.getCenter().lng.toFixed(4));
      setLat(map.current.getCenter().lat.toFixed(4));
      setZoom(map.current.getZoom().toFixed(2));
    });

    // const div = document.createElement("DIV");
    // div.style.background = "red";
    // div.style.width = "20px";
    // div.style.height = "20px";
    // div.addEventListener("click", () => console.log("CLICKED!"));

    // Create a default Marker and add it to the map.
    // const marker1 = new mapboxgl.Marker({ draggable: true, element: div })
    //   .setLngLat([37.7442273, 55.6703166])
    //   .addTo(map.current);
  });

  useEffect(() => {
    const arr = [
      { lng: 37.7442273, lat: 55.6703166 },
      { lng: 37.4935, lat: 55.69461 },
      { lng: 37.683103, lat: 55.804368 },
    ];
    const div = document.createElement("DIV");
    div.style.background = "red";
    div.style.width = "20px";
    div.style.height = "20px";
    div.addEventListener("click", () => console.log("CLICKED!"));

    const geojson = {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          properties: {
            message: "Foo",
            iconSize: [60, 60],
          },
          geometry: {
            type: "Point",
            coordinates: [37.7442273, 55.6703166],
          },
        },
        {
          type: "Feature",
          properties: {
            message: "Bar",
            iconSize: [50, 50],
          },
          geometry: {
            type: "Point",
            coordinates: [37.4935, 55.69461],
          },
        },
      ],
    };

    geojson.features.map((marker) => {
      const popupNode = document.createElement("div");
      ReactDOM.render(<Popup />, popupNode);
      const popup = new mapboxgl.Popup({
        // offset: popupOffsets,
        className: "mapbox__popup-wrapper",
      })
        // @ts-ignore
        .setDOMContent(popupNode)
        .setMaxWidth("350px")
        .addTo(map.current);

      // Add markers to the map.
      new mapboxgl.Marker()
        .setLngLat(marker.geometry.coordinates)
        .setPopup(popup)
        .addTo(map.current);
    });
    // @ts-ignore
    if (position.latitude && position.longitude) {
      const markerHeight = 10;
      const markerRadius = 10;
      const linearOffset = 25;
      const popupOffsets = {
        top: [0, 0],
        "top-left": [0, 0],
        "top-right": [0, 0],
        bottom: [0, -markerHeight],
        "bottom-left": [
          linearOffset,
          (markerHeight - markerRadius + linearOffset) * -1,
        ],
        "bottom-right": [
          -linearOffset,
          (markerHeight - markerRadius + linearOffset) * -1,
        ],
        left: [markerRadius, (markerHeight - markerRadius) * -1],
        right: [-markerRadius, (markerHeight - markerRadius) * -1],
      };
    }
    //   @ts-ignore
  }, [position.latitude, position.longitude]);

  return (
    <div>
      <div ref={mapContainer} className="map-container" />
    </div>
  );
}

export default Map;
