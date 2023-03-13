import React from "react";
import styled from "styled-components";

import redMarker from "../../../static/photos/icons/red-marker.png";
import blueMarker from "../../../static/photos/icons/blue-marker.png";

export default function Marker({ isCurrentUser }) {
  console.log("isCurrentUser", isCurrentUser);
  return <MarkerWrapper isCurrentUser={isCurrentUser} />;
}

// const el = document.createElement("div");
// el.className = "marker";

// el.style.backgroundImage = `url(${
//   marker.properties.isCurrentUser ? blueMarker : redMarker
// })`;
// el.style.width = "35px";
// el.style.height = "35px";
// el.style.backgroundSize = "100%";

const MarkerWrapper = styled.div<{ isCurrentUser: boolean }>`
  background-image: ${({ isCurrentUser }) =>
    isCurrentUser ? `url(${blueMarker})` : `url(${redMarker})`};
  width: 35px;
  height: 35px;
`;
