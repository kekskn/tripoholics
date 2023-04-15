import React, { createElement } from "react";
import { Provider } from "react-redux";
import { render } from "react-dom";
import { Map } from "./components";
import store from "./redux/store";

function MapWrapper() {
  return (
    <Provider store={store}>
      <Map />
    </Provider>
  );
}

if (window.location.pathname.includes("members/myprofile")) {
  const mapWrapper = document.querySelector("#map");

  (function () {
    render(createElement(MapWrapper, {}, null), mapWrapper);
  })();
}
