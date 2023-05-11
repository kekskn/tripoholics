import React, { useState } from "react";

import { Oval } from "react-loader-spinner";
import "./Popup.scss";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { createNewDialog, fetchUserPopupInfo } from "src/redux/actions";
import { RootState } from "src/redux/store";
import { getUserPopupInfo } from "src/api";
import PopupUserInfo from "./components/PopupUserInfo";

function Popup({ userId }) {
  const isLoadingUserPopupInfo = useSelector(
    (state: RootState) => state.map.isLoading
  );

  return (
    <div className="map__popup-wrapper">
      {isLoadingUserPopupInfo ? (
        <Oval
          height={100}
          width={100}
          color="#e13f3e"
          wrapperStyle={{
            width: "100%",
            alignItems: "center",
            justifyContent: "center",
          }}
          wrapperClass=""
          visible={true}
          ariaLabel="oval-loading"
          secondaryColor="#e13f3e"
          strokeWidth={2}
          strokeWidthSecondary={2}
        />
      ) : (
        <PopupUserInfo userId={userId} />
      )}
    </div>
  );
}

export default Popup;
