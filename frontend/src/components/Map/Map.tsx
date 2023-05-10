import React, { useRef, useEffect, useState, memo } from "react";
import mapboxgl from "mapbox-gl";
import MapboxLanguage from "@mapbox/mapbox-gl-language";

import "./Map.scss";
import { usePosition } from "../hooks/usePosition";
import ReactDOM from "react-dom";
import Popup from "./Popup/Popup";

// import { Marker as MarkerComponent } from "./Marker";
import Marker from "./Marker";
import redMarker from "../../../static/photos/icons/red-marker.png";
import blueMarker from "../../../static/photos/icons/blue-marker.png";

import { popupOffsets } from "./helpers/popupOffset";
import { Provider, useDispatch } from "react-redux";
import store from "src/redux/store";
import { fetchUserPopupInfo } from "src/redux/actions";

mapboxgl.accessToken =
  "pk.eyJ1Ijoia2Vrc2tuIiwiYSI6ImNsYmo5M3o0czEwdWIzcHEzOG1oZTZ4enUifQ.fxi2SRHRvtqBeUyPlEjc4A";

function Map() {
  const { latitude: lat, longitude: lng } = usePosition();
  console.log("POSS:", lat, lng);
  const mapContainer = useRef(null);
  const map = useRef(null);

  const dispatch = useDispatch();

  //   const mar = useRef(Marker);

  useEffect(() => {
    if (map.current) return; // initialize map only once
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/streets-v12",
      zoom: 9,
    });
    mapboxgl.setRTLTextPlugin(
      "https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text/v0.1.0/mapbox-gl-rtl-text.js"
    );
    var mapboxLanguage = new MapboxLanguage({
      defaultLanguage: "ru",
    });

    map.current.addControl(mapboxLanguage);
  });

  useEffect(() => {
    const arr = [
      { lng: 37.7442273, lat: 55.6703166 },
      { lng: 37.4935, lat: 55.69461 },
      { lng: 37.683103, lat: 55.804368 },
    ];

    const geojson = {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          properties: {
            isCurrentUser: false,
          },
          geometry: {
            type: "Point",
            coordinates: [37.4935, 55.69461],
          },
        },
      ],
    };

    if (lat && lng) {
      map.current.flyTo({ center: [lng, lat], speed: 0.8 });
      geojson.features.push({
        type: "Feature",
        properties: {
          isCurrentUser: true,
        },
        geometry: {
          type: "Point",
          coordinates: [lng, lat],
        },
      });
      geojson.features.map((marker) => {
        const popupNode = document.createElement("div");
        ReactDOM.render(
          <Provider store={store}>
            <Popup userId={12} />
          </Provider>,
          popupNode
        );

        const popup = new mapboxgl.Popup({
          offset: popupOffsets,
          className: "mapbox__popup-wrapper",
        })
          .setDOMContent(popupNode)
          .setMaxWidth("350px")
          .addTo(map.current);

        const el = document.createElement("div");
        el.className = "marker";

        el.style.backgroundImage = `url(${
          marker.properties.isCurrentUser ? blueMarker : redMarker
        })`;
        el.style.width = "35px";
        el.style.height = "35px";
        el.style.backgroundSize = "100%";

        // Add markers to the map.
        new mapboxgl.Marker(el)
          .setLngLat(marker.geometry.coordinates)
          .setPopup(popup)
          .setOffset([0, -17])
          .addTo(map.current);

        popup.on("open", () => {
          console.log("opened popup");
          dispatch(fetchUserPopupInfo(12));
          const { lng, lat } = popup.getLngLat();
          map.current.flyTo({
            center: [lng, lat],
            zoom: 12,
            speed: 0.6,
          });
        });
      });
    }
  }, [lat, lng]);

  return (
    <div>
      <div ref={mapContainer} className="map-container" />
    </div>
  );
}

export default memo(Map);
