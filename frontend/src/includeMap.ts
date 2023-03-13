import { createElement } from "react";
import { render } from "react-dom";
import { Map } from "./components";

if (window.location.pathname.includes("members/myprofile")) {
  const mapWrapper = document.querySelector("#map");

  (function () {
    render(createElement(Map, {}, null), mapWrapper);
  })();
}
